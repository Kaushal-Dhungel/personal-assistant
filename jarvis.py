import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib
from random import randint

engine = pyttsx3.init('sapi5') # you can use other apis too
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) # voice[0] for girl's voice 


def speak(audio): # speak function .
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning Kaushal. ")

    elif hour>=12 and hour <18:
        speak("good afternoon Kaushal. ")

    else:
        speak("good evening Kaushal. ")

    speak("Hello,I am Jarvis,speed 1 terahertz memory 1 zeta byte, what can I do for you")


def takeCommand():
    #takes microphone commands and returns strings
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...!!")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:- {query}\n")


    except Exception as e:
        #print(e)

        print("Say that again please..")
        return "None"


    return query



def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your-email@gmail.com', 'password') #my email and password
    server.sendmail('your-email@gmail.com', to ,content)
    server.close()


if __name__== "__main__":

    

    wishMe()

    #while True:

    if 1:
        query = takeCommand().lower()

        #logic for executing....

        if 'wikipedia' in query:
            try:
                #speak('searching Wikipedia....')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2) # specify how many sentences of wikipedia you want 
                #speak("According to wikipedia") # this gets repeated
                print(results)
                speak(results)

            except Exception as e:
                speak('Pardon me, I could not find the result')

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'quora' in query:
            webbrowser.open("quora.com")

        elif 'facebook' in query:
            webbrowser.open("facebook.com")

        elif 'instagram' in query:
            webbrowser.open("instagram.com")

        elif 'twitter' in query:
            webbrowser.open("twitter.com")

        elif 'music' in query:
            music_dir = 'E:\\audios' # your music directory. use double slash(\\)
            songs = os.listdir(music_dir)
            print(songs)
            num = randint(0,2) #generating random num to play random songs. specify fix no for playing partiular song.
            os.startfile(os.path.join(music_dir, songs[num]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"  the time is {strTime}")

        elif 'send email' in query:
            try:
                speak("what should I write darling?")
                content = takeCommand()
                to = "receiver-address@gmail.com" # this is receiver's email address 
                sendEmail(to, content)
                speak("your email has been send ")

            except Exception as e:
                print(e)
                speak("Pardon me , I could not send the email")