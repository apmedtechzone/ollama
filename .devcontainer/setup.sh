#!/bin/bash

echo "--- Installing Ollama ---"
curl -fsSL https://ollama.com/install.sh | sh

echo "--- Setting up Open WebUI ---"
if [ ! -d "open-webui" ]; then
    git clone https://github.com/open-webui/open-webui.git
fi
cd open-webui
# Install Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
cd ../..

echo "--- Setting up ComfyUI ---"
if [ ! -d "ComfyUI" ]; then
    git clone https://github.com/comfyanonymous/ComfyUI.git
fi
cd ComfyUI
python -m venv venv
source venv/bin/activate
# INSTALL CPU VERSION OF TORCH (Required for free Codespaces)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
deactivate
cd ..

echo "--- Setup Complete! Run 'python start_studio.py' to launch. ---"
