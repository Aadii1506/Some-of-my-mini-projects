import pyttsx3 as p
import speech_recognition as sr
import googlesearch
import webbrowser
import re
import time
def searchqry(query):
    s = googlesearch.search(query,num_results=1)
    for j in s:
        print(webbrowser.open(j))


engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',160)
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
speak("Hello, I am your Assistant!, How are you Aadi?")

speak('what can i do for you?')
while True:
    r=sr.Recognizer()#gonna retrieve audio from microphone
    with sr.Microphone() as source:
        r.energy_threshold=10000  #cancles noises around me and mere voice sunega bs
        r.adjust_for_ambient_noise(source,1.2)#ye sunega meri bat source ke through
        speak("aahan listening..")
        print("listening..")
        audio=r.listen(source)
        text=r.recognize_google(audio) #google ke api ko bhejdega ye jo voice hm send krenge
        if re.search("search",text):
            searchqry(text)
            time.sleep(4)


        if text=="stop":
            break
        print(text)
        if 'what' and 'about' and 'you' in text:
            speak("I am having a good day aadi!")






