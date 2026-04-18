#!/bin/bash
echo "📱 Setting up OmniOperator for Termux..."

# Storage permission
termux-setup-storage

# Update and Install system packages
pkg update && pkg upgrade -y
pkg install -y python git nmap termux-api openssl libffi libcrypt clang make ndk-sysroot -y

# Setup Python environment
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Termux setup complete! Run 'python main.py' to start."
