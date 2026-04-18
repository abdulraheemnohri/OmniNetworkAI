# OmniOperator AI Suite

A unified AI control ecosystem for PCs, mobiles, network devices, CCTV, IoT, and web automation.

## 🚀 Installation & Setup

### 1. Automated Setup (Recommended)
```bash
chmod +x setup.sh
./setup.sh
```

### 2. Docker Deployment (Full Stack)
```bash
docker-compose up -d
```
This starts the Operator API, the Dashboard, and a local Ollama instance.

### 3. Offline AI & Ollama Setup
To use Version 2 (Offline-Only), you need a local Ollama server.
1. Run `bash scripts/setup_ollama.sh` to install Ollama and download the **Gemma 4** model:
   - [Gemma 4 GGUF Model](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF/resolve/main/gemma-4-E2B-it-Q4_K_M.gguf?download=true)
2. Ensure Ollama is running: `ollama serve`

## 🧠 AI API Providers Supported
OmniOperator integrates with all major AI intelligence layers:
- **OpenAI / Gemini / Claude**: Flagship intelligence.
- **Groq**: Ultra-fast inference.
- **Mistral / Cohere / Perplexity**: Specialized tasks and web search.

## 🏗️ Project Architecture
- **version1_cloud/**: Online-Only Operator.
- **version2_offline/**: Local Operator using Ollama & Gemma 4.
- **version3_hybrid/**: Flagship Hybrid Operator.

## 🛠️ Configuration
Manage your tokens and device IPs in `config.json`.

---

**Note**: This system controls devices through legitimate interfaces (SSH, ONVIF, ADB, SNMP, APIs). No unauthorized access is performed.
