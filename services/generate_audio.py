#!/usr/bin/env -S uv run --script

# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "pyttsx3",
#     "moviepy",
# ]
# ///

"""
Generate higher-quality TTS narration using pyttsx3 and export as a high-bitrate MP3.

What’s improved vs previous version:
- Picks a better system voice by name if available (e.g., Samantha/Alex on macOS; Aria/Zira/Guy on Windows).
- Uses a more natural speaking rate (~170 wpm) and full volume.
- Saves to WAV (lossless) first, then encodes to 192 kbps MP3 at 44.1 kHz via MoviePy/ffmpeg.

Tips to further improve quality:
- macOS: System Settings → Accessibility → Spoken Content → System Voice → Manage Voices…
  Download high-quality voices (e.g., "Samantha (Enhanced)", "Alex").
- Windows: Install Microsoft Neural voices (if available) or select Aria/Zira/Guy.
- Linux: Install espeak-ng or mbrola voices; consider using an online TTS for best naturalness.
"""

from pathlib import Path
import sys
import pyttsx3
from moviepy import AudioFileClip

AUDIO_DIR = Path(__file__).parent / "audio"
AUDIO_DIR.mkdir(exist_ok=True)

# You can edit this narration text or pass it as CLI args.
DEFAULT_TEXT = (
    "Minimalist illustration of a developer sitting in front of a laptop with the glowing "
    "Next dot JS logo on the screen. Dark theme, modern flat design."
)

# Preferred voice names to try across platforms (case-insensitive substring match)
PREFERRED_VOICES = [
    # macOS voices
    "Samantha", "Alex", "Ava", "Victoria", "Karen", "Moira", "Tessa",
    # Windows voices
    "Aria", "Zira", "Guy", "Jenny", "Davis", "Steffan",
]


def pick_best_voice(engine: pyttsx3.Engine) -> str | None:
    voices = engine.getProperty("voices") or []
    # Try to find a preferred voice by name
    for pref in PREFERRED_VOICES:
        for v in voices:
            name = getattr(v, "name", "") or ""
            if pref.lower() in name.lower():
                return v.id
    # Fallback: return the current default voice id if present
    try:
        return voices[0].id if voices else None
    except Exception:
        return None


def synthesize_to_wav(text: str, wav_path: Path, rate: int = 170, volume: float = 1.0) -> None:
    engine = pyttsx3.init()

    # Configure speaking rate (words per minute) and volume (0.0 - 1.0)
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)

    # Choose a better voice if available
    voice_id = pick_best_voice(engine)
    if voice_id:
        engine.setProperty("voice", voice_id)

    # Save to WAV first (pyttsx3 drivers produce best results with WAV/AIFF)
    wav_path.parent.mkdir(parents=True, exist_ok=True)
    engine.save_to_file(text, str(wav_path))
    engine.runAndWait()
    engine.stop()


def convert_wav_to_mp3(wav_path: Path, mp3_path: Path, bitrate: str = "192k", fps: int = 44100) -> None:
    # Use MoviePy/ffmpeg to convert with controlled sample rate/bitrate
    with AudioFileClip(str(wav_path)) as audio:
        audio.write_audiofile(
            str(mp3_path),
            fps=fps,
            bitrate=bitrate,
            codec="libmp3lame",
        )


def main():
    # Accept text from CLI argument or fallback to DEFAULT_TEXT
    text = " ".join(sys.argv[1:]).strip() or DEFAULT_TEXT

    tmp_wav = AUDIO_DIR / "narration_tmp.wav"
    out_mp3 = AUDIO_DIR / "narration.mp3"

    print("Synthesizing speech…")
    synthesize_to_wav(text, tmp_wav, rate=170, volume=1.0)

    print("Encoding MP3 (192 kbps @ 44.1 kHz)…")
    convert_wav_to_mp3(tmp_wav, out_mp3, bitrate="192k", fps=44100)

    # Optionally keep an AAC/M4A too (uncomment if you prefer AAC for Shorts)
    # out_m4a = AUDIO_DIR / "narration.m4a"
    # with AudioFileClip(str(tmp_wav)) as audio:
    #     audio.write_audiofile(str(out_m4a), fps=44100, bitrate="192k", codec="aac")

    # Clean-up temp WAV if desired
    try:
        tmp_wav.unlink()
    except Exception:
        pass

    print(f"Done. High-quality narration saved to: {out_mp3}")
    print("Tip: Use this path in text_narration.py's audio_file parameter.")


if __name__ == "__main__":
    main()