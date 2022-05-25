from json.tool import main
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import sys
import wolframalpha
import json
import requests
import random
import pywhatkit as pwk
from lsHotword import ls


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
# chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# webbrowser.register()

# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
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
        ls.lsHotword_loop()
        query = takeCommand().lower()
    
    #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak (results)
        
        #this is for opening youtube
        # elif 'open youtube' in query:
        #     speak("Opening youtube")
        #     webbrowser.open("https://www.youtube.com/")


        #this is for opening the best youtube channel 
        elif 'open vibes nation' in query:
            speak(" Opening Vibes Nation ")
            webbrowser.open("https://www.youtube.com/channel/UC6OUOw2jBeP4GwSRm8gshVQ")

        #this is for opening learn
        elif 'open learn' in query:
            speak("opening learn")
            webbrowser.open("https://learn.uwaterloo.ca/d2l/home")
        
        elif 'show me the news' in query:
            speak("opening national post")
            webbrowser.open("https://nationalpost.com/")

        #this is for waterloo works
        elif 'open waterlooworks' in query:
            speak("opening waterlooworks")
            webbrowser.open("https://waterlooworks.uwaterloo.ca/myAccount/dashboard.htm")

        elif 'help me find a job' in query:
            speak("opening waterlooworks")
            webbrowser.open("https://waterlooworks.uwaterloo.ca/myAccount/dashboard.htm")


        #this is for netflix
        elif 'chill time' in query:
            webbrowser.open("https://www.netflix.com/browse")

        elif 'netflix' in query:
            speak("opening netflix")
            webbrowser.open("https://www.netflix.com/browse")


        
        #this is for playing music
        elif 'play my music' in query:
            speak(" Playing your music on amazon music ")
            webbrowser.open("https://music.amazon.ca/my/playlists/804ce7ec-8858-406a-a497-f2782f166e94")
        
        #this is for the time 
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Sir, currently the time is {strTime}")
    
        #his is for openeing clion
        elif 'open sea lion ' in query:
            codePath = "C:\\Program Files\\JetBrains\\CLion 2021.3.2\\bin\\clion64.exe"
            os.startfile(codePath)
        
        #this is for opening word
        elif 'open word' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)

        #this is for opening outlook
        elif 'open outlook' in query:
            webbrowser.open("https://outlook.office.com/mail/inbox/id/AAQkADY3YzYwZTI3LTFkNmItNDEyNy04ZjMzLWMxNGY3MDI5NDhkNgAQAFWzcKL5dWVFv6NOBJ8j0R4%3D")

        #this is for python coding practices
        elif 'practice time' in query:
            webbrowser.open("https://www.sololearn.com/learning/1172")
        
 
        #this is to watch anime
        elif 'anime time' in query:
            speak(" Understood sir, it's anime time ")
            webbrowser.open("https://ww7.attacktitanepisode.com/attack-on-titan-season-4-episode-15-english-dubbed-watch-online/")

        # this is to search anything on google
        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open ("https://www.google.com/search?q="+query+"&rlz=1C1ONGR_enCA973CA973&oq="+query+"&aqs=chrome..69i57j46i67i433j0i131i433i512j0i131i433i457i512j0i67i433j0i3j0i433i512l2j0i512l2.4828j0j7&sourceid=chrome&ie=UTF-8")
            speak("searching" + query+ "on google")

        elif 'youtube' in query:
            video = query
            speak(f"Okay sir, playing {video} on youtube")
            pwk.playonyt(video)
            # query = query.replace("youtube", "")
            # webbrowser.open ("https://www.google.com/search?q="+query+"&rlz=1C1ONGR_enCA973CA973&oq="+query+"&aqs=chrome..69i57j46i67i433j0i131i433i512j0i131i433i457i512j0i67i433j0i3j0i433i512l2j0i512l2.4828j0j7&sourceid=chrome&ie=UTF-8")
            # speak("searching" + query+ "on google")
            

        #This is for geographical and computationa questions
        elif 'capital' in query:
            question = query
            app_id = "K88UKY-EPY4U9L98V"
            client = wolframalpha.Client('K88UKY-EPY4U9L98V')
            response = client.query(question)
            answer = next(response.results).text
            speak(answer)
            print(answer)
        
        elif 'current weather' in query:
            question = query
            app_id = "K88UKY-EPY4U9L98V"
            client = wolframalpha.Client('K88UKY-EPY4U9L98V')
            response = client.query(question)
            answer = next(response.results).text
            speak(answer)
            print(answer)
     
        elif "flip" in query:
            moves = ["heads", "tails"]
            cmove=random.choice(moves)
            speak("Sir I choose " + cmove)
        
        elif '1' in query:
            question = query 
            app_id = "K88UKY-EPY4U9L98V"
            client = wolframalpha.Client('K88UKY-EPY4U9L98V')
            response = client.query(question)
            answer = next(response.results).text
            speak(answer)
            print(answer)
        
        elif '' in query:
            question = query 
            app_id = "K88UKY-EPY4U9L98V"
            client = wolframalpha.Client('K88UKY-EPY4U9L98V')
            response = client.query(question)
            answer = next(response.results).text
            speak(answer)
            print(answer)
       
        elif '2' in query:
            question = query 
            app_id = "K88UKY-EPY4U9L98V"
            client = wolframalpha.Client('K88UKY-EPY4U9L98V')
            response = client.query(question)
            answer = next(response.results).text
            speak(answer)
            print(answer)
            # break use this for making it stop after a command
        
        elif '3' in query:
            question = query 
            app_id = "K88UKY-EPY4U9L98V"
            client = wolframalpha.Client('K88UKY-EPY4U9L98V')
            response = client.query(question)
            answer = next(response.results).text
            speak(answer)
            print(answer)
            # break use this for making it stop after a command
        elif '4' in query:
            question = query 
            app_id = "K88UKY-EPY4U9L98V"
            client = wolframalpha.Client('K88UKY-EPY4U9L98V')
            response = client.query(question)
            answer = next(response.results).text
            speak(answer)
            print(answer)
            # break use this for making it stop after a command
        elif '5' in query:
            question = query 
            app_id = "K88UKY-EPY4U9L98V"
            client = wolframalpha.Client('K88UKY-EPY4U9L98V')
            response = client.query(question)
            answer = next(response.results).text
            speak(answer)
            print(answer)
            # break use this for making it stop after a command
        elif '6' in query:
            question = query 
            app_id = "K88UKY-EPY4U9L98V"
            client = wolframalpha.Client('K88UKY-EPY4U9L98V')
            response = client.query(question)
            answer = next(response.results).text
            speak(answer)
            print(answer)
            # break use this for making it stop after a command
        elif '7' in query:
            question = query 
            app_id = "K88UKY-EPY4U9L98V"
            client = wolframalpha.Client('K88UKY-EPY4U9L98V')
            response = client.query(question)
            answer = next(response.results).text
            speak(answer)
            print(answer)
            # break use this for making it stop after a command
        elif '8' in query:
            question = query 
            app_id = "K88UKY-EPY4U9L98V"
            client = wolframalpha.Client('K88UKY-EPY4U9L98V')
            response = client.query(question)
            answer = next(response.results).text
            speak(answer)
            print(answer)
            # break use this for making it stop after a command
        elif '9' in query:
            question = query 
            app_id = "K88UKY-EPY4U9L98V"
            client = wolframalpha.Client('K88UKY-EPY4U9L98V')
            response = client.query(question)
            answer = next(response.results).text
            speak(answer)
            print(answer)
            # break use this for making it stop after a command
        
        elif '0' in query:
            question = query 
            app_id = "K88UKY-EPY4U9L98V"
            client = wolframalpha.Client('K88UKY-EPY4U9L98V')
            response = client.query(question)
            answer = next(response.results).text
            speak(answer)
            print(answer)
            # break use this for making it stop after a command
        
        elif 'integral' in query:
            question = query 
            app_id = "K88UKY-EPY4U9L98V"
            client = wolframalpha.Client('K88UKY-EPY4U9L98V')
            response = client.query(question)
            answer = next(response.results).text
            speak(answer)
            print(answer)
            # break use this for making it stop after a command
        
        

        
        #This is for the creator of the assistant

        # elif ("who made you", "who created you","Did I create you", 'who discovered you', 'did you make yourself')in query:
        #     speak('I was created by Nikunj Patel')
        #     print('I was created by Nikunj Patel')
        
        #This is for weather 
        elif "weather" in query:
            api_key = "d35aa773eeb843dbf143c422fcf1f634"
            base_url = "https://api.openweathermap.org/data/2.5/weather?q="
            speak("Sir, what is the name of the city?")
            city_name = takeCommand() 
            complete_url = base_url + city_name + "&units=metric&appid=" + api_key
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y=x["main"]
                now_temp = y["temp"]
                now_humid = y["humidity"]
                z = x["weather"]
                weather_desc = z[0]["description"]
                speak("The current temperature in celsius in " +city_name+ "is" + str(now_temp) + 
                        "\n while the humidity in percentage is " + str(now_humid) +
                        "\n and it looks like its" + str(weather_desc) + "in " + city_name)
        
          #exit status function
        elif 'thanks' in query:
            speak('Goodbye sir')
            sys.exit()

        elif 'thank you' in query:
            speak("That's my duty. Please call me if you require my assistance. Goodbye sir")
            sys.exit()
        
        elif 'goodbye jarvis' in query:
            speak("Have a wonderful day sir. Please call me if you require my assistance. Goodbye")
            sys.exit()

        elif 'bye' in query:
            speak("Have a wonderful day sir. Please call me if you require my assistance. Goodbye")
            sys.exit()

        ls.lsHotword_loop()
# UPCOMING FEATURES/IN DEVELOPMENT
#       add wake up word
#       add a note taking FEATURE
#       add a timer
#       add a calender
#       WATCH ANYTHING ON YOUTUBE WITH THE USE OF VOICE COMMMAND


      
