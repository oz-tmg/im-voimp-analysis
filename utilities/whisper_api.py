import os
import subprocess
from pathlib import Path
from faster_whisper import WhisperModel

# Initialize the model once
model = WhisperModel("base")  # you can change to "small", "medium", or "large"

path_to_folder = os.getenv("PATH_TO_FOLDER")

def convert_opus_to_wav(opus_path, wav_path):
    """Convert a .opus file to .wav using ffmpeg."""
    try:
        subprocess.run([
            "ffmpeg", "-y", "-i", str(opus_path),
            "-ar", "16000", "-ac", "1",  # 16kHz mono audio
            str(wav_path)
        ], check=True)
        print(f"Converted {opus_path} → {wav_path}")
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg failed on {opus_path}: {e}")

def transcribe_audio(wav_path):
    """Transcribe a .wav file using faster-whisper."""
    print(f"Transcribing: {wav_path}")
    segments, info = model.transcribe(str(wav_path))

    transcription = ""
    for segment in segments:
        transcription += f"[{segment.start:.2f} - {segment.end:.2f}] {segment.text}\n"
    
    return transcription

def process_audio_files(folder_path):
    """Process all .opus and .wav files in a folder."""
    folder = Path(folder_path)
    for file in folder.iterdir():
        if file.suffix == ".opus":
            wav_file = file.with_suffix(".wav")
            convert_opus_to_wav(file, wav_file)
            transcription = transcribe_audio(wav_file)
            txt_file = file.with_suffix(".txt")
        elif file.suffix == ".wav":
            transcription = transcribe_audio(file)
            txt_file = file.with_suffix(".txt")
        else:
            continue  # skip non-audio files

        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(transcription)
        print(f"📝 Saved transcription: {txt_file.name}\n")


# 📂 Set this to your folder with .opus files
process_audio_files(path_to_folder)
