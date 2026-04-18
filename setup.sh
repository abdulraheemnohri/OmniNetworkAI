#!/bin/bash

echo "🚀 Initializing OmniOperator AI Suite Setup..."

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Setup Ollama
echo "🧠 Do you want to set up local Ollama for offline mode? (y/n)"
read setup_ollama
if [ "$setup_ollama" == "y" ]; then
    bash scripts/setup_ollama.sh
fi

# Configuration check
if [ ! -f config.json ]; then
    echo "⚙️ Creating default config.json..."
    cp shared_core/config.json . 2>/dev/null || echo '{"version": 3}' > config.json
fi

echo "✅ Setup finished. Run 'python main.py' to start."
