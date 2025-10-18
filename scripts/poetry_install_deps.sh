#!/bin/bash

# --- Find the script's own directory ---
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

REQUIREMENTS_FILE="$SCRIPT_DIR/../requirements.txt"

echo "Installing requirements from: $REQUIREMENTS_FILE"
pip install --index-url https://download.pytorch.org/whl/cu121 torch==2.4.0 torchvision==0.19.0
pip install -r "$REQUIREMENTS_FILE"
echo "Installation complete."