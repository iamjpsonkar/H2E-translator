import os
import datetime


if os.path.isfile("log.txt")!=True:
    os.system("pip install SpeechRecognition")
    os.system("pip install pygame")
    os.system("pip install googletrans")
    f=open("log.txt",'w')
    f.write("==> setup run "+str(datetime.datetime.now())+"\n")
    f.close()


f=open("log.txt",'a')
f.write("==> app run "+str(datetime.datetime.now())+"\n")
f.close()


import speech_recognition as sr
import pygame
from googletrans import Translator
import win32com.client
import urllib.request


mic=sr.Microphone()
r=sr.Recognizer()

speaker = win32com.client.Dispatch("SAPI.SpVoice")
translator = Translator()
print("I am Hindi to English translator")
speaker.Speak("I am Hindi to English translator")
print("I am the creation of Mr. Jay Prakash.")
speaker.Speak("I am the creation of Mr. Jay Prakash.")
lsd="hii"
lsd1="hii"
print("Translation speed depend on your Internet connection and the loudness of your voice")
speaker.Speak("Translation speed depend on your Internet connection and the loudness of your voice")
print("say ok bye to exit")
speaker.Speak("say okay bye to exit")
print("Wait I am connecting to internet")
speaker.Speak("Wait I am connecting to internet")
print("...",end="")

   
try :
    stri = "https://www.google.co.in"
    data = urllib.request.urlopen(stri,timeout=1)
    print("\nConnected")
    speaker.Speak("Connected")
except urllib.error.URLError as e:
    print("not connected")
    speaker.Speak("not Connected")
    print("please try again later")
    speaker.Speak("please try again later")
    quit()

print("Now speak in Hindi and I will Translate it into English")
speaker.Speak("Now speak in Hindi and I will Translate it into English")

while lsd!="ok bye":

    

    print("speak")
    with mic as source:
        audio=r.listen(source)
    
    try:
        lsd=str(r.recognize_google(audio))
        lsd1=translator.translate(lsd, dest='en').text
    except:
        lsd1="I didn't recognize"
        try :
            stri = "https://www.google.co.in"
            data = urllib.request.urlopen(stri,timeout=1)
        except urllib.error.URLError as e:
            print("No Internet Connection")
            speaker.Speak("No Internet Connection")
            print("please try again later")
            speaker.Speak("please try again later")
            quit()
        lsd=lsd1
    print("you : ",lsd)
    print("translated :  ",lsd1)
    speaker.Speak(lsd1)
    print("done")
    

