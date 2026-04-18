#!/bin/bash
REPO_URL="https://github.com/abdulraheemnohri/OmniNetworkAI.git"
echo "🚢 OmniOperator AI Suite: Deployment Initiated"
if [ ! -f config.json ]; then
    echo "⚙️ Initializing config.json..."
    cp shared_core/config.json . 2>/dev/null || echo '{"version": 3}' > config.json
fi
echo "🚀 Launching containers..."
docker-compose up -d --build
echo "✅ Deployment Successful!"
echo "Dashboard: http://localhost:3000"
echo "API Server: http://localhost:8000"
