import speech_recognition as sr
import pyttsx3 as ps
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser


engine=ps.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk('good morning')
        talk('Hello i am alexa please tell me how can i help you')
    elif hour>=12 and hour<18:
        talk("Good Afternoon")
        talk('Hello i am alexa please tell me how can i help you')
    else:
        talk("good evening")
        talk('Hello i am alexa please tell me how can i help you')
    

def take_command():
    try:
        listener = sr.Recognizer()
        mic=sr.Microphone()
        with mic as source:
            print("\nListening...\n")
            # listener.pause_threshold=1
            listener.energy_threshold=200
            audio=listener.listen(source)
            print('Recognizing...\n')
            command=listener.recognize_google(audio)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(f"User said : {command}\n")

            elif 'alexa' not in command:
                print('Alexa said: I am alexa please mention alexa in command')
                talk('i am alexa please mention alexa in command')
                take_command()
                
    except:
        print('Alexa said: Powering off...')
        talk('Powering off')
        quit()
   
    return command

def run_alexa():
    command=take_command()
    # print(command)
    if 'play' in command:
        song=command.replace('play','')
        print(f'Alexa said: Playing{song}\n')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        quit()
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print('Alexa said: '+time)
        talk("current time is " + time)
    elif 'wiki' in command:
        object=command.replace('wiki','')
        info=wikipedia.summary(object,2)
        print('Alexa said: '+info)
        talk(info)
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print('Alexa said: '+joke)
        talk(joke)
    elif 'open youtube' in command:
        webbrowser.open("youtube.com")
    elif 'stop' in command:
        print('Shutting down...')
        talk('good bye see you again')
        quit()
    else:
        print('Alexa said: Please say the command again')
        talk('please say the command again')


print('Initializing Alexa...')   
wishme()
while True:
    run_alexa()
