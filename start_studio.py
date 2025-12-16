import subprocess
import os
import time

# Define paths
ROOT_DIR = os.getcwd()
WEBUI_DIR = os.path.join(ROOT_DIR, "open-webui", "backend")
COMFY_DIR = os.path.join(ROOT_DIR, "ComfyUI")

def run_service(command, cwd):
    return subprocess.Popen(command, cwd=cwd, shell=True)

try:
    print("--- Starting Ollama ---")
    subprocess.Popen("ollama serve", shell=True)
    time.sleep(5) # Give it time to start

    print("--- Starting ComfyUI (Video Engine) ---")
    comfy_cmd = "venv/bin/python main.py --cpu --listen 0.0.0.0 --port 8188"
    run_service(comfy_cmd, COMFY_DIR)

    print("--- Starting Open WebUI (Chat Interface) ---")
    # We use a simplified start command for Codespaces
    webui_cmd = "venv/bin/python -m uvicorn main:app --host 0.0.0.0 --port 8080"
    run_service(webui_cmd, WEBUI_DIR)

    print("\n✅ AI Studio is Running!")
    print("Check the 'PORTS' tab in your VS Code terminal to access the links.")
    
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping...")
