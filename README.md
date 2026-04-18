# OmniOperator AI Suite

A unified AI control ecosystem for PCs, mobiles, network devices, CCTV, IoT, and web automation.

## 🚀 Installation Methods

### 1. Local Installation (Recommended for Development)
Ensure you have Python 3.10+ installed.

```bash
# Clone the repository
git clone https://github.com/your-repo/OmniOperator.git
cd OmniOperator

# Install dependencies
pip install -r requirements.txt

# Configure the system
# Edit config.json with your API keys and device credentials

# Run the flagship Hybrid version
python main.py --version 3
```

### 2. Docker Deployment (Recommended for Production)
Ensure Docker and Docker Compose are installed.

```bash
# Build the Docker image
docker build -t omnioperator .

# Run the container
docker run -d \
  -p 8000:8000 \
  --name onaio \
  -e TELEGRAM_BOT_TOKEN="your_token" \
  omnioperator
```

### 3. Agent-Specific Setup
- **Mobile (Android)**: Enable 'USB Debugging' and 'Install via ADB' on your device.
- **Network (Switch)**: Enable SNMP v2c/v3 on your managed switches.
- **CCTV**: Ensure ONVIF is enabled on your IP cameras.

## 🧠 AI API Providers Supported
OmniOperator integrates with all major AI intelligence layers:
- **OpenAI**: GPT-4o, GPT-3.5-Turbo
- **Google Gemini**: Gemini 1.5 Pro/Flash
- **Anthropic**: Claude 3.5 Sonnet/Opus
- **Groq**: Llama 3 70B (Fast Inference)
- **OpenRouter**: Unified access to 100+ models
- **Perplexity**: Real-time web-enhanced AI
- **Mistral AI**: Mixtral, Mistral Large
- **Cohere**: Command R+

## 🏗️ Project Architecture
- **version1_cloud/**: Online-Only AI Operator.
- **version2_offline/**: Fully Offline Local AI Operator.
- **version3_hybrid/**: Flagship Hybrid AI Operator (Offline speed + Online intelligence).
- **agents/**: Specialized control layers (PC, Mobile, Network, CCTV, IoT, Web).
- **shared_core/**: Central intelligence, security, and automation modules.

## 🛠️ Configuration
All settings are managed via `config.json`. You can specify your AI API keys, device IPs, and security tokens there.

---

**Note**: This system controls devices through legitimate interfaces (SSH, ONVIF, ADB, SNMP, APIs). No unauthorized access is performed.
