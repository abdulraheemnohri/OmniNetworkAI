# OmniOperator AI Suite

A unified AI control ecosystem for PCs, mobiles, network devices, CCTV, IoT, and web automation.

## 🚀 Complete Installation Guide

### Method A: Docker Deployment (Recommended - All Platforms)
Ensure Docker and Docker Compose are installed.
1. Clone the repo: `git clone https://github.com/your-repo/OmniOperator.git`
2. Run: `docker-compose up -d`
3. Access Dashboard at `http://localhost:3000`

### Method B: Non-Docker Installation (Manual)

#### 🖥️ Windows
1. Install [Python 3.11+](https://www.python.org/downloads/).
2. Install [Nmap](https://nmap.org/download.html) and [ADB Platform Tools](https://developer.android.com/tools/releases/platform-tools).
3. Open PowerShell and run:
   ```powershell
   pip install -r requirements.txt
   python main.py --version 3
   ```

#### 🐧 Linux (Ubuntu/Debian)
Run the automated script:
```bash
chmod +x scripts/setup_linux_mac.sh
./scripts/setup_linux_mac.sh
```

#### 🍎 macOS
Ensure [Homebrew](https://brew.sh/) is installed, then run:
```bash
chmod +x scripts/setup_linux_mac.sh
./scripts/setup_linux_mac.sh
```

#### 📱 Termux (Android)
Install Termux from F-Droid, then run:
```bash
pkg install wget
wget https://raw.githubusercontent.com/your-repo/OmniOperator/main/scripts/setup_termux.sh
chmod +x setup_termux.sh
./setup_termux.sh
```

## 🧠 AI API Providers Supported
OmniOperator integrates with all major AI intelligence layers:
- **Premium**: OpenAI (GPT-4o), Anthropic (Claude 3.5), Gemini 1.5 Pro.
- **Free/No-Setup**:
  - **Jules API**: Optimized developer interface.
  - **Puter.js**: Zero-setup, user-pays model.
  - **ApiFreeLLM**: Free 200B+ models.
  - **Google AI Studio**: Free Gemini API.
  - **Groq**: Ultra-fast free open-source models.
  - **Routeway.ai / Z.ai**: Free GLM model access.

## 🏗️ Project Architecture
- **version1_cloud/**: Online-Only Operator.
- **version2_offline/**: Local Operator using Ollama & Gemma 4.
- **version3_hybrid/**: Flagship Hybrid Operator.

---

**Note**: This system controls devices through legitimate interfaces (SSH, ONVIF, ADB, SNMP, APIs). No unauthorized access is performed.
