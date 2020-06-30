import pyttsx3
import speech_recognition as sr
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate=engine.getProperty('rate')
volume=engine.getProperty('volume')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',160)
engine.setProperty('volume',1)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hey" + "I am Julia Here.")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        if 'Julia' in query:
            speak("Yes!!I am here")
        if 'cat and dog' in query:
            speak("Yes,I am very well know now!Moreover,I can now easily recognize cat and dog")
            from gui import graphical_part
            graphical_part()






