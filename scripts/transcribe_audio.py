import logging
import speech_recognition as sr
import os
from pydub import AudioSegment
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def transcribe_audio_chunk(recognizer, audio_chunk_path):
    try:
        with sr.AudioFile(audio_chunk_path) as source:
            audio = recognizer.record(source)
            return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        logger.error(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def transcribe_audio(audio_file, chunk_length_ms=30000):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_file(audio_file)
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

    full_transcript = ""
    for i, chunk in enumerate(chunks):
        logger.info(f"Processing chunk {i + 1}/{len(chunks)} of {audio_file}")
        chunk_path = "temp_chunk.wav"
        chunk.export(chunk_path, format="wav")
        chunk_transcript = transcribe_audio_chunk(recognizer, chunk_path)
        full_transcript += chunk_transcript + " "

    return full_transcript.strip()

if __name__ == "__main__":
    audio_folder = "../audio/"
    transcript_folder = "../transcripts/"
    os.makedirs(transcript_folder, exist_ok=True)

    audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.wav')]
    for audio in audio_files:
        logger.info(f"Transcribing {audio}")
        transcript = transcribe_audio(os.path.join(audio_folder, audio))
        transcript_file = os.path.join(transcript_folder, f"{os.path.splitext(audio)[0]}.txt")
        with open(transcript_file, "w") as f:
            f.write(transcript)
        logger.info(f"Transcription completed for {audio}")
