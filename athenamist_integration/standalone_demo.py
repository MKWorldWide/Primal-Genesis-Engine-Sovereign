#!/usr/bin/env python3
"""
AthenaMist AI - Standalone Demo with Real AI Integration
A powerful AI assistant for creative workflows and government contract data
"""

import asyncio
import json
import random
import time
import os
from typing import Dict, List, Optional
import requests
import aiohttp

# Import AI and SAM integration
from core.sam_integration import SAMIntegration, AthenaMistSAMIntegration
from core.ai_integration import AIIntegrationManager, configure_ai_provider

class AthenaMistAI:
    """AthenaMist AI Core - Standalone Version with Real AI Integration"""
    
    def __init__(self, mode: str = "creative", ai_provider: str = "mistral", ai_api_key: str = None):
        self.mode = mode
        self.personality = self._get_personality(mode)
        self.conversation_history = []
        self.workflow_suggestions = []
        
        # Initialize AI integration
        self.ai_manager = configure_ai_provider(ai_provider, ai_api_key)
        
        # Initialize SAM integration with the provided API key
        sam_api_key = "gkwM6H5pnxU2qEkPJLp4UT9OwBfuLLonsovaU2Im"
        self.sam_integration = SAMIntegration(sam_api_key)
        self.sam_ai = AthenaMistSAMIntegration(self.sam_integration)
        
    def _get_personality(self, mode: str) -> Dict:
        """Get AI personality based on mode"""
        personalities = {
            "creative": {
                "name": "AthenaMist Creative",
                "style": "inspiring and artistic",
                "focus": "creative workflows and artistic expression",
                "greeting": "🌟 Greetings, creative soul! I am AthenaMist, your AI companion for artistic endeavors and government contract insights. What shall we create today?"
            },
            "technical": {
                "name": "AthenaMist Technical",
                "style": "precise and analytical",
                "focus": "technical workflows and optimization",
                "greeting": "⚙️ Hello! I am AthenaMist Technical, your AI assistant for precise workflows, optimization, and government contract analysis. How may I assist you?"
            },
            "workflow": {
                "name": "AthenaMist Workflow",
                "style": "efficient and organized",
                "focus": "workflow automation and productivity",
                "greeting": "🚀 Welcome! I am AthenaMist Workflow, your AI partner for streamlined productivity and government contract opportunities. Let's optimize your workflow!"
            },
            "government": {
                "name": "AthenaMist Government",
                "style": "official and comprehensive",
                "focus": "government contracts and SAM data analysis",
                "greeting": "🏛️ Greetings! I am AthenaMist Government, your AI specialist for US Government contracts and SAM database insights. How can I help with your government contracting needs?"
            }
        }
        return personalities.get(mode, personalities["creative"])
    
    async def process_query(self, query: str) -> str:
        """Process user query and generate response"""
        # Add to conversation history
        self.conversation_history.append({"user": query, "timestamp": time.time()})
        
        # Check if this is a SAM-related query
        sam_keywords = ['sam', 'government', 'contract', 'opportunity', 'entity', 'duns', 'federal', 'agency']
        query_lower = query.lower()
        
        if any(keyword in query_lower for keyword in sam_keywords):
            # Handle SAM-related queries
            response = await self.sam_ai.process_sam_query(query)
        else:
            # Use real AI for other queries
            response = await self._generate_ai_response(query)
        
        # Add response to history
        self.conversation_history.append({"ai": response, "timestamp": time.time()})
        
        return response
    
    async def _generate_ai_response(self, query: str) -> str:
        """Generate response using real AI provider"""
        try:
            # Build context from conversation history
            context = self._build_context()
            
            # Generate response using AI provider
            response = await self.ai_manager.generate_response(query, context, self.mode)
            return response
            
        except Exception as e:
            # Fallback to mock response if AI fails
            return self._generate_fallback_response(query)
    
    def _build_context(self) -> str:
        """Build context from recent conversation history"""
        if not self.conversation_history:
            return ""
        
        # Get last 4 exchanges for context
        recent_history = self.conversation_history[-8:]  # 4 exchanges (user + ai pairs)
        context_parts = []
        
        for entry in recent_history:
            if "user" in entry:
                context_parts.append(f"User: {entry['user']}")
            elif "ai" in entry:
                context_parts.append(f"Assistant: {entry['ai']}")
        
        return "\n".join(context_parts)
    
    def _generate_fallback_response(self, query: str) -> str:
        """Generate fallback response when AI is unavailable"""
        query_lower = query.lower()
        
        # Creative mode responses
        if self.mode == "creative":
            if "lighting" in query_lower:
                return "✨ For dramatic lighting, try using three-point lighting with a key light at 45°, fill light at 90°, and back light for separation. Consider using warm tones for intimate scenes and cool tones for dramatic effects!"
            elif "texture" in query_lower:
                return "🎨 Texture creation is an art! Start with high-resolution base textures, add procedural noise for realism, and layer multiple textures for depth. Remember to consider scale and UV mapping!"
            elif "animation" in query_lower:
                return "🎬 Animation is storytelling in motion! Start with strong keyframes, use easing curves for natural movement, and remember the 12 principles of animation. What story are you telling?"
            else:
                return "🌟 Your creative vision is unique! Let me help you bring it to life. What specific aspect of your project would you like to explore?"
        
        # Technical mode responses
        elif self.mode == "technical":
            if "optimize" in query_lower:
                return "⚙️ Optimization is key! Consider polygon count, texture resolution, and render settings. Use LOD (Level of Detail) systems and efficient UV mapping for better performance."
            elif "render" in query_lower:
                return "🖥️ Rendering efficiently requires balance. Use denoising, optimize light bounces, and consider GPU rendering for faster results. What render engine are you using?"
            elif "script" in query_lower:
                return "📝 Scripting can automate repetitive tasks! Python integration allows for custom tools and workflows. What specific task would you like to automate?"
            else:
                return "⚙️ Technical precision leads to better results! How can I help you optimize your workflow today?"
        
        # Workflow mode responses
        elif self.mode == "workflow":
            if "workflow" in query_lower:
                return "🚀 Efficient workflows save time and reduce errors! Consider using asset libraries, template files, and automated processes. What workflow would you like to streamline?"
            elif "organize" in query_lower:
                return "📁 Organization is the foundation of productivity! Use consistent naming conventions, folder structures, and version control. How can I help you organize your project?"
            elif "automate" in query_lower:
                return "🤖 Automation frees you to focus on creativity! Scripts, macros, and batch processing can handle repetitive tasks. What would you like to automate?"
            else:
                return "🚀 Let's make your workflow more efficient! What process would you like to optimize today?"
        
        # Government mode responses
        else:
            if "government" in query_lower or "contract" in query_lower:
                return "🏛️ I'm connected to the US Government's SAM database! I can help you find contract opportunities, search for entities, and analyze government contracting data. What would you like to explore?"
            elif "opportunity" in query_lower:
                return "📋 I can show you recent government contract opportunities! Would you like me to search for specific types of contracts or agencies?"
            elif "search" in query_lower:
                return "🔍 I can search the SAM database for companies, organizations, or specific entities. What would you like to search for?"
            else:
                return "🏛️ I'm your AI assistant for government contracting and SAM data analysis. How can I help with your government contracting needs?"
    
    def get_workflow_suggestions(self) -> List[str]:
        """Get workflow suggestions based on current mode"""
        suggestions = {
            "creative": [
                "🎨 Create a mood board for your project",
                "✨ Experiment with different lighting setups",
                "🎭 Develop character concepts and backstories",
                "🌍 Design environmental storytelling elements",
                "🎬 Plan camera movements and composition"
            ],
            "technical": [
                "⚙️ Optimize polygon count and topology",
                "🖥️ Set up efficient render settings",
                "📐 Create precise measurements and proportions",
                "🔧 Develop custom tools and scripts",
                "📊 Analyze performance metrics"
            ],
            "workflow": [
                "📁 Organize project files and assets",
                "🔄 Create reusable templates and presets",
                "⏱️ Set up time tracking and milestones",
                "🤖 Automate repetitive tasks",
                "📋 Establish quality control checklists"
            ],
            "government": [
                "🏛️ Search for government contract opportunities",
                "🔍 Look up companies in the SAM database",
                "📊 Analyze government contracting trends",
                "📋 Review recent contract awards",
                "🏢 Research potential business partners"
            ]
        }
        return suggestions.get(self.mode, suggestions["creative"])
    
    def get_ai_insights(self) -> Dict:
        """Get AI insights and recommendations"""
        sam_status = self.sam_integration.get_integration_status()
        ai_status = self.ai_manager.get_status()
        
        return {
            "mode": self.mode,
            "personality": self.personality["name"],
            "conversation_count": len(self.conversation_history) // 2,
            "suggestions": self.get_workflow_suggestions(),
            "ai_integration": {
                "provider": ai_status['provider'],
                "enabled": ai_status['api_key_valid'],
                "status": "Connected" if ai_status['api_key_valid'] else "Not Connected"
            },
            "sam_integration": {
                "enabled": sam_status['api_key_valid'],
                "status": "Connected" if sam_status['api_key_valid'] else "Not Connected"
            },
            "recommendations": [
                "Consider taking breaks every 2 hours for optimal creativity",
                "Save your work frequently and use version control",
                "Experiment with different approaches to find what works best",
                "Collaborate with others for fresh perspectives",
                "Explore government contract opportunities for business growth" if sam_status['api_key_valid'] else "Configure SAM API key to access government contract data",
                f"Configure {ai_status['provider'].title()} API key for enhanced AI responses" if not ai_status['api_key_valid'] else f"Using {ai_status['provider'].title()} for AI responses"
            ]
        }

class StandaloneDemo:
    """Standalone AthenaMist Demo Interface with Real AI Integration"""
    
    def __init__(self):
        # Check for API keys in environment
        mistral_key = os.getenv("MISTRAL_API_KEY", "")
        openai_key = os.getenv("OPENAI_API_KEY", "")
        
        # Default to Mistral if available, otherwise OpenAI, otherwise mock mode
        if mistral_key:
            self.ai = AthenaMistAI("creative", "mistral", mistral_key)
        elif openai_key:
            self.ai = AthenaMistAI("creative", "openai", openai_key)
        else:
            self.ai = AthenaMistAI("creative", "mock")
        
        self.running = True
    
    def print_banner(self):
        """Print AthenaMist banner"""
        ai_status = self.ai.ai_manager.get_status()
        provider_name = ai_status['provider'].title() if ai_status['api_key_valid'] else "Mock"
        
        banner = f"""
╔══════════════════════════════════════════════════════════════╗
║                    🌟 ATHENAMIST AI 🌟                       ║
║              Your Creative AI Companion                      ║
║                                                              ║
║  Inspired by Skyrim Mods • Built for Creativity             ║
║  Modes: Creative • Technical • Workflow • Government        ║
║  🏛️ SAM Integration: Government Contract Data               ║
║  🤖 AI Provider: {provider_name:<42} ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def print_help(self):
        """Print help information"""
        help_text = """
🎮 COMMANDS:
  /help          - Show this help
  /mode <mode>   - Switch AI mode (creative/technical/workflow/government)
  /suggestions   - Get workflow suggestions
  /insights      - Show AI insights
  /history       - Show conversation history
  /clear         - Clear conversation history
  /sam_status    - Check SAM integration status
  /ai_status     - Check AI integration status
  /set_api_key   - Set AI API key
  /quit          - Exit AthenaMist

💡 TIPS:
  - Ask me anything about creative workflows
  - I can help with technical optimization
  - Let me suggest workflow improvements
  - I remember our conversation context
  - 🏛️ I'm connected to US Government SAM database!
  - 🤖 I use real AI for intelligent responses!
  - Try: "search for software companies" or "show contract opportunities"

🏛️ SAM FEATURES:
  - Search for government entities and companies
  - Find contract opportunities
  - Analyze government contracting data
  - Get detailed entity information

🤖 AI FEATURES:
  - Real AI responses using Mistral or OpenAI
  - Context-aware conversations
  - Multiple personality modes
  - Intelligent workflow suggestions
        """
        print(help_text)
    
    async def run(self):
        """Run the standalone demo"""
        self.print_banner()
        print(self.ai.personality["greeting"])
        print("\nType /help for commands or just start chatting!")
        print("─" * 60)
        
        while self.running:
            try:
                # Get user input
                user_input = input("\n🎯 You: ").strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.startswith("/"):
                    await self.handle_command(user_input)
                    continue
                
                # Process with AI
                print(f"\n🤖 {self.ai.personality['name']}: ", end="", flush=True)
                response = await self.ai.process_query(user_input)
                print(response)
                
            except KeyboardInterrupt:
                print("\n\n👋 Farewell! May your creativity flow like the rivers of Skyrim!")
                self.running = False
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
    
    async def handle_command(self, command: str):
        """Handle user commands"""
        parts = command.split()
        cmd = parts[0].lower()
        
        if cmd == "/help":
            self.print_help()
        
        elif cmd == "/mode":
            if len(parts) > 1:
                mode = parts[1].lower()
                if mode in ["creative", "technical", "workflow", "government"]:
                    self.ai = AthenaMistAI(mode, self.ai.ai_manager.provider_name, self.ai.ai_manager.api_key)
                    print(f"🔄 Switched to {mode} mode!")
                    print(self.ai.personality["greeting"])
                else:
                    print("❌ Invalid mode. Use: creative, technical, workflow, or government")
            else:
                print("❌ Usage: /mode <creative|technical|workflow|government>")
        
        elif cmd == "/suggestions":
            suggestions = self.ai.get_workflow_suggestions()
            print("\n💡 WORKFLOW SUGGESTIONS:")
            for i, suggestion in enumerate(suggestions, 1):
                print(f"  {i}. {suggestion}")
        
        elif cmd == "/insights":
            insights = self.ai.get_ai_insights()
            print(f"\n🧠 AI INSIGHTS:")
            print(f"  Mode: {insights['mode']}")
            print(f"  Personality: {insights['personality']}")
            print(f"  Conversations: {insights['conversation_count']}")
            print(f"  🤖 AI Integration: {insights['ai_integration']['status']} ({insights['ai_integration']['provider']})")
            print(f"  🏛️ SAM Integration: {insights['sam_integration']['status']}")
            print(f"\n📋 RECOMMENDATIONS:")
            for rec in insights['recommendations']:
                print(f"  • {rec}")
        
        elif cmd == "/ai_status":
            status = self.ai.ai_manager.get_status()
            print(f"\n🤖 AI INTEGRATION STATUS:")
            print(f"  Provider: {status['provider'].title()}")
            print(f"  API Key Configured: {'✅ Yes' if status['api_key_configured'] else '❌ No'}")
            print(f"  API Key Valid: {'✅ Yes' if status['api_key_valid'] else '❌ No'}")
            
            if status['api_key_valid']:
                print(f"\n🎉 AI integration is active! Using {status['provider'].title()} for responses.")
            else:
                print(f"\n🔑 To enable real AI responses, set your API key:")
                if status['provider'] == 'mistral':
                    print(f"  export MISTRAL_API_KEY='your_mistral_api_key'")
                elif status['provider'] == 'openai':
                    print(f"  export OPENAI_API_KEY='your_openai_api_key'")
        
        elif cmd == "/sam_status":
            status = self.ai.sam_integration.get_integration_status()
            test_result = await self.ai.sam_integration.test_connection()
            
            print(f"\n🏛️ SAM INTEGRATION STATUS:")
            print(f"  API Key Configured: {'✅ Yes' if status['api_key_configured'] else '❌ No'}")
            print(f"  API Key Valid: {'✅ Yes' if status['api_key_valid'] else '❌ No'}")
            print(f"  Connection Test: {'✅ Passed' if test_result['success'] else '❌ Failed'}")
            print(f"  Base URL: {status['base_url']}")
            
            if status['api_key_valid']:
                print(f"\n🎉 SAM integration is active! You can:")
                print(f"  • Search for government entities")
                print(f"  • Find contract opportunities")
                print(f"  • Analyze government contracting data")
        
        elif cmd == "/set_api_key":
            if len(parts) < 3:
                print("❌ Usage: /set_api_key <provider> <api_key>")
                print("  Example: /set_api_key mistral your_api_key_here")
                return
            
            provider = parts[1].lower()
            api_key = parts[2]
            
            if provider not in ["mistral", "openai"]:
                print("❌ Invalid provider. Use: mistral or openai")
                return
            
            try:
                self.ai.ai_manager.switch_provider(provider, api_key)
                print(f"✅ Successfully configured {provider.title()} API key!")
            except Exception as e:
                print(f"❌ Error configuring API key: {e}")
        
        elif cmd == "/history":
            if self.ai.conversation_history:
                print("\n📜 CONVERSATION HISTORY:")
                for i, entry in enumerate(self.ai.conversation_history[-10:], 1):
                    if "user" in entry:
                        print(f"  {i}. You: {entry['user']}")
                    elif "ai" in entry:
                        print(f"     AI: {entry['ai']}")
            else:
                print("📜 No conversation history yet.")
        
        elif cmd == "/clear":
            self.ai.conversation_history = []
            print("🗑️ Conversation history cleared!")
        
        elif cmd == "/quit":
            print("\n👋 Farewell! May your creativity flow like the rivers of Skyrim!")
            self.running = False
        
        else:
            print(f"❌ Unknown command: {cmd}")
            print("Type /help for available commands.")

async def main():
    """Main entry point"""
    demo = StandaloneDemo()
    await demo.run()

if __name__ == "__main__":
    asyncio.run(main()) 