import speech_recognition as sr
import pyttsx3
jarvis = pyttsx3.init()
import pywhatkit
import datetime
import wikipedia
import pyjokes
#voices=jarvis.getProperty('voices')
#jarvis.setProperty('voice',voices[1].id)

listener = sr.Recognizer()


def talk(text):
    jarvis.say(text)
    jarvis.runAndWait()


def take_Code():

    try:
        with sr.Microphone() as source:
            talk("listening...")
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if'jarvis'in command:
                command = command.replace('jarvis','')
                talk(command)
                print(command)
            #else:
            #talk("Sorry, I don't understand your request please try again")
            #print("Sorry, I don't understand your request please try again")
    except:
        pass
    return command

def run_Jarvis():
    command=take_Code()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk("Playing "+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M%p')
        talk("The current time is: "+time)
        print("The current time is: "+time)

    elif'who is'in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,3)
        print(info)
        talk(info)

    elif'joke'in command:
        talk(pyjokes.get_joke())

    else:
        talk("Sorry, I didn't understand the command please try again")
        print("Sorry, I didn't understand the command please try again")

while True:
    run_Jarvis()
