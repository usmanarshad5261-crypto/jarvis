import speech_recognition as sr
import pyttsx3
import webbrowser
music_library = {
    "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA"
}


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def process_command(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("ht tps://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        parts = c.split(" ", 1)
        if len(parts) > 1:
            song = parts[1]
            if song in music_library:
                webbrowser.open(music_library[song])
            else:
                speak(f"Sorry, I don't have {song} in my library.")
        else:
            speak("Please tell me the song name after 'play'.")
    else:
        pass


if __name__ == "__main__":
    speak("Initializing Jarvis")
    r = sr.Recognizer()
    while True:
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=5)

            command = r.recognize_google(audio)
            print("You said:", command)
            speak(command)
            process_command(command)

        except sr.WaitTimeoutError:
            print("No speech detected in the given time.")

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")

        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")
