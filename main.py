import speech_recognition as sr
import wikipedia 
import pyttsx3
import datetime 
import bardapi
import pyaudio
import struct 
import math 
from time import sleep
import ctypes 
import pywhatkit
import pyautogui
import keyboard 
from pyautogui import hotkey 
from keyboard  import add_hotkey 
from keyboard import press_and_release 
from keyboard import press 
from pyautogui import click 
import pyautogui 
import psutil
from bardapi import BardCookies 
import datetime
import os 
from plyer import notification
import random
import wikipedia as googleScrap 
import smtplib
import requests
from bs4 import BeautifulSoup 
from time import sleep 
import webbrowser
from bardapi import Bard
import wolframalpha
from googletrans import Translator
import google.generativeai as genai
INITIAL_TAP_THRESHOLD = 0.5
FORMAT = pyaudio.paInt16
SHORT_NORMALIZE = (1.0/32768.0)
CHANNELS = 2
RATE = 44100  
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)
OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME                    
UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME 
MAX_TAP_BLOCKS = 0.15/INPUT_BLOCK_TIME
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
engine.setProperty('rate', 180)

def get_rms( block ):
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, block )
    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt( sum_squares / count )
class TapTester(object):

    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = INITIAL_TAP_THRESHOLD
        self.noisycount = MAX_TAP_BLOCKS+1 
        self.quietcount = 0 
        self.errorcount = 0

    def stop(self):
        self.stream.close()

    def find_input_device(self):
        device_index = None            
        for i in range( self.pa.get_device_count() ):     
            devinfo = self.pa.get_device_info_by_index(i)   
            # print( "Device %d: %s"%(i,devinfo["name"]) )

            for keyword in ["mic","input"]:
                if keyword in devinfo["name"].lower():
                    # print( "Found an input: device %d - %s"%(i,devinfo["name"]) )
                    device_index = i
                    return device_index

        if device_index == None:
            print( "No preferred input found; using default input device." )

        return device_index

    def open_mic_stream( self ):
        device_index = self.find_input_device()

        stream = self.pa.open(   format = FORMAT,
                                 channels = CHANNELS,
                                 rate = RATE,
                                 input = True,
                                 input_device_index = device_index,
                                 frames_per_buffer = INPUT_FRAMES_PER_BLOCK)

        return stream

    def listen(self):

        try:
            block = self.stream.read(INPUT_FRAMES_PER_BLOCK)

        except IOError as e:
            self.errorcount += 1
            print( "(%d) Error recording: %s"%(self.errorcount,e) )
            self.noisycount = 1
            return

        amplitude = get_rms( block )

        if amplitude > self.tap_threshold:
            self.quietcount = 0
            self.noisycount += 1
            if self.noisycount > OVERSENSITIVE:

                self.tap_threshold *= 1.1
        else:            

            if 1 <= self.noisycount <= MAX_TAP_BLOCKS:
                return "True-Mic"
            self.noisycount = 0
            self.quietcount += 1
            if self.quietcount > UNDERSENSITIVE:
                self.tap_threshold *= 2
def Tester():

    tt = TapTester()

    while True:
        kk = tt.listen()
        if "True-Mic" == kk:
            print("Hi ! sir my name is JARVIS welcome Mr Tanish " )
            break
Tester()

def speak(audio):
     engine.say(audio)
     engine.runAndWait()
def ai():
    
    GOOGLE_API_KEY ='AIzaSyD7xVt7D1G97UqCeuWaQF5g-2IjTrP_D8Q'
    genai.configure(api_key=GOOGLE_API_KEY) 
     
    gernation_config = {
        "temperature":0.5,
        "top_p":1,
        "top_k":1,
        "max_output_tokens":400,
    }

    modal=genai.GenerativeModel('gemini-1.0-pro-latest',generation_config=gernation_config)
    convo =modal.start_chat()
    
    while True:
        user_input =take().lower()
        convo.send_message(user_input)
        print(convo.last.text)
        speak(convo.last.text)
GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
             "ok jarvis", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir","Hey there! What's going on?",
"Hi! What can I do for you today?,"
"What's up? Need anything from me?",
"How's it going? Let me know if you need anything.",
"Yo! What can I help you with?",
]
def friday():
    
    GOOGLE_API_KEY ='AIzaSyD7xVt7D1G97UqCeuWaQF5g-2IjTrP_D8Q'
    genai.configure(api_key=GOOGLE_API_KEY) 
     
    gernation_config = {
        "temperature":0.5,
        "top_p":1,
        "top_k":1,
        "max_output_tokens":2400,
    }

    modal=genai.GenerativeModel('gemini-1.0-pro-latest',generation_config=gernation_config)
    convo =modal.start_chat()
    
    while True:
        user_input =take().lower()
        convo.send_message(user_input)
        print(convo.last.text)
        speak(convo.last.text)
def take():  
       r = sr.Recognizer()
       with sr.Microphone() as source:
        print("listening....................")
        #speak("yes sir speak")
        r.pause_threshold = 2
        audio = r.listen(source,0,6)

        try:
            print(" recognisinging ")
           # speak("wait sir")   
            query = r.recognize_google(audio,language='en-in')
            print(f"you:{query}")
        except Exception as e:
             speak(" boss ............")   
             print("please speak again............")
             return "None"
        return query
def takecommand():  
       r = sr.Recognizer()   
       with sr.Microphone() as source:
        #print("listening....................")
        #speak("yes sir speak")
        #r.pause_threshold = 1
       # audio = r.listen(source,0,9)
        print('Listening........................')
        r.pause_threshold = 1
       # r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

        try:
            print(" recognisinging ")
           # speak("wait sir")   
            query = r.recognize_google(audio,language='en-in')
            print(" ")
            print(f"you:{query}")
            print(" ")
            print("JARVIS :- ")
            return query
        except Exception as e:
             speak(" sorry.....")   
             print("please speak again............")
             return "some internet issue boss please forgive me"    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        tim = datetime.datetime.now().strftime("%I %M %p ")
        speak("welcome back, boss")
        speak(f"its {tim} good morning")
       ## temp()
    elif hour>=12 and hour<16:
        tim = datetime.datetime.now().strftime("%I %M %p")
        speak("hlo boss  welcome back")
        speak(f"its {tim}")
        #temp()
    elif hour>=16 and hour<18:
        time = datetime.datetime.now().strftime("%I %M %p ")
       # temp()
        speak(f"welcome boss its{time} good evening")
      
    elif hour>=18 and hour<23:
        time = datetime.datetime.now().strftime("%I %M %p ")
        #temp()
        speak(f"welcome boss its{time}")
        speak("what's the task for me ")
       
    else:
        time = datetime.datetime.now().strftime("%I %M %p ")
        speak(f"hlo welcome boss its {time}")
        #temp()
        speak("i think its time for your sleep")
       
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)        
_key = "ELTPYE-JGY9WU82GV"
def computational_intelligence(question):
    try:
        client = wolframalpha.Client(_key)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None
    
if __name__ == "__main__": 
    wishMe()
    while True:
        query = takecommand().lower()
       # listen = take().lower()
        query.replace("jarvis","")
        #querylisten.replace("jarvis","")
        
        if 'wikipedia' in query:
            speak('searching...')
            query = query.replace("wikipedia","")
            query = query.replace("tell me about","")
            query = query.replace("search","")
            query = query.replace("jarvis","")
            query = query.replace("kro","")
            query = query.replace("about","")
            query = query.replace("pe","")
            results = wikipedia.summary(query,2)
            speak(results)
            print(f"ok{results}")

        elif query in GREETINGS:
            speak(random.choice(GREETINGS_RES))
        elif 'close all tab' in query:
            speak("ok sir as your wish")
            keyboard.press_and_release('ctrl+shift+w')   
        elif 'close tab' in query:
            speak("ok sir as your wish")
            keyboard.press_and_release('ctrl+w')
        elif 'lock' in query:
            speak('As You Wish')
            ctypes.windll.user32.LockWorkStation()
            exit()
        elif "calculate" in query:
            speak("tell me the question sir")
            question = take().lower()
            answer = computational_intelligence(question)
            speak(answer)
        elif "where i am" in query or "current location" in query or "where am i" in query:
                try:
                    city, state, country = take().lower()
                    print(city, state, country)
                    speak(
                        f"You are currently in {city} city which is in {state} state and country {country}")
                except Exception as e:
                    speak(
                        "Sorry sir, I coundn't fetch your current location. Please try again")

        elif 'website'in query:
            speak("booss which website i have to open ") 
            name = takecommand().lower()
            we = 'https://www.' + name +'.com'
            webbrowser.open(we)
            speak(f"opening{name}") 
        elif 'song'in query:
            speak("booss which song you have to listen ") 
            nme = takecommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={nme}")
            speak(f"you can choose any music related to {nme}")  
        
        elif "take screenshot" in query or "take a screenshot" in query or "capture the screen" in query:
                speak("By what name do you want to save the screenshot?")
                name = takecommand().lower()
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")
        elif 'cmd' in query:
            speak("starting ")
            os.system("start cmd") 
        elif 'music' in query:
            music_dir = "C:\\Users\\tanish\\Music"
            song = os.listdir(music_dir)
            rd = random.choice(song)
            os.startfile(os.path.join(music_dir, rd))  
        elif 'goodbye friday'in query:
            speak("good bye boss you can call me anytime ")
            speak("bye bye ")
            break
        elif 'weather' in query or'temperature' in query or'mosam' in query  or'masom' in query:    
            speak("speak the place sir")  
            l=takecommand().lower()  
            if 'outside 'in l or 'bhar ' in l or 'bhr' in l:
                pywhatkit.search(f"weather today near Jhakhar Pindi, Punjab")
                speak("see the weather boss ")
                try:
                        result = googleScrap.summary(query,2)
                        speak(result)
                        print(result)
                except: 
                        speak("No Speakable Data Available!") 
            else:
                pywhatkit.search(f"today weather in {l}")
                try:
                        result = googleScrap.summary(query,2)
                        speak(result)
                        print(result)
                except: 
                        speak("No Speakable Data Available!") 
                speak(f"sir the weather in {l} is ")
        elif ' play  sad song' in query:
            webbrowser.open("https://youtu.be/lyOo1MZawU0?si=5_DUaA7GEOYVRyho") 
            speak("playing song")
        elif 'Trucaller ' in query:
            webbrowser.open("truecaller.com")
            speak("ok now sir ") 
        elif 'google open' in query:    
           speak("what sould i have to search ")   
           cm = takecommand().lower()   
           webbrowser.open(f"{cm}")    
        elif 'youtube search' in query:          
            speak("sir what should i have to search ") 
            cm = takecommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={cm}")
            speak("searching")
            pywhatkit.playonyt(cm)
            speak("this may also help you boss")
        elif 'whatsapp ' in query:
             speak("speak the number boss")
             contact= takecommand().lower()
             num = '+91'+ contact
             speak("What do you want to say?")
             message = takecommand().lower()
             speak("When to send?")
             s_time= takecommand().lower()
             if 'later' in s_time:
                 speak ("Tell me about the hour?")
                 hour__ =int(takecommand().lower())
                 speak("Tell me about the minutes?")
                 minute__ =int(takecommand().lower())
             elif 'now' in s_time:
                hour__ = (datetime.datetime.now().hour)
                if (datetime.datetime.now().second) < 30:
                    minute__ = (datetime.datetime.now().minute) + 1
                else:
                    minute__=(datetime.datetime.now().minute) + 2
             speak("Sending Message.")
             pywhatkit.sendwhatmsg(num, message, hour__,minute__)        
        elif ' Instagram' in query:
            webbrowser.open("https://www.instagram.com//")
            speak("ok now sir ") 
        elif 'snapchat' in query:
            webbrowser.open("https://www.snapchat.com//")
            speak("ok now sir ") 
        elif 'gmail ' in query:
            webbrowser.open("gmail.com")
            speak("ok now sir ") 
        elif 'papa ko message ' in query:  
             num = '+918437493081' 
             speak("What do you want to say?")
             message = takecommand().lower()
             speak("When to send?")
             s_time= takecommand().lower()
             if 'later' in s_time:
                 speak ("Tell me about the hour?")
                 hour__ =int(takecommand().lower())
                 speak("Tell me about the minutes?")
                 minute__ =int(takecommand().lower())
             elif 'now' in s_time:
                hour__ = datetime.datetime.now().hour
                if (datetime.datetime.now().second) < 30:
                    minute__ = (datetime.datetime.now().minute) + 1
                else:
                    minute__=(datetime.datetime.now().minute) + 2
             speak("Sending Message.")
             pywhatkit.sendwhatmsg(num, message, hour__,minute__)  
             speak(f"done boss message sent to{num} ")
        elif 'plan' in query:
            webbrowser.open("https://www.notion.so/School-jee-framewok-7a58dbfbbfe141fe96a7663db2619bfd")
            speak("tanish boss plan your day")          
        elif 'coding time' in query:
            e= "jarvis app backup\\Visual Studio Code.lnk"
            os.startfile(e)    
            speak("opening vs code") 
        elif 'my day ' in query:
             webbrowser.open("https://calendar.google.com/calendar/u/0/r")
             speak("ok sir i will")
        elif 'time table ' in query:
             webbrowser.open("https://docs.google.com/document/d/1ptEb30nZxz2P-uKjZkLpzhGCZoZAK2_gS27FlycFtO8/edit#heading=h.h4kgoop6fffj")
             speak("ok sir i will")
        elif 'message' in query:
             ont = takecommand().lower()
             cont = '+91'+ ont 
             mess = takecommand().lower()    
        elif 'what is your name ' in query:
            speak("my name is jarvis boss") 
            print("my name is jarvis boss")
        elif 'how are you friday ' in query:
            speak("i am fine boss what about you") 
            print("my name is friday boss")  
        elif 'charge' in query or 'power' in query or 'jaan' in query or 'batery' in query or 'jan' in query: 
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent) 
            time_left = secs2hours(battery.secsleft)
            print (percent)
            if percent < 45:
                speak('sir, please connect charger because i can survive only '+ time_left)
            if percent > 45:
                speak("boss its your choice t charge me but i can survive  "+ time_left)
            else:
                speak("don't worry sir, charger is connected")       
        elif 'name'  in query:
            speak('My name is JARVIS boss')
        elif 'who made you' in query:
            speak ("I was created by Mr.Tanish sharma")
        elif "mark 2" in query or "mark two" in query or "mark-2" in query  or "mark to" in query:
            speak("voice activation required boss")
            e_passcode = takecommand().lower()
            v_passcode = "iron man"
            if e_passcode == v_passcode:
                speak("acess granted!, Welcome back! Mr.Tanish")
                webbrowser.open("https://github.com/tanishtirpathi/JARVIS/blob/main/friday_ai.py") 
                speak("boss i'm saving the progress")
                ol =takecommand().lower()
                if 'ok'in ol or 'thik hai 'in ol or 'yes' in ol: 
                    speak("saving...............")
                    speak("thank you sir for your permission")  
                else:
                    speak("ok sir as your wish boss")       
            else:
                speak("access decline")
       
        elif 'hello 'in query:
            speak("hello tanish sir how are you") 
        elif 'i am fine'in query:
            speak("would you like to listen my favroute music") 
            u = takecommand().lower()
            if u == "yes":
                speak("you are so nice ")
                yre = "https://youtu.be/2vKMY75kvjI?si=16elG23pxOxp0Pq_"
                webbrowser.open(yre)
            elif u =="no":
                speak("ok then i will not talk to you")
                break
            else:
                ("i dont have mood to talk to talk to you so give me a task")
        elif 'how are you' in query:
            speak("you have so beautiful heart because you ask about me ")
        elif 'jarvis mera name ' in query:
            speak("your name is Tanish ,sir ") 
        elif 'who are you' in query:
            speak("I am JARVIS your assistant") 
        elif 'tum kon ho' in query:
            speak("I am JARVIS your assistant")           
        elif 'bye-bye' in query or 'bye ' in query or 'so jao ' in query or 'soo jao ' in query or'band ho jao' in query:
            speak("good bye sir ")
            speak("see you later ")
            break
        elif 'tum thik' in query or 'tum theek'in query:
            speak("yess boss  I was also thinking this")
            speak(" so good night boss")
            speak("i'm going to take a good sleep")
            speak("bye bye boss take care")
            break
        elif 'thank you'in query or 'thanks 'in query or 'thank u' in query:
            speak("mention not sir ")  
            speak("you are my boss its my duty")     
        elif 'remember that' in query or 'note' in query or 'yad ' in query or 'yadev' in query or 'yadav ' in query  or'not' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("jarvis","")
            rememberMsg = rememberMsg.replace("note","")
            rememberMsg = rememberMsg.replace("not","")
            rememberMsg = rememberMsg.replace("yad","")
            rememberMsg = rememberMsg.replace("rakhna ","")
            rememberMsg = rememberMsg.replace("yadav ","")
            rememberMsg = rememberMsg.replace("Rakho","")
            speak("youtell me to remember that:"+rememberMsg)
            Remember = open("Remember.txt","w")
            Remember.write(rememberMsg)
            Remember.close()   
        elif 'something' in query or 'forget'in query or 'kuch'in query:
            Remember = open("Remember.txt","r")
            speak("yes boss")
            speak("you tell me to remember that"+Remember.read())
            print(f"yes{Remember}")
        elif 'good morning' in query:
            speak("a very good morning sir")
            webbrowser.open("https://youtu.be/xJ3vatsNQDU?si=WXGj6sWt2VM6Zff5")
        elif 'good afternoon ' in query:
            speak(" its a very good day sir")
        elif 'good evening ' in query:
            speak("I hope your day was good  sir")
        elif 'good night ' in query:
            speak(" i hope you already have plan for next day")
            sht = takecommand().lower()
            if sht == "yes":
                webbrowser.open("https://youtu.be/xJ3vatsNQDU?si=WXGj6sWt2VM6Zff5")
                speak("ok boss shut down the system")
                os.system("shutdown /s /t 1")
            elif  sht == "no":
                speak("ok fine boss i will help you ")
                webbrowser.open("https://www.notion.so/School-jee-framewok-7a58dbfbbfe141fe96a7663db2619bfd") 
                webbrowser.open("https://youtu.be/xJ3vatsNQDU?si=WXGj6sWt2VM6Zff5")
            else:
                webbrowser.open("https://youtu.be/xJ3vatsNQDU?si=WXGj6sWt2VM6Zff5")
        elif 'shutdown' in query:
            speak("ok boss fine")
            speak("three")
            speak("two")
            speak("one")
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            speak("ok boss restart the pc ")
            speak("three")
            speak("two")
            speak("one")
            os.system("shutdown /r /t 1")
        elif 'sleep' in query:
            speak("as your wish sir")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif'open insta profile' in query:
            speak("please enter the username correctly")
            name = input("enter the username :")
            webbrowser.open(f"www.instagram.com/{name}")    
        elif 'date' in query:
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
            speak(f"boss the date is {day}{month}")
            speak(f"and the year is {year}")
            speak("boss i think you have to remember the date atleast")
        elif 'screenshot'in query or 'save' in query:
            speak("boss file name ")
            k = takecommand().lower()
            path = k + '.png'
            path1 = "jarvis ke kiche hua screenshot"+path
            kk = pyautogui.screenshot()
            speak("ok boss")
            kk.save(path1)
            speak("you want to see the file boss")
            y = takecommand().lower()
            if 'yes' in y or 'haa'in y or 'ha' in y:
                os.startfile("C:\\jarvis ke kiche hua screenshot")
                speak("here is the file sir")
            else:
                pass          
        elif 'full screen' in query:
            keyboard.press('f')
        elif 'type'in query:
            query.replace("jarvis","")
            query.replace("type","")
            query.replace("kro","")
            keyboard.write(query)
      
        elif 'google ' in query or'show ' in query or'dikhao' in query  or'dikhna' in query:       
                    query = query.replace("jarvis","")
                    query = query.replace("show that","")
                    query = query.replace("google search","")
                    query = query.replace("show me","")
                    query = query.replace("google","")
                    query = query.replace("kro","")
                    query = query.replace("karo","")
                    query = query.replace("kardo","")
                    query = query.replace("krodo","")   
                    query = query.replace("about","")
                    speak("This Is What I Found On The Web!")   
                    pywhatkit.search(query)
                    try:
                        result = googleScrap.summary(query,2)
                        speak(result)
                        print(result)
                    except: 
                        speak("No Speakable Data Available!") 
        
        else:
            ai()
            
""" elif 'alarm' in query:
            speak(" ok boss")
            speak("enter the time boss:-")
            time = input("enter the time boss")
            speak("done sir")
            while True:
                time_Ac = datetime.datetime.now()
                now = time_Ac.strftime("%H:%M")
                if now ==  time:
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ") 
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("its time to wake up boss ")
                    speak("ok boss if you don't wake up i will start music  ")
                    speak("itsyour last chance boss ")
                    speak("music start ")
                    song_2 = "c:\\Users\\tanish\\Music\\music song\\Babam Bam-(PagalWorld).mp3"
                    os.startfile(song_2)               
                elif now>time:
                   exit()"""