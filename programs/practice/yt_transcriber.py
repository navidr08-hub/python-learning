# Chapter 24 - Text-to-Speech and Speech Recognition
# (Practice Program) - Youtube Transcriber
# Windows 10 ONLY

"""
Write a program that glues together the features of yt-dlp and
Whisper to automatically download YouTube videos and produce 
subtitle files in the .srt format. The input can be a list of URLs
to download and transcribe. You can also add options to produce different 
subtitle formats. Python is an excellent “glue language” for combining 
the capabilities of different modules.
"""

import os
import whisper
from whisper.utils import WriteVTT, WriteSRT
from yt_dlp import YoutubeDL
from pathlib import Path


URLS = [
    "https://www.youtube.com/shorts/g9fIWtSexLs",
    "https://www.youtube.com/shorts/Q-wtD36ur2s",
    "https://www.youtube.com/shorts/b-bTjOLmwcc"
]

OUTPUT_DIR = "C:\\Users\\navid\\Documents\\programs\\output"

def download_audio(url: str, output_dir: Path) -> Path:
    """Downloads the audio track from a YouTube video using yt-dlp."""
    # output_template = os.path.join(output_dir, "%(title)s.%(ext)s")
    output_template = str(output_dir / "%(title)s.%(ext)s")
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "quiet": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        base = os.path.splitext(filename)[0]
        audio_path = f"{base}.mp3"
        print(f"Downloaded: {audio_path}")
        return Path(audio_path)
    

def write_srt(result, fp: str):
    """Save as transcribed audio .srt file"""
    def format_srt_timestamp(seconds: float) -> str:
        """Convert seconds to SRT timestamp (hh:mm:ss,mmm)."""
        milliseconds = int((seconds - int(seconds)) * 1000)
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hours:02}:{minutes:02}:{secs:02},{milliseconds:03}"

    with open(fp, "w", encoding="utf-8") as f:
        for i, seg in enumerate(result["segments"], start=1):
            start = format_srt_timestamp(seg["start"])
            end = format_srt_timestamp(seg["end"])
            text = seg["text"].strip()
            f.write(f"{i}\n{start} --> {end}\n{text}\n\n")

    print("✅ Saved transcript (.srt)")


def write_vtt(result, fp: str):
    """Save as transcribed audio .vtt file"""
    with open(fp, "w", encoding="utf-8") as f:
        f.write("WEBVTT\n\n")
        for i, segment in enumerate(result["segments"], start=1):
            start = whisper.utils.format_timestamp(segment["start"])
            end = whisper.utils.format_timestamp(segment["end"])
            text = segment["text"].strip()
            f.write(f"{i}\n{start} --> {end}\n{text}\n\n")

    print("✅ Saved transcript (.vtt)")


def write_txt(result, fp: str):
    with open(fp, "w", encoding="utf-8") as f:
        for seg in result["segments"]:
            f.write(seg["text"].strip() + "\n")
    
    print("✅ Saved transcript (.txt)")


def transcribe(audio_path: Path, model_name="base", output_format="srt"):
    """Transcribes the given audio file using Whisper."""
    print(f"Transcribing {audio_path.name} ...")

    model = whisper.load_model(model_name)
    base = audio_path.with_suffix("")
    result = model.transcribe(str(audio_path), verbose=False)

    # Save to desired subtitle format
    if output_format == "srt":
        output_fp = base.with_suffix(".srt")
        write_srt(result, output_fp)
    elif output_format == "vtt":
        output_fp = base.with_suffix(".vtt")
        write_vtt(result, output_fp)
    elif output_format == "txt":
        output_fp = base.with_suffix(".txt")
        write_txt(result, output_fp)
    else:
        raise ValueError("Invalid output format. Choose from: srt, vtt, txt")

    return output_fp


def main():
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(exist_ok=True)
    for url in URLS:
        audio_fp = download_audio(url=url, output_dir=output_dir)
        transcribe(audio_fp)


if __name__ == "__main__":
    main()