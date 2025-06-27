#!/usr/bin/env python3
"""
AthenaMist Configuration
Easy API key management and settings
"""

import os
import json
from pathlib import Path

class Config:
    """Configuration manager for AthenaMist"""
    
    def __init__(self, config_file: str = "athenamist_config.json"):
        self.config_file = Path(config_file)
        self.config = self._load_config()
    
    def _load_config(self) -> dict:
        """Load configuration from file"""
        default_config = {
            "ai_provider": "mistral",  # "mistral" or "openai"
            "ai_api_key": "",
            "sam_api_key": "gkwM6H5pnxU2qEkPJLp4UT9OwBfuLLonsovaU2Im",
            "default_mode": "creative",
            "max_history": 50,
            "auto_save": True
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    loaded_config = json.load(f)
                    # Merge with defaults
                    default_config.update(loaded_config)
            except Exception as e:
                print(f"Warning: Could not load config file: {e}")
        
        return default_config
    
    def save_config(self):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save config file: {e}")
    
    def get(self, key: str, default=None):
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key: str, value):
        """Set configuration value"""
        self.config[key] = value
        self.save_config()
    
    def get_ai_api_key(self) -> str:
        """Get AI API key from config or environment"""
        # Check config first
        api_key = self.config.get("ai_api_key", "")
        if api_key:
            return api_key
        
        # Check environment variables
        provider = self.config.get("ai_provider", "mistral")
        if provider == "mistral":
            return os.getenv("MISTRAL_API_KEY", "")
        elif provider == "openai":
            return os.getenv("OPENAI_API_KEY", "")
        
        return ""
    
    def set_ai_api_key(self, api_key: str):
        """Set AI API key"""
        self.set("ai_api_key", api_key)
    
    def get_sam_api_key(self) -> str:
        """Get SAM API key"""
        return self.config.get("sam_api_key", "")
    
    def set_sam_api_key(self, api_key: str):
        """Set SAM API key"""
        self.set("sam_api_key", api_key)
    
    def get_ai_provider(self) -> str:
        """Get AI provider preference"""
        return self.config.get("ai_provider", "mistral")
    
    def set_ai_provider(self, provider: str):
        """Set AI provider preference"""
        if provider.lower() in ["mistral", "openai"]:
            self.set("ai_provider", provider.lower())
        else:
            raise ValueError("Provider must be 'mistral' or 'openai'")

# Global configuration instance
config = Config()

def setup_api_keys():
    """Interactive setup for API keys"""
    print("🔧 AthenaMist API Key Setup")
    print("=" * 40)
    
    # AI Provider setup
    print("\n🤖 AI Provider Setup:")
    print("1. Mistral AI (recommended)")
    print("2. OpenAI")
    
    while True:
        choice = input("Choose AI provider (1 or 2): ").strip()
        if choice == "1":
            config.set_ai_provider("mistral")
            break
        elif choice == "2":
            config.set_ai_provider("openai")
            break
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")
    
    # AI API Key setup
    provider = config.get_ai_provider()
    print(f"\n🔑 {provider.title()} API Key:")
    print(f"Get your API key from:")
    if provider == "mistral":
        print("  https://console.mistral.ai/")
    else:
        print("  https://platform.openai.com/api-keys")
    
    api_key = input(f"Enter your {provider.title()} API key (or press Enter to skip): ").strip()
    if api_key:
        config.set_ai_api_key(api_key)
        print("✅ API key saved!")
    else:
        print("⚠️  No API key provided. AthenaMist will use mock responses.")
    
    # SAM API Key setup (optional)
    print(f"\n🏛️ SAM API Key (optional):")
    sam_key = input("Enter SAM API key (or press Enter to use default): ").strip()
    if sam_key:
        config.set_sam_api_key(sam_key)
        print("✅ SAM API key updated!")
    else:
        print("✅ Using default SAM API key.")
    
    print("\n🎉 Setup complete! You can now run AthenaMist.")
    print("To change settings later, edit the config file or run setup again.")

if __name__ == "__main__":
    setup_api_keys() 