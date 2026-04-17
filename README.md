# OmniNetwork AI Operator (ONAIO)

A unified AI-powered network and device control system for managing PCs, mobiles, routers, CCTV, IoT devices, and cloud services via Telegram, WhatsApp, Web Dashboard, and CLI.

## Features

- **Hybrid AI Architecture**: Offline (Qwen2.5-1.5B/Mistral 7B) + Online (OpenAI/Gemini/Claude/Groq/OpenRouter)
- **Device Control**: PCs, mobiles, routers, switches, CCTV, IoT, web services
- **Interfaces**: Telegram Bot, WhatsApp Bridge, Web Dashboard (Next.js), CLI
- **Security**: User authentication, device whitelist, risk scoring
- **Advanced Features**: Autonomous network fixing, AI network admin mode, multi-device orchestration

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Project Structure

```
OmniNetworkAI/
├── brain/
│   ├── offline_model.py
│   ├── online_router.py
│   ├── intent_engine.py
├── control/
│   ├── computer/
│   ├── mobile/
│   ├── router/
│   ├── switch/
│   ├── cctv/
│   ├── iot/
├── network/
│   ├── network_scanner.py
│   ├── device_discovery.py
├── automation/
│   ├── task_engine.py
│   ├── scheduler.py
├── security/
│   ├── auth.py
│   ├── device_whitelist.py
│   ├── encryption.py
├── comms/
│   ├── telegram_bot.py
│   ├── whatsapp_bridge.py
│   ├── api_server.py
├── dashboard/
│   ├── nextjs_frontend/
├── main.py
├── requirements.txt
└── README.md
```

---

**Note**: This system controls devices through legitimate interfaces (SSH, ONVIF, ADB, SNMP, APIs). No unauthorized access is performed.