import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Use the microphone as source for input
with sr.Microphone() as source:
    print("Say something!")
    # Adjust for ambient noise to improve accuracy
    r.adjust_for_ambient_noise(source, duration=0.10)
    # Listen for the user's input
    audio = r.listen(source)

    try:
        # Using Google Speech Recognition to recognize audio
        text = r.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
