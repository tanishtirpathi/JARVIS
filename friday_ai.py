import pyttsx3  
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import pyaudio      
import struct
import math
from time import sleep
#import playsound
import ctypes
import pywhatkit
import keyboard
from pyautogui import hotkey
import wolframalpha
import openai
from keyboard import add_hotkey
from keyboard import press_and_release
from keyboard import press
from pyautogui import click
import pyautogui
import psutil
import os
#from pygame import mixer
from plyer import notification
'''import googletrans
from googletrans import Translator'''
import random
import wikipedia as googleScrap
import smtplib
import requests
'''
from time import sleep

dictapp = {"commandprompt":"cmd","vscode":"code","chrome": "chrome"}


def openappweb(query):
    speak("launching sir")
    if ".com"  in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")   
        query = query.replace(" ","")
        webbrowser.open(f"http://www.{query}")
    else:
        keys = list(dict.keys())
        for app in keys:
            if app in query:
                os.system(f"start{dictapp}")

def closeappweb():
    speak("closing boss")
    if "one tab " in query or "1 tab " in query:
        pyautogui.hotkey("ctrl","w")
    elif "two tab " in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tab closed")
    elif "three tab " in query or "1 tab " in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tab closed")
    elif "four tab " in query or "1 tab " in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5) 
        pyautogui.hotkey("ctrl","w")
        speak("all tab closed")
    elif "five tab " in query or "1 tab " in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tab closed")  
    else:
        keys = list(dict.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp}.exe ")





def wake():  
       r = sr.Recognizer()
       with sr.Microphone() as source:
        print("listening....................")
        #speak("yes sir speak")
        r.pause_threshold = 7
        audio = r.listen(source,0,7)

        try:
            print(" recognisinging ")
           # speak("wait sir")   
            query = r.recognize_google(audio,language='en-in')
            print(f"you:{query}")
        except Exception as e:
             #speak("please speak again boss ............")   
             print("please speak again............")
             return "None"
        return query
    

def wak():
   
        wake_up = wake().lower()
        if 'wake up'in wake_up:
           
        else:
             print("nothing")'''
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
            print("Hi welcome Mr Tanish " )
            break
Tester()
openai.api_key = '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'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[2].id)
def speak(audio):
   engine.say(audio)
   engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        tim = datetime.datetime.now().strftime("%I %M %p ")
        speak("hlo boss how are you feeling today")
        speak(f"its {tim}")
        speak("wese good morning")
        speak("what you want to do today")

    elif hour>=12 and hour<16:
        tim = datetime.datetime.now().strftime("%I %M %p")
        speak("hlo boss how your day is going")
        speak(f"its {tim}")
        speak("wese goodafternoon")
        speak("any task booss")
        

    elif hour>=16 and hour<19:
        time = datetime.datetime.now().strftime("%I %M %p ")
        speak(f"welcome boss its{time}")
        speak("wese good evening")
    elif hour>=19 and hour<23:
        time = datetime.datetime.now().strftime("%I %M %p ")
        speak(f"welcome boss its{time}")
        speak("what's the task for me ")
    else:
        time = datetime.datetime.now().strftime("%I %M %p ")
        speak(f"hlo welcome boss its {time}")
        speak("i think its time for your sleep")      
def takecommand():  
       r = sr.Recognizer()
       with sr.Microphone() as source:
        print("listening....................")
        #speak("yes sir speak")
        r.pause_threshold = 7
        audio = r.listen(source,0,7)

        try:
            print(" recognisinging ")
           # speak("wait sir")   
            query = r.recognize_google(audio,language='en-in')
            print(f"you:{query}")
        except Exception as e:
             speak("please speak again boss ............")   
             print("please speak again............")
             return "None"
        return query
def ai(prompt,open_ai = None):
    Filelog = open("open_ai.txt","r")   
    chat_log_template = Filelog.read()
    Filelog.close()
    if open_ai is None:
       open_ai = chat_log_template
    prompt = prompt
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the text-davinci-003 engine for ChatGPT
        prompt=prompt,
        max_tokens=200  # Adjust max_tokens as needed
)
    generated_text = response['choices'][0]['text']
    chat_log_template_update = chat_log_template + f"\n You: {prompt} \nJarvis :{generated_text}"
    Filelog = open("open_ai.txt","w")
    Filelog.write(chat_log_template_update)
    Filelog.close()
    if 'what is your name ' in prompt:
        speak("my name is friday boss") 
        print("my name is friday boss")
    elif 'how are you ' in prompt:
        speak("i am fine boss what about you") 
        print("my name is friday boss")
    else:
        pass
    print(generated_text)
    speak(f"ok boss{generated_text} ")
    t = takecommand().lower()
    if 'speak'in t or 'bolo' in t or 'bol' in t:
        speak("hi")
    else:
        pass
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)
def location():
    ip_add = requests.get('http://api.ipify.org').text
    url = 'http://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    state = geo_d['city']
    country = geo_d['country']
    speak(f"sir you are in{state,country}")
    print(f"sir you are in{state,country}")
    
if __name__ == "__main__": 
    wishMe()
    while  True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('searching...')
            query = query.replace("wikipedia","")
            query = query.replace("search","")
            query = query.replace("jarvis","")
            query = query.replace("kro","")
            query = query.replace("about","")
            query = query.replace("pe","")
            results = wikipedia.summary(query,2)
            speak(results)
            print(f"ok{results}")
        elif 'friday' in query or 'Friday' in query:
            query = query.replace("hi","")   
            query = query.replace("friday","")  
            query = query.replace("Friday","") 
            ai(prompt=query)
        elif 'google search' in query:       
            query = query.replace("jarvis","")
            query = query.replace("google search","")
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
        elif 'location' in query:
            location()
        elif 'lock' in query:
            speak('As You Wish')
            ctypes.windll.user32.LockWorkStation()
        elif 'website open'in query:
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
        elif 'cmd' in query:
            speak("starting ")
            os.system("start cmd") 
        elif 'music' in query:
            music_dir = "C:\\Users\\tanish\\Music\\music song"
            song = os.listdir(music_dir)
            rd = random.choice(song)
            os.startfile(os.path.join(music_dir, rd))  
        elif 'goodbye friday'in query:
            speak("good bye boss you can call me anytime ")
            speak("bye bye ")
            break
        elif 'youtube open' in query:
            webbrowser.open("youtube.com")
            speak("ok now sir ")  
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
        elif '  papa ko message ' in query:  
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
        elif  'plan' in query:
            webbrowser.open("https://www.notion.so/School-jee-framewok-7a58dbfbbfe141fe96a7663db2619bfd")
            speak("tanish boss plan your day")          
        elif 'coding time' in query:
            e= "Visual Studio Code.lnk"
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
        elif 'how are you ' in query:
            speak("i am fine boss what about you") 
            print("my name is friday boss")  
        elif 'charge' in query or 'power' in query or 'jann' in query or 'jan' in query: 
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
        elif "hi" in query or 'how are you' in query or 'hlo' in query:
            stMsgs = ['Just doing my thing!', 'I am fine !', 'Nice !', 'I am nice and full of energy','i am weel what about you boss','thank you for asking but i am always fell energetic ']
            speak(random.choice(stMsgs))   
        elif 'name'  in query:
            speak('My name is JARVIS boss')
        elif 'who made you' in query:
            speak ("I was created by Mr.Tanish sharma")
        elif "show my private files" in query or "enter prior mode" in query or "private" in query:
            speak("voice activation required")
            e_passcode = takecommand().lower()
            v_passcode = "ironman"
            if e_passcode == v_passcode:
                speak("Welcome! Mr.Tanish")
                webbrowser.open("")
            else:
                speak("access decline")
        elif 'alarm' in query:
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
                   exit()
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
        elif 'start'in query or 'open' in query or'visit'in query:
            name = query.replace("start",'')
            query.replace("jarvis","")
            query.replace("open","")
            query.replace("visit","")
            query.replace("kro","")
            query.replace("jao","")
            query.replace("ko","")
            query.replace("friday,l̥","")
            query.replace("kardo","")
            pyautogui.press('win')
            sleep(1)
            keyboard.write(name)
            sleep(1)
            print(name)
            keyboard.press('enter')
            sleep(0.5)
        elif 'something' in query or 'forget'in query or 'kuch'in query:
            Remember = open("Remember.txt","r")
            speak("yes boss")
            speak("you tell me to remember that"+Remember.read())
            print(f"yes{Remember}")
        elif 'good morning ' in query:
            speak("a very good morning sir")
            webbrowser.open("https://youtu.be/oCD5iPDjMgw?si=0mwxnldhyXhBN26n")
        elif 'good afternoon ' in query:
            speak(" its a very good day sir")
        elif 'good evening ' in query:
            speak("I hope your day was good  sir")
        elif 'good night ' in query:
            speak(" i hope you already have plan for next day")
            sht = takecommand().lower()
            if sht == "yes":
                speak("ok boss shut down the system")
                os.system("shutdown /s /t 1")
            elif  sht == "no":
                speak("ok fine boss i will help you ")
                webbrowser.open("https://www.notion.so/School-jee-framewok-7a58dbfbbfe141fe96a7663db2619bfd") 
            else:
                speak("i did not understand please speak again  `")
        elif 'shutdown' in query:
            speak("ok boss fine")
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            speak("ok boss restart the pc ")
            os.system("shutdown /r /t 3")
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
            path1 = "C:\\jarvis ke kiche hua screenshot\\"+path
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
            
            
            
            
'''
def wolfram(query):
    api_key = "TL4UQG-TQLVJ6RWY4"   
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)
    try:    
        answer = next(requested.results).text
        return answer
    except:
        speak("this is not answer able")
def temp(query):
    term = str(query)
    term = term.replace("jarvis","") 
    term = term.replace("temperature","") 
    term = term.replace("in","") 
    term = term.replace("kya ","") 
    term = term.replace("hai","") 
    term = term.replace("ha","")
    temp_query = str(term)
    if 'outside 'in temp_query or 'bhar' in query: 
        var1 = 'temperature in pathankot'
        ans = wolfram(var1)
        speak(f"{var1} is {ans}")
        print(f"{var1} is {ans}")
    else:
        var2 = 'temperature in' + temp_query
        answ = wolfram(var2)
        speak(f"{var2} is {answ}")
        print(f"{var2} is {answ}")

        welif 'lock'in query:
            pyautogui.hotkey('windows + l')
            speak("system lock")
        elif 'jarvis' in query:
            press('enter')
            speak("opebinhiiron mang")
            press('i+r+o+n+SPACE+m+a+n')
            speak("opebinhiiron mang")
            press('enter')
            speak("opebinhiiron mang")      
        elif 'shutdown' in query:
            speak("are you sure boss")
            shut = input("really boss ?(yes/no)")
            if shut == "yes":
                speak("ok boss shut down the system")
                os.system("shutdown /s /t 5")
            elif  shut == "no":
                speak("ok fine boss")
elif' email send' in query:
            try:
                speak('waht should i have to send')
                content = takecommand().lower()
                to = 'sharmatanish205@gmail.com'
                sendEmail(to,content)
                speak("fine sir email has bee sent")    
            except Exception as e:
                print(e)
                speak("sorry sir i am not able to sent" )  
  elif 'open' in query:
            from dict import openappweb 
            openappweb(query) 
        elif 'closed' in query:
            from dict import closedappweb 
            closedappweb(query) 
def translation(Text):
    line = str(Text)
    translate = Translator()
    results = translate.translate(line,str = 'en')
    data = results.text
    print(f"you : {data}")
    return data
def micconnect():
    query = takecommand().lower()
    data = translation(query)
    return data               
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',535)
    server.ehlo()
    server.starttls()
    server.login('tanishtirpathi0@gmail.com','Rattangarh')
    server.sendmail('tanishtirpathi0@gmail.com',to,content)
    server.close()
def passs(pass__inp):
    password = "iron man"
    l = str(password)
    if l==str(pass__inp):
        speak("welcome Tanish sir ")
        pass
    elif l!=str(pass__inp):
            print("you are not Tanish sir so you can't use me only tanish sir can use me")
            speak("password wrong  ")  
            speak("you are not tanish sir so you can't use me only tanish sir can use me")
            exit()                
speak("please speak the password to start me ")
    print("hint: best character in M.C.U")
    f = takecommand().lower() 
    passs(f)  
    elif 'task'in query:
            tasks =[]
            i = 0
            speak("no of task sir")
            no_task = int(input("enter heb jsgfjsdg   :"))
            for i in range(no_task):
                speak("speak the tasks boss")
                tasks.append(takecommand().lower())  
                file = open("taks.txt","w") 
                file.write(f"{i}:{tasks[i]}\n")
                file.close()
                speak("tasks save")
                break
        elif 'show' in query:
            file = open("taks.txt","r" )  
            content = file.read()
            file.close()
            speak("here is your to do")
            notification.notify(
                title = "tasks To-Do Boss :",
                message = content,
                timeout = 50)
           '''
   