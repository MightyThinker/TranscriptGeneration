import logging
from transformers import pipeline
import os
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def summarize_text(text, max_length=130, min_length=30):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
    return summary

def chunk_text(text, chunk_size=1000):
    for i in range(0, len(text), chunk_size):
        yield text[i:i+chunk_size]

def summarize_long_text(text, chunk_size=1000):
    chunks = list(chunk_text(text, chunk_size))
    summaries = []
    for i, chunk in enumerate(chunks):
        logger.info(f"Summarizing chunk {i + 1}/{len(chunks)}")
        summary = summarize_text(chunk)
        summaries.append(summary)
    return " ".join(summaries)

if __name__ == "__main__":
    transcript_folder = "../transcripts/"
    summary_folder = "../summaries/"
    os.makedirs(summary_folder, exist_ok=True)

    transcript_files = [f for f in os.listdir(transcript_folder) if f.endswith('.txt')]
    for transcript_file in transcript_files:
        summary_file = os.path.join(summary_folder, f"{os.path.splitext(transcript_file)[0]}_summary.txt")
        if os.path.exists(summary_file):
            logger.info(f"Summary file {summary_file} already exists. Skipping summarization.")
            continue
        logger.info(f"Summarizing {transcript_file}")
        with open(os.path.join(transcript_folder, transcript_file), "r") as f:
            transcript = f.read()

        summary = summarize_long_text(transcript)

        with open(summary_file, "w") as f:
            f.write(summary)
        logger.info(f"Summary completed for {transcript_file}")
