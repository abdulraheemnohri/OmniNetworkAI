# OmniOperator AI Suite

A unified AI control ecosystem for PCs, mobiles, network devices, CCTV, IoT, and web automation.

## Project Structure

- **version1_cloud/**: Cloud AI Operator (Online-Only).
- **version2_offline/**: Offline AI Operator (Local-Only).
- **version3_hybrid/**: Hybrid AI Operator (Flagship - Offline speed + Online intelligence).
- **shared_core/**: Core logic including automation, command parsing, security, memory, and networking.
- **agents/**: Specialized controllers for PC, Mobile (ADB/iOS), Network (SSH/SNMP), CCTV (ONVIF/RTSP), IoT (MQTT/Home Assistant), and Web (Playwright).
- **ai_brain/**: Local and cloud AI models and routing logic.
- **comms/**: Telegram Bot, WhatsApp Bridge, and FastAPI server.
- **dashboard/**: Futuristic Next.js UI for system monitoring and control.

## Installation

```bash
pip install -r requirements.txt
```

## Features

- **Hybrid Brain**: Dual AI switching between local (Qwen) and cloud (GPT/Gemini/Claude) models.
- **Memory System**: Vector DB memory for learning and context awareness.
- **Autonomous Logic**: Self-healing network and multi-device orchestration.
- **Advanced Control**: Full OS automation, mobile ADB control, SNMP network diagnostics, and ONVIF CCTV management.
- **Security**: JWT-based authentication, risk scoring, and device whitelisting.

## Usage

```bash
# Run the hybrid version
python main.py --version 3

# Execute a single command
python main.py --version 3 --command "Scan the network"
```

---

**Note**: This system controls devices through legitimate interfaces (SSH, ONVIF, ADB, SNMP, APIs). No unauthorized access is performed.
