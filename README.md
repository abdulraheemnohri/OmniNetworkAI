# OmniOperator AI Suite (ONAIO)

A unified AI control ecosystem for PCs, mobiles, network devices, CCTV, IoT, and web automation.

**Repository URL**: [https://github.com/abdulraheemnohri/OmniNetworkAI.git](https://github.com/abdulraheemnohri/OmniNetworkAI.git)

## 🚀 Complete Installation Guide

### Method A: Docker Deployment (Recommended)
Deployment via Docker ensures that all dependencies (Nmap, ADB, Python environment) are perfectly configured.

#### 🛠️ Docker Deep Dive
- **Network Mode**: The system uses `bridge` mode by default, but for full network scanning, `host` mode is recommended on Linux.
- **Volumes**:
  - `ollama_data`: Persists your local AI models.
  - `./config.json`: Mounted to keep your API keys and settings synchronized.
- **Health Checks**: Containers are configured to restart automatically if they fail.

#### 🏃 Quick Start with Docker
```bash
# 1. Clone the repository
git clone https://github.com/abdulraheemnohri/OmniNetworkAI.git
cd OmniNetworkAI

# 2. Run the suite
docker-compose up -d

# 3. Access
# Dashboard: http://localhost:3000
# API: http://localhost:8000
```

---

### Method B: Non-Docker Installation (Manual)

#### 🖥️ Windows
1. Install [Python 3.11+](https://www.python.org/downloads/).
2. Install [Nmap](https://nmap.org/download.html) and [ADB Platform Tools](https://developer.android.com/tools/releases/platform-tools).
3. Run:
   ```powershell
   pip install -r requirements.txt
   python main.py --version 3
   ```

#### 🐧 Linux (Ubuntu/Debian) / 🍎 macOS
```bash
chmod +x scripts/setup_linux_mac.sh
./scripts/setup_linux_mac.sh
```

#### 📱 Termux (Android)
```bash
pkg install wget
wget https://raw.githubusercontent.com/abdulraheemnohri/OmniNetworkAI/main/scripts/setup_termux.sh
chmod +x setup_termux.sh
./setup_termux.sh
```

## 🧠 AI API Providers Supported
OmniOperator integrates with 10+ AI intelligence layers, including **Jules API**, **Puter.js**, **Google AI Studio**, **Groq**, and **OpenRouter**.

## 🏗️ Project Architecture
- **version3_hybrid/**: Flagship Hybrid Operator (Default).
- **agents/**: PC, Mobile, Network, CCTV, IoT, and Web agents.
- **dashboard/**: Futuristic Next.js UI following the 'Digital Bastion' design.

---

**Note**: This system controls devices through legitimate interfaces (SSH, ONVIF, ADB, SNMP, APIs). No unauthorized access is performed.
