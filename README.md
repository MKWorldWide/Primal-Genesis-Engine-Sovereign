# �� AthenaMist-Blended 2.0 - Advanced AI Integration Framework

A powerful AI assistant framework for creative workflows and government contract data analysis, inspired by the immersive world of Skyrim mods. AthenaMist-Blended 2.0 provides seamless integration with multiple AI providers, comprehensive government contract data access, and a modern web interface.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Internet connection for AI provider APIs
- SAM API access (optional, default key provided)

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd AthenaMist-Blended

# Run setup (first time only)
python3 setup.py

# Install dependencies
pip install -r requirements.txt

# Launch web interface
python3 run_web_interface.py

# Or use the command-line interface
cd athenamist_integration
python3 standalone_demo.py
```

### Quick Launch
```bash
# Use the convenient launcher scripts
./run_athenamist.sh          # Command-line interface
python3 run_web_interface.py # Web interface
```

## 🤖 AI Integration

AthenaMist-Blended 2.0 supports **7 major AI providers** for intelligent responses with advanced features:

### **Mistral AI** (Recommended)
- **Free Tier**: Available with generous limits
- **Performance**: Excellent response quality and speed
- **Models**: Mistral Large and Medium variants
- **Rate Limits**: 20 requests/minute (free), 1000 requests/minute (paid)
- **Get API Key**: https://console.mistral.ai/

### **OpenAI**
- **Models**: GPT-4o and GPT-3.5-turbo support
- **Features**: Advanced reasoning and analysis
- **Rate Limits**: 500 requests/minute (GPT-4o), 3500 requests/minute (GPT-3.5-turbo)
- **Get API Key**: https://platform.openai.com/api-keys

### **Anthropic Claude**
- **Models**: Claude 3.5 Sonnet, Claude 3 Opus
- **Features**: Advanced reasoning, safety-focused
- **Rate Limits**: 500 requests/minute (Sonnet), 200 requests/minute (Opus)
- **Get API Key**: https://console.anthropic.com/

### **Google Gemini**
- **Models**: Gemini Pro, Gemini Flash
- **Features**: Multimodal capabilities, Google integration
- **Rate Limits**: 1000 requests/minute (Pro), 2000 requests/minute (Flash)
- **Get API Key**: https://aistudio.google.com/

### **Cohere**
- **Models**: Command, Command Light
- **Features**: Enterprise-focused, multilingual support
- **Rate Limits**: 1000 requests/minute (Command), 2000 requests/minute (Light)
- **Get API Key**: https://cohere.com/

### **DeepSeek**
- **Models**: DeepSeek Chat, DeepSeek Coder
- **Features**: Code generation, technical expertise
- **Rate Limits**: 50 requests/minute (free), 2000 requests/minute (paid)
- **Get API Key**: https://platform.deepseek.com/

### **Phantom AI** (Ethereal)
- **Features**: Mystical workflow enhancement, shadow tendrils
- **Capabilities**: Ethereal response generation, phantom-powered analytics
- **Integration**: Advanced mystical capabilities

### **AI Provider Setup**

#### Option 1: Interactive Setup (Recommended)
```bash
python3 setup.py
```

#### Option 2: Environment Variables (Secure)
```bash
# For Mistral AI
export MISTRAL_API_KEY="your_mistral_api_key"

# For OpenAI
export OPENAI_API_KEY="your_openai_api_key"

# For Claude
export ANTHROPIC_API_KEY="your_anthropic_api_key"

# For Gemini
export GOOGLE_API_KEY="your_google_api_key"

# For Cohere
export COHERE_API_KEY="your_cohere_api_key"

# For DeepSeek
export DEEPSEEK_API_KEY="your_deepseek_api_key"
```

#### Option 3: In-App Configuration
```
/set_api_key mistral your_api_key_here
/set_api_key openai your_api_key_here
/set_api_key claude your_api_key_here
/set_api_key gemini your_api_key_here
/set_api_key cohere your_api_key_here
/set_api_key deepseek your_api_key_here
```

## 🌐 Web Interface

AthenaMist-Blended 2.0 includes a modern, responsive web interface with real-time capabilities:

### **Features**
- **Real-time Chat**: WebSocket-powered instant messaging with AI
- **Multi-Provider Support**: Switch between AI providers seamlessly
- **Government Data Integration**: Direct SAM database access
- **Performance Monitoring**: Real-time system health and metrics
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern UI**: Beautiful, intuitive interface with dark/light themes

### **Launch Web Interface**
```bash
# Launch with default settings
python3 run_web_interface.py

# Launch on specific host and port
python3 run_web_interface.py --host 127.0.0.1 --port 8080

# Launch in debug mode
python3 run_web_interface.py --debug
```

### **Web Interface URLs**
- **Main Interface**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc

## 🏛️ Features

### **Core Capabilities**
- **Multi-Provider AI Integration** - Seamless switching between 7 AI providers
- **Real AI Responses** - Powered by state-of-the-art language models
- **Creative AI Assistant** - Multiple personality modes (Creative, Technical, Workflow, Government)
- **SAM Integration** - US Government contract data and entity search
- **Web Interface** - Modern, responsive web application
- **Standalone Mode** - Works without external dependencies
- **Interactive Chat** - Natural language processing with context awareness
- **Configuration Management** - Easy API key setup and management

### **Advanced Features**
- **Async Architecture** - High-performance concurrent processing
- **Comprehensive Error Handling** - Robust retry logic and fallback mechanisms
- **Performance Monitoring** - Real-time metrics and optimization
- **Security Features** - API key encryption and secure storage
- **Caching System** - Intelligent response caching for performance
- **Rate Limiting** - Built-in protection against API abuse
- **WebSocket Support** - Real-time communication and updates
- **REST API** - Full API for external integrations

### **AI Personality Modes**
- **Creative Mode** - Artistic and imaginative responses for creative projects
- **Technical Mode** - Precise and analytical responses for technical workflows
- **Workflow Mode** - Practical and efficiency-focused advice
- **Government Mode** - SAM and contract-focused responses with official terminology

## 🎮 Commands

### **Core Commands**
- `/help` - Show comprehensive help and command list
- `/mode <mode>` - Switch AI mode (creative/technical/workflow/government)
- `/provider <provider>` - Switch AI provider
- `/suggestions` - Get workflow suggestions and recommendations
- `/insights` - Show AI insights and performance metrics
- `/history` - Show conversation history and context
- `/clear` - Clear conversation history and reset context

### **Status Commands**
- `/sam_status` - Check SAM integration status and connectivity
- `/ai_status` - Check AI integration status and provider health
- `/system_status` - Comprehensive system health and performance metrics
- `/providers` - List all supported AI providers and their status

### **Configuration Commands**
- `/set_api_key <provider> <key>` - Set AI API key for specified provider
- `/switch_provider <provider>` - Switch between AI providers
- `/config` - View current configuration settings
- `/reset_config` - Reset configuration to defaults

### **Utility Commands**
- `/quit` - Exit AthenaMist gracefully
- `/version` - Show current version and build information
- `/debug` - Enable debug mode for troubleshooting

## 🏛️ SAM Integration

Connected to US Government System for Award Management (SAM) database with advanced features:

### **Entity Search**
- Search for government entities and companies
- Filter by entity type and registration status
- Advanced search with multiple criteria
- Detailed entity information and history

### **Contract Opportunities**
- Find current contract opportunities
- Filter by keywords and opportunity type
- Analyze government contracting trends
- Track opportunity status and deadlines

### **Data Analysis**
- Comprehensive government contracting data
- Entity relationship mapping
- Contract value analysis
- Compliance and regulatory information

### **API Features**
- Secure API key management
- Rate limiting and caching
- Error handling and retry logic
- Real-time data updates

## 📁 Project Structure

```
AthenaMist-Blended/
├── athenamist_integration/          # Core integration framework
│   ├── core/                       # Core modules
│   │   ├── ai_integration.py       # AI provider management (7 providers)
│   │   ├── sam_integration.py      # SAM API integration
│   │   └── phantom_integration.py  # Phantom AI (ethereal capabilities)
│   ├── web/                        # Web interface
│   │   ├── app.py                  # FastAPI web application
│   │   ├── templates/              # HTML templates
│   │   └── static/                 # Static assets
│   └── standalone_demo.py          # Command-line interface
├── config.py                       # Configuration management
├── setup.py                        # Setup and installation wizard
├── run_web_interface.py           # Web interface launcher
├── requirements.txt                # Python dependencies
├── run_athenamist.sh              # Command-line launcher script
├── ARCHITECTURE.md                # Comprehensive architecture documentation
├── README.md                      # This documentation file
└── .gitignore                     # Git ignore patterns
```

### **Core Components**

#### **AI Integration Module** (`athenamist_integration/core/ai_integration.py`)
- Multi-provider AI integration (7 providers)
- Async request handling
- Performance monitoring
- Error handling and retry logic
- Mode-based personality switching

#### **SAM Integration Module** (`athenamist_integration/core/sam_integration.py`)
- Government contract data access
- Entity search and filtering
- Secure API key management
- Caching and performance optimization
- Comprehensive error handling

#### **Web Interface** (`athenamist_integration/web/app.py`)
- FastAPI web application
- WebSocket real-time communication
- REST API endpoints
- Modern responsive UI
- Performance monitoring

#### **Configuration Manager** (`config.py`)
- Centralized configuration management
- API key storage and retrieval
- Environment variable integration
- Interactive setup wizard
- Secure configuration persistence

#### **Standalone Demo** (`athenamist_integration/standalone_demo.py`)
- Command-line application interface
- Interactive command processing
- Real-time AI responses
- SAM data integration
- Performance monitoring

## 🔧 Requirements
```
requests>=2.32.0
aiohttp>=3.12.0
openai>=1.0.0
mistralai>=0.0.10
anthropic>=0.18.0
google-generativeai>=0.8.0
cohere>=4.0.0
cryptography>=41.0.0
python-dotenv>=1.0.0
asyncio-mqtt>=0.16.0
websockets>=12.0
fastapi>=0.104.0
uvicorn>=0.24.0
pydantic>=2.5.0
jinja2>=3.1.0
```

## 🚀 Getting Started

### **1. Installation**
```bash
# Clone and setup
git clone <repository-url>
cd AthenaMist-Blended
python3 setup.py
```

### **2. Configure API Keys**
```bash
# Set environment variables
export MISTRAL_API_KEY="your_mistral_api_key"
export OPENAI_API_KEY="your_openai_api_key"
# ... other providers as needed
```

### **3. Launch Application**
```bash
# Web interface (recommended)
python3 run_web_interface.py

# Command-line interface
cd athenamist_integration
python3 standalone_demo.py
```

### **4. Start Using**
- **Web Interface**: Open http://localhost:8000 in your browser
- **Command Line**: Use `/help` to see available commands
- **AI Providers**: Switch between providers with `/provider <name>`
- **Modes**: Change AI personality with `/mode <mode>`

## 🔒 Security

### **API Key Management**
- Secure encryption and storage
- Environment variable support
- No key logging or exposure
- Provider-specific isolation

### **Data Protection**
- Input validation and sanitization
- Secure session management
- Rate limiting and abuse prevention
- Audit logging and monitoring

### **Network Security**
- HTTPS/WSS support
- CORS configuration
- Request validation
- Error handling without data exposure

## 📊 Performance

### **Optimizations**
- Async/await architecture
- Connection pooling
- Intelligent caching
- Background processing
- Memory management

### **Monitoring**
- Real-time metrics
- Performance tracking
- Error monitoring
- Health checks
- Resource usage

## 🤝 Contributing

We welcome contributions to AthenaMist-Blended! Please see our contributing guidelines for details.

### **Development Setup**
```bash
# Clone repository
git clone <repository-url>
cd AthenaMist-Blended

# Install development dependencies
pip install -r requirements.txt

# Run tests
python3 -m pytest

# Launch in development mode
python3 run_web_interface.py --debug
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Mistral AI** for excellent language models
- **OpenAI** for GPT series models
- **Anthropic** for Claude AI
- **Google** for Gemini models
- **Cohere** for enterprise AI solutions
- **DeepSeek** for technical AI capabilities
- **US Government** for SAM database access

## 📞 Support

For support and questions:
- **Documentation**: See ARCHITECTURE.md for technical details
- **Issues**: Report bugs and feature requests on GitHub
- **Discussions**: Join community discussions
- **Email**: Contact the development team

---

**AthenaMist-Blended 2.0** - Where AI meets government data, powered by multiple providers and enhanced with modern web technology. 🌟 