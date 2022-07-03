from datetime import datetime
import speech_recognition as sr
import pyttsx3 as ps
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine=ps.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        mic=sr.Microphone()
        with mic as source:
            talk('Hello i am alexa I am listening to you')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                # print(command)
    except:
        pass
    return command

def run_alexa():
    command=take_command()
    # print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("current time is " + time)
    elif 'wiki' in command:
        object=command.replace('wiki','')
        info=wikipedia.summary(object,2)
        print(info)
        talk(info)
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'stop' in command:
        talk('good bye see you again')
        quit()
    else:
        talk('please say the command again')
    
while True:
 run_alexa()
 