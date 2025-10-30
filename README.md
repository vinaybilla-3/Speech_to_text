# Speech_to_text
from fastapi import FastAPI
import speech_recognition as sr

app = FastAPI(title="Speech to Text API")

@app.get("/")
def home():
    return {"message": "Welcome to the Speech to Text FastAPI service!"}

@app.post("/speech-to-text/")
def speech_to_text(duration: int = 10):
    """
    Record audio from the microphone for a given duration (in seconds)
    and convert it to text using Google Speech Recognition.
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(f" Recording for {duration} seconds...")
        r.adjust_for_ambient_noise(source, duration=0.5)   #adopt background noice
        audio = r.record(source, duration=duration)  #  Record fixed duration

    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return {"duration": duration, "transcription": text}
    except sr.UnknownValueError:
        return {"error": "Could not understand audio"}
    except sr.RequestError as e:
        return {"error": f"Could not request results from Google Speech Recognition service; {e}"}
