#!/usr/bin/env python3
"""
AthenaMist AI Integration Module
Supports Mistral AI and OpenAI APIs for real AI responses
"""

import os
import json
import asyncio
import aiohttp
from typing import Dict, List, Optional, Any
from datetime import datetime
import logging

class AIProvider:
    """Base class for AI providers"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.logger = logging.getLogger(__name__)
    
    async def generate_response(self, query: str, context: str = "", mode: str = "creative") -> str:
        """Generate AI response - to be implemented by subclasses"""
        raise NotImplementedError

class MistralAIProvider(AIProvider):
    """Mistral AI API Integration"""
    
    def __init__(self, api_key: str = None):
        super().__init__(api_key)
        self.base_url = "https://api.mistral.ai/v1"
        self.model = "mistral-large-latest"  # or "mistral-medium-latest"
    
    async def generate_response(self, query: str, context: str = "", mode: str = "creative") -> str:
        """Generate response using Mistral AI"""
        if not self.api_key:
            return "🔑 Mistral AI API key not configured. Please set your API key."
        
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            # Create system prompt based on mode
            system_prompt = self._get_system_prompt(mode)
            
            # Build messages
            messages = [
                {"role": "system", "content": system_prompt}
            ]
            
            if context:
                messages.append({"role": "user", "content": f"Context: {context}\n\nQuery: {query}"})
            else:
                messages.append({"role": "user", "content": query})
            
            payload = {
                "model": self.model,
                "messages": messages,
                "max_tokens": 1000,
                "temperature": 0.7,
                "top_p": 0.9
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.base_url}/chat/completions",
                    headers=headers,
                    json=payload
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data["choices"][0]["message"]["content"]
                    else:
                        error_text = await response.text()
                        self.logger.error(f"Mistral AI error: {response.status} - {error_text}")
                        return f"❌ Mistral AI Error: {response.status}"
                        
        except Exception as e:
            self.logger.error(f"Error calling Mistral AI: {e}")
            return f"❌ Error: {str(e)}"
    
    def _get_system_prompt(self, mode: str) -> str:
        """Get system prompt based on AI mode"""
        base_prompt = """You are AthenaMist, an AI assistant inspired by Skyrim mods. You help with creative workflows, technical optimization, and government contract data analysis. Be helpful, creative, and provide detailed, actionable advice."""
        
        mode_prompts = {
            "creative": "Focus on artistic and creative workflows. Provide inspiring, imaginative suggestions for creative projects.",
            "technical": "Focus on technical optimization and precise workflows. Provide detailed, technical advice and solutions.",
            "workflow": "Focus on workflow efficiency and productivity. Provide practical tips for streamlining processes.",
            "government": "Focus on government contracts and SAM data analysis. Provide insights about government contracting opportunities."
        }
        
        return f"{base_prompt} {mode_prompts.get(mode, '')}"

class OpenAIProvider(AIProvider):
    """OpenAI API Integration"""
    
    def __init__(self, api_key: str = None):
        super().__init__(api_key)
        self.base_url = "https://api.openai.com/v1"
        self.model = "gpt-4o"  # or "gpt-3.5-turbo"
    
    async def generate_response(self, query: str, context: str = "", mode: str = "creative") -> str:
        """Generate response using OpenAI"""
        if not self.api_key:
            return "🔑 OpenAI API key not configured. Please set your API key."
        
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            # Create system prompt based on mode
            system_prompt = self._get_system_prompt(mode)
            
            # Build messages
            messages = [
                {"role": "system", "content": system_prompt}
            ]
            
            if context:
                messages.append({"role": "user", "content": f"Context: {context}\n\nQuery: {query}"})
            else:
                messages.append({"role": "user", "content": query})
            
            payload = {
                "model": self.model,
                "messages": messages,
                "max_tokens": 1000,
                "temperature": 0.7,
                "top_p": 0.9
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.base_url}/chat/completions",
                    headers=headers,
                    json=payload
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data["choices"][0]["message"]["content"]
                    else:
                        error_text = await response.text()
                        self.logger.error(f"OpenAI error: {response.status} - {error_text}")
                        return f"❌ OpenAI Error: {response.status}"
                        
        except Exception as e:
            self.logger.error(f"Error calling OpenAI: {e}")
            return f"❌ Error: {str(e)}"
    
    def _get_system_prompt(self, mode: str) -> str:
        """Get system prompt based on AI mode"""
        base_prompt = """You are AthenaMist, an AI assistant inspired by Skyrim mods. You help with creative workflows, technical optimization, and government contract data analysis. Be helpful, creative, and provide detailed, actionable advice."""
        
        mode_prompts = {
            "creative": "Focus on artistic and creative workflows. Provide inspiring, imaginative suggestions for creative projects.",
            "technical": "Focus on technical optimization and precise workflows. Provide detailed, technical advice and solutions.",
            "workflow": "Focus on workflow efficiency and productivity. Provide practical tips for streamlining processes.",
            "government": "Focus on government contracts and SAM data analysis. Provide insights about government contracting opportunities."
        }
        
        return f"{base_prompt} {mode_prompts.get(mode, '')}"

class AIIntegrationManager:
    """Manages AI provider integration"""
    
    def __init__(self, provider: str = "mistral", api_key: str = None):
        """
        Initialize AI integration manager
        
        Args:
            provider: "mistral" or "openai"
            api_key: API key for the selected provider
        """
        self.provider_name = provider.lower()
        self.api_key = api_key or self._get_api_key_from_env()
        
        if self.provider_name == "mistral":
            self.provider = MistralAIProvider(self.api_key)
        elif self.provider_name == "openai":
            self.provider = OpenAIProvider(self.api_key)
        else:
            raise ValueError(f"Unsupported provider: {provider}")
        
        self.logger = logging.getLogger(__name__)
    
    def _get_api_key_from_env(self) -> str:
        """Get API key from environment variables"""
        if self.provider_name == "mistral":
            return os.getenv("MISTRAL_API_KEY", "")
        elif self.provider_name == "openai":
            return os.getenv("OPENAI_API_KEY", "")
        return ""
    
    async def generate_response(self, query: str, context: str = "", mode: str = "creative") -> str:
        """Generate AI response using the configured provider"""
        return await self.provider.generate_response(query, context, mode)
    
    def get_status(self) -> Dict[str, Any]:
        """Get AI integration status"""
        return {
            "provider": self.provider_name,
            "api_key_configured": bool(self.api_key),
            "api_key_valid": len(self.api_key) > 0 if self.api_key else False,
            "timestamp": datetime.now().isoformat()
        }
    
    def update_api_key(self, api_key: str):
        """Update API key"""
        self.api_key = api_key
        self.provider.api_key = api_key
    
    def switch_provider(self, provider: str, api_key: str = None):
        """Switch to different AI provider"""
        self.provider_name = provider.lower()
        self.api_key = api_key or self._get_api_key_from_env()
        
        if self.provider_name == "mistral":
            self.provider = MistralAIProvider(self.api_key)
        elif self.provider_name == "openai":
            self.provider = OpenAIProvider(self.api_key)
        else:
            raise ValueError(f"Unsupported provider: {provider}")

# Configuration helper
def configure_ai_provider(provider: str = "mistral", api_key: str = None) -> AIIntegrationManager:
    """
    Configure AI provider
    
    Args:
        provider: "mistral" or "openai"
        api_key: API key (optional, will use environment variable if not provided)
    
    Returns:
        Configured AI integration manager
    """
    return AIIntegrationManager(provider, api_key) 