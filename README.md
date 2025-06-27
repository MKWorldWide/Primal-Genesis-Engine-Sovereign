# 🌟 AthenaMist AI - Clean Edition

A powerful AI assistant for creative workflows and government contract data, inspired by Skyrim mods.

## 🚀 Quick Start

```bash
# Run setup (first time only)
python3 setup.py

# Or manually:
source venv/bin/activate
cd athenamist_integration
python3 standalone_demo.py
```

## 🤖 AI Integration

AthenaMist now supports real AI providers for intelligent responses:

### **Mistral AI** (Recommended)
- Free tier available
- Excellent performance
- Get API key: https://console.mistral.ai/

### **OpenAI**
- GPT-4o and GPT-3.5-turbo support
- Get API key: https://platform.openai.com/api-keys

### **Setup AI Integration**
```bash
# Option 1: Interactive setup
python3 setup.py

# Option 2: Environment variables
export MISTRAL_API_KEY="your_mistral_api_key"
export OPENAI_API_KEY="your_openai_api_key"

# Option 3: In-app configuration
/set_api_key mistral your_api_key_here
/set_api_key openai your_api_key_here
```

## 🏛️ Features

- **Real AI Responses** - Powered by Mistral AI or OpenAI
- **Creative AI Assistant** - Multiple personality modes (Creative, Technical, Workflow, Government)
- **SAM Integration** - US Government contract data and entity search
- **Standalone Mode** - Works without Blender installation
- **Interactive Chat** - Natural language processing with context awareness
- **Configuration Management** - Easy API key setup and management

## 🎮 Commands

- `/help` - Show this help
- `/mode <mode>` - Switch AI mode (creative/technical/workflow/government)
- `/suggestions` - Get workflow suggestions
- `/insights` - Show AI insights
- `/history` - Show conversation history
- `/clear` - Clear conversation history
- `/sam_status` - Check SAM integration status
- `/ai_status` - Check AI integration status
- `/set_api_key` - Set AI API key
- `/quit` - Exit AthenaMist

## 🏛️ SAM Integration

Connected to US Government System for Award Management (SAM) database:
- Search for government entities and companies
- Find contract opportunities
- Analyze government contracting data
- Get detailed entity information

## 📁 Project Structure

```
AthenaMist_Clean/
├── athenamist_integration/
│   ├── core/
│   │   ├── ai_integration.py        # AI provider integration
│   │   └── sam_integration.py       # SAM API integration
│   └── standalone_demo.py           # Main demo application
├── venv/                            # Python virtual environment
├── config.py                        # Configuration management
├── setup.py                         # Setup script
├── requirements.txt                 # Python dependencies
├── run_athenamist.sh               # Launcher script
└── README.md                       # This file
```

## 🔧 Requirements

- Python 3.8+
- requests
- aiohttp
- openai (optional)
- mistralai (optional)

## 🎯 Usage Examples

```bash
# Start with real AI
python3 setup.py  # Configure API keys first
./run_athenamist.sh

# Ask about government contracts
"Show me recent contract opportunities"

# Search for companies
"Search for software companies"

# Get workflow suggestions
/suggestions

# Check AI status
/ai_status
```

## 🔑 API Key Setup

### Mistral AI (Recommended)
1. Visit https://console.mistral.ai/
2. Create account and get API key
3. Run `python3 setup.py` or set environment variable:
   ```bash
   export MISTRAL_API_KEY="your_api_key_here"
   ```

### OpenAI
1. Visit https://platform.openai.com/api-keys
2. Create account and get API key
3. Run `python3 setup.py` or set environment variable:
   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

## 🌟 Inspired by Skyrim Mods

AthenaMist brings the immersive, detailed approach of Skyrim modding to AI assistance, providing rich context and creative inspiration for your workflows.

## 🚀 Performance

- **Clean Architecture** - Streamlined codebase for fast enumeration
- **Real AI Integration** - No more mock responses
- **Efficient Caching** - Optimized for performance
- **Minimal Dependencies** - Only essential packages included 