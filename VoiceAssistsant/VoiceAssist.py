import pyttsx3
import speech_recognition as sr
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            command = r.recognize_google(audio)
            print(f"You said: {command}\n")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
        except sr.WaitTimeoutError:
            speak("Listening timed out. Try again.")
    return ""
def process_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye! Have a nice day.")
        return False 
    else:
        speak("I'm still learning. Please try a different command.")
    return True


speak("Hi Mr. Bharath! I am your voice assistant.")
while True:
    user_input = listen()
    if user_input:
        should_continue = process_command(user_input)
        if not should_continue:
            break
