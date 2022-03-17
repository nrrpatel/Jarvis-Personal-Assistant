
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import sys
#import wolframalpha (upcoming feature)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#url =  'https://www.youtube.com/channel/UC6OUOw2jBeP4GwSRm8gshVQ'

 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak ("Jay Shree Krishna!")

    elif hour > 12 and hour < 18:
        speak ("Good Afternoon!")

    else:
        speak ("Good Evening!")

    speak("Jarvis here. What can I do for you today sir")

def takeCommand():
    # it takes microphone input from the user and returns a string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)  


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-ca')
        print(f"User said: {query}/n")

    # this is if audio doesn't work.    
    except Exception as e:
       # print(e)

        print("I couldn't catch that. Could you please repeat it?")
        speak("I couldn't catch that. Could you please repeat it?")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    
    #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak (results)

        elif 'open youtube' in query:
            webbrowser.open("chrome", "youtube.com")

        elif 'open vibes nation' in query:
            speak(" Opening Vibes Nation ")
            webbrowser.open("https://www.youtube.com/channel/UC6OUOw2jBeP4GwSRm8gshVQ")

        elif 'open learn' in query:
            webbrowser.open("https://learn.uwaterloo.ca/d2l/home")

        elif 'open waterlooworks' in query:
            webbrowser.open("https://waterlooworks.uwaterloo.ca/myAccount/dashboard.htm")

        elif 'chill time' in query:
            webbrowser.open("https://www.netflix.com/browse")

        elif 'play my music' in query:
            speak(" Playing your music on amazon music ")
            webbrowser.open("https://music.amazon.ca/my/playlists/804ce7ec-8858-406a-a497-f2782f166e94")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Sir, currently the time is {strTime}")
    
        elif 'open sea lion ' in query:
            codePath = "C:\\Program Files\\JetBrains\\CLion 2021.3.2\\bin\\clion64.exe"
            os.startfile(codePath)
        
        elif 'open word' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)

        elif 'open outlook' in query:
            webbrowser.open("https://outlook.office.com/mail/inbox/id/AAQkADY3YzYwZTI3LTFkNmItNDEyNy04ZjMzLWMxNGY3MDI5NDhkNgAQAFWzcKL5dWVFv6NOBJ8j0R4%3D")

        elif 'that is all jarvis' in query:
            sys.exit()
 