#!/bin/bash
echo "🚀 Setting up local Ollama server..."
if ! command -v ollama &> /dev/null; then
    echo "Ollama not found. Please install it from https://ollama.com/"
else
    echo "Ollama is already installed."
fi
MODEL_URL="https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF/resolve/main/gemma-4-E2B-it-Q4_K_M.gguf?download=true"
MODEL_FILE="gemma-4-E2B.gguf"
echo "📥 Downloading Gemma 4 GGUF model..."
curl -L "$MODEL_URL" -o "$MODEL_FILE"
echo "🛠️ Creating Ollama model 'gemma4'..."
cat <<MODELFEOF > Modelfile
FROM ./"$MODEL_FILE"
PARAMETER temperature 0.7
SYSTEM "You are OmniOperator AI, an offline network and device control assistant."
MODELFEOF
ollama create gemma4 -f Modelfile
rm Modelfile
echo "✅ Ollama setup complete! Local model 'gemma4' is ready."
