#!/bin/bash
echo "🚀 Setting up OmniOperator for Linux/macOS..."
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt-get update
    sudo apt-get install -y python3-pip nmap adb libgl1-mesa-glx libglib2.0-0
elif [[ "$OSTYPE" == "darwin"* ]]; then
    brew install nmap android-platform-tools
fi
pip3 install -r requirements.txt
echo "✅ Setup complete! Run 'python3 main.py' to start."
