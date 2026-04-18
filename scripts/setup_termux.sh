#!/bin/bash
echo "📱 Setting up OmniOperator for Termux..."
pkg update && pkg upgrade -y
pkg install -y python ndk-sysroot clang make libjpeg-turbo libffi libcrypt openssl nmap termux-api
pip install --upgrade pip
pip install -r requirements.txt
echo "✅ Termux setup complete! Run 'python main.py' to start."
