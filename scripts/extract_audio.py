import logging
from pydub import AudioSegment
import os
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def extract_audio(video_file, audio_file):
    if os.path.exists(audio_file):
        logger.info(f"Audio file {audio_file} already exists. Skipping extraction.")
        return
    try:
        video = AudioSegment.from_file(video_file)
        video.export(audio_file, format="wav")
        logger.info(f"Extracted audio from {video_file} to {audio_file}")
    except Exception as e:
        logger.error(f"Failed to extract audio from {video_file}: {e}")

if __name__ == "__main__":
    video_folder = "../videos/"
    audio_folder = "../audio/"
    os.makedirs(audio_folder, exist_ok=True)

    video_files = [f for f in os.listdir(video_folder) if f.endswith('.mp4')]
    for video in video_files:
        audio_file = os.path.join(audio_folder, f"{os.path.splitext(video)[0]}.wav")
        extract_audio(os.path.join(video_folder, video), audio_file)
