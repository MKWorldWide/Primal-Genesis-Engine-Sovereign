#!/usr/bin/env python3
"""
AthenaMist Setup Script
Easy installation and configuration
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command: str, description: str):
    """Run a command with error handling"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python version {version.major}.{version.minor}.{version.micro} is compatible!")
    return True

def create_virtual_environment():
    """Create virtual environment if it doesn't exist"""
    venv_path = Path("venv")
    if venv_path.exists():
        print("✅ Virtual environment already exists!")
        return True
    
    return run_command("python3 -m venv venv", "Creating virtual environment")

def install_dependencies():
    """Install required dependencies"""
    # Activate virtual environment and install packages
    if os.name == 'nt':  # Windows
        pip_cmd = "venv\\Scripts\\pip"
    else:  # Unix/Linux/macOS
        pip_cmd = "venv/bin/pip"
    
    return run_command(f"{pip_cmd} install -r requirements.txt", "Installing dependencies")

def setup_configuration():
    """Run configuration setup"""
    print("\n🔧 Configuration Setup")
    print("=" * 40)
    
    # Import and run config setup
    try:
        from config import setup_api_keys
        setup_api_keys()
        return True
    except Exception as e:
        print(f"❌ Configuration setup failed: {e}")
        return False

def main():
    """Main setup function"""
    print("🌟 AthenaMist AI Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Setup configuration
    if not setup_configuration():
        print("⚠️  Configuration setup failed, but you can still run AthenaMist with default settings.")
    
    print("\n🎉 Setup complete!")
    print("\n🚀 To start AthenaMist:")
    print("  ./run_athenamist.sh")
    print("\n📖 For more information, see README.md")

if __name__ == "__main__":
    main() 