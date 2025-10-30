from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

# Recording settings
duration = 10  # seconds
sample_rate = 16000

print("Speak something in English...")

# Record audio from microphone
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
sd.wait()

audio = audio.flatten()
# Load Whisper model
model = WhisperModel("small")  # you can use "medium" for better accuracy

# Transcribe and translate to Hindi
segments, info = model.transcribe(audio, language="en", task="translate")

print("\nSpeech to Text:\n")
for segment in segments:
    print(segment.text)
