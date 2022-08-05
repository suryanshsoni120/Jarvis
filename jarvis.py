import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import cv2
import time
import random
import smtplib
import pywhatkit as kit
import pyjokes
import pyautogui
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow

mail_ids = {"suryansh": "surisoni10@gmail.com", "dad": "kamal.soni@icicilombard.com",  "brother": "shreyanshsoni0107@gmail.com"}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[3].id)
engine.setProperty('voice', voices[3].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am Jarvis. How may I help you?")


def takeCommand():
    """It takes microphone as input and returns string as output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=8)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please....")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Users email id', 'Users password')
    server.sendmail('Receipents email', to, content)
    server.close()


def news():
    news_link = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=f25d2258e66d4a788992cf6b8d7fc495"
    main_page = requests.get(news_link).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        print(f"Todays {day[i]} news is: ", head[i])
        speak(f"Todays {day[i]} news is: {head[i]}")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(chrome))
        # Logic to take command based on query
        if 'wikipedia' in query:
            print("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('chrome').open('youtube.com')
            speak("opening youtube")

        elif 'search on youtube' in query:
            speak("What would you like to see sir?")
            search = input("What would you like to see sir? ")
            webbrowser.open(f"https://www.youtube.com/search?q={search}")
            speak(f"opening {search} in youtube")

        elif 'close notepad plus plus' in query:
            speak('closing notepad++')
            os.system("taskkill /f /im notepad++.exe")

        elif 'open google' in query:
            webbrowser.get('chrome').open('google.com')
            speak("opening google")

        elif 'search on google' in query:
            while True:
                time.sleep(2)
                speak("What would you like to see sir?")
                browse = input("What would you like to see sir? ")
                try:
                    if 'exit' in browse or 'close' in browse:
                        speak("Ok sir")
                        break
                    else:
                        webbrowser.open(
                            f"https://www.google.com/search?q={browse}")
                        speak(f"opening {browse} in google")
                except:
                    speak("Sorry sir i am unable to find this")

        elif 'open amazon' in query:
            webbrowser.get('chrome').open('amazon.in')
            speak("opening amazon")

        elif 'open flipkart' in query:
            webbrowser.get('chrome').open('flipkart.com')
            speak("opening flipkart")

        elif 'open lms' in query:
            webbrowser.get('chrome').open('lms-kjsce.somaiya.edu')
            speak("opening lms")

        elif 'open notebook' in query:
            nb_path = "Path of Jupyter Notebook in your PC"
            os.startfile(nb_path)
            speak("opening jupyter notebook")

        elif 'open notepad plus plus' in query:
            npath = "Path of Notepad ++ in your PC"
            os.startfile(npath)
            speak("opening notepad ++")

        elif 'close notepad plus plus' in query:
            speak('closing notepad++')
            os.system("taskkill /f /im notepad++.exe")

        elif 'open teams' in query:
            tpath = "Path of Microsoft Teams in your PC"
            os.startfile(tpath)
            speak("opening microsoft teams")

        elif 'close ms teams' in query:
            speak('closing microsoft teams')
            os.system("taskkill /f /im Microsoft Teams.lnk")

        elif 'open cmd' in query:
            os.system('start cmd')
            speak("opening command prompt")

        elif 'close cmd' in query:
            speak('closing command prompt')
            os.system("taskkill /f /im cmd.exe ")

        elif 'open camera' in query:
            speak("opening camera")
            cam = cv2.VideoCapture(0)
            pic = 0
            while True:
                pic += 1
                ret, img = cam.read()
                print(ret)
                print(img)
                cv2.imshow('camera', img)
                k = cv2.waitKey(10)
                if k == 27:
                    break
            print(pic)
            cam.release()
            cv2.destroyAllWindows()

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'send mail' in query:
            speak("whom should i send the mail sir?")
            name = takeCommand().lower()
            if name in mail_ids:
                try:
                    speak("What should i say?")
                    content = takeCommand().lower()
                    to = mail_ids[name]
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry! Email could not be sent")
            else:
                speak("User not found sir")

        elif 'send message' in query:
                kit.sendwhatmsg(person, msg, time_hour, time_min)

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            speak("window has been switched")

        elif "what's the news" in query:
            speak("Browsing the latest news. Please wait sir")
            news()

        elif "check temperature" in query:
            speak("Which city's temperature would you like to check sir?")
            city = input(
                "Which city's temperature would you like to check sir? ")
            temp_url = f"https://www.google.com/search?q=temperature of {city}"
            req = requests.get(temp_url)
            data = BeautifulSoup(req.text, "html.parser")
            temperature = data.find("div", class_="BNeawe").text
            speak(f"Current temperature in {city} is {temperature}")

        elif "give me some information" in query:
            while True:
                speak("What information would you like to know sir?")
                Query = takeCommand()
                try:
                    if 'exit' in Query or 'close' in Query:
                        speak("That's all for today's information sir")
                        break
                    else:
                        max_result = 1
                        Result = search_wikihow(Query, max_result)
                        assert len(Result) == 1
                        print(Result[0].summary)
                        speak(Result[0].summary)
                except:
                    speak("Sorry sir i am unable to find this")

        # elif 'shut down the system' in query:
        #     os.system("shutdown /r /t 5")
        #
        # elif 'restart the system' in query:
        #     os.system("shutdown /r /t 5")
        #
        # elif 'let the system sleep' in query:
        #     os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")

        elif 'go to sleep' in query:
            speak("goodbye sir!")
            os.abort()
