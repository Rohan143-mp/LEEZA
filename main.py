import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'liza' in command:
                command = command.replace('liza', '')
                print(command)
    except:
        pass
    return command


def run_liza():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        
    elif 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        
    elif 'date' in command:
        talk('sorry, I my Dating Soham  right now')
        
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
        
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
            
    elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
            
    elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
            
    elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
            
    elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
            
    elif 'open whatsapp' in query:
            speak("opening whatsapp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
            
    elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
            
    elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
            
    elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
            
    elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
            
    elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
            
    else:
        talk('Please say the command again.')


while True:
    run_liza()

while False:
    run_liza()
