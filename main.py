import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)


def speak (audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Hey! I am Jarvis, Disha. Please tell me how may i help you")



def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said; {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "Home"
    return query



def get_random_advice():
    res = requests.get("https;//api.adviceslip.com/advice").json()
    return res['slip']['advice']


if __name__== "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        



        if 'wikipedia' in query:
            speak('Search Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'Who created you' in query:
            speak("Disha created me by using python")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma'am, the time is {strTime}")

        elif 'How are you' in query:
            speak("I am good, what about you")

        elif 'logout' in query:
            speak("Thank you!")
            exit()
