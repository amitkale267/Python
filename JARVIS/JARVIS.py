#########

__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'
__version__ = 'v 0.1'

"""
JARVIS:
- Control windows programs with your voice
"""

# import modules
from datetime import datetime  # datetime module supplies classes for manipulating dates and times
import subprocess  # subprocess module allows you to spawn new processes
master
import pyjokes

=======
from playsound import *  #for sound output
master
import speech_recognition as sr  # speech_recognition Library for performing speech recognition with support for Google Speech Recognition, etc..

# pip install pyttsx3                  
# need to run only once to install the library

# importing the pyttsx3 library
import pyttsx3
import webbrowser

# initialisation
engine = pyttsx3.init()


def sendEmail(do, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'yourr-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    
    
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    engine.say("Say something")
    engine.runAndWait()
    audio = r.listen(source)
    
    
#for audio output instead of print
def voice(p):
    myobj=gTTS(text=p,lang='en',slow=False)
    myobj.save('try.mp3')
    playsound('try.mp3')
    
# recognize speech using Google Speech Recognition
Query = r.recognize_google(audio, language = 'en-IN', show_all = True )
print(Query)


# Run Application with Voice Command Function
def get_app(Q):
    master
    if Q == "time":
        print(datetime.now())
        x=datetime.now()
        voice(x)
    elif Q == "notepad":
        subprocess.call(['Notepad.exe'])
    elif Q == "calculator":
        subprocess.call(['calc.exe'])
    elif Q == "stikynot":
        subprocess.call(['StikyNot.exe'])
    elif Q == "shell":
        subprocess.call(['powershell.exe'])
    elif Q == "paint":
        subprocess.call(['mspaint.exe'])
    elif Q == "cmd":
        subprocess.call(['cmd.exe'])
    elif Q == "browser":
        subprocess.call(['C:\Program Files\Internet Explorer\iexplore.exe'])
patch-1
    elif Q == "open youtube":
        webbrowser.open("https://www.youtube.com/")   # open youtube
    elif Q == "open google":
        webbrowser.open("https://www.google.com")    # open google
        
    elif Q == "email to other":                     # here you want to change and input your mail and password whenver you implement 
            try: 
                speak("What should I say?")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    r.pause_threshold = 1
                    audio = r.listen(source)
                to = "abc@gmail.com" 
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorray i am not send this mail")
=======
  master
    elif Q=="Take screenshot"
        snapshot=ImageGrab.grab()
            drive_letter = "C:\\"
            folder_name = r'downloaded-files'
            folder_time = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
            extention = '.jpg'
            folder_to_save_files = drive_letter + folder_name + folder_time + extention
            snapshot.save(folder_to_save_files)
     
    elif Q=="Jokes":
        print(pyjokes.get_joke())

master
    else:
        engine.say("Sorry Try Again")
        engine.runAndWait()
   
=======
=======

    apps = {
    "time": datetime.now(),
    "notepad": "Notepad.exe",
    "calculator": "calc.exe",
    "stikynot": "StikyNot.exe",
    "shell": "powershell.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "browser": "C:\Program Files\Internet Explorer\iexplore.exe"
    }

    for app in apps:
        if app == Q.lower():
            subprocess.call([apps[app]])
            break
    master
    else:
        engine.say("Sorry Try Again")
        engine.runAndWait()
master
    return
# Call get_app(Query) Func.
get_app(Query)
