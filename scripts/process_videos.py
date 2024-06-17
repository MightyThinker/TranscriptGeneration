import logging
import os
import subprocess
import sys
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def run_script(script_name):
    try:
        # Ensure to use the same Python interpreter that runs this script
        result = subprocess.run([sys.executable, script_name], cwd="./scripts", check=True)
        logger.info(f"Successfully ran {script_name}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error running {script_name}: {e}")

if __name__ == "__main__":
    run_script("extract_audio.py")
    run_script("transcribe_audio.py")
    run_script("summarize_text.py")
