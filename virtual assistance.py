import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os

# program by Jaylu 😉

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
hour = datetime.datetime.now().hour
if hour >= 4 and hour < 10:
    mj = 'good morning. '
elif hour >= 10 and hour < 15:
    mj = 'good afternoon. '
elif hour >= 15 and hour < 20:
    mj = 'good evening. '
else:
    mj = 'good night. '

engine.say('Hey Jay. I am ariana. ' + mj + 'how may i help you')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            listener.pause_threshold = 0.7
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command

def run_va():
    command = take_command()
    print('User Said: ' + command)
    if 'open youtube' in command.lower():
        url = 'https://www.youtube.com/home'
        print('Opening')
        talk('opening ')
        pywhatkit.playonyt(url)
    elif 'time' in command.lower():
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'music' in command.lower():
        songs_dir = 'F:\Songs'
        talk('opening groove music player')
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))
    elif 'wikipedia' in command.lower():
        talk('searching wikipedia...')
        command = command.replace('wikipedia', '')
        results = wikipedia.summary(command, sentences=2)
        print(results)
        talk(results)
    elif 'i love you' in command.lower():
        print('I Love You Too')
        talk('i love you too')
    elif 'search' in command.lower():
        url1 = command.replace('search', '')
        talk('searching' + url1)
        pywhatkit.search(url1)
    elif 'shut down' in command.lower():
        talk('Do you want to shutdown your computer baby?')
        while True:
            command = take_command()
            if "no" in command:
                talk("Thank u sir I will not shut down the computer")
                break
            if "yes" in command:
                # Shutting down
                talk("Shutting the computer")
                os.system("shutdown /s /t 30")
                break
    else:
        if 'go back' in command.lower():
            talk('Ok Bye')
            exit()
        else:
            talk('please say it again.')
while True:
    run_va()
