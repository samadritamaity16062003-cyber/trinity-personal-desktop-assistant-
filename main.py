import speech_recognition as sr
import webbrowser
import pyttsx3           #helps to convert text to speech
import pocketsphinx
import time
import musiclibrary
import requests       #for getting news
import dateparser
from datetime import datetime
import threading
from google import genai
from google.genai import types
import re


def clean_text(text):
    # Remove bold markers **...**
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    # Remove single * (italics or bullets)
    text = text.replace("*", "")
    return text.strip()

"""VOICE"""                                
 #getting details of current voice
 #changing index, changes voices. o for male
 #changing index, changes voices. 1 for female
'''INITIALIZING SPEECH ENGINE ONCE'''

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # female voice (check available voices!)
    cleaned = clean_text(text)  # ✅ clean markdown
    engine.say(cleaned)
    engine.runAndWait()


url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=aac1b86e06944ce3a91d5f1cbff0983d"

def ai_process(command):
    client = genai.Client(
        api_key = "AIzaSyBa3O4JMDV_2poCIBlMfARTMlJA68tHt7U"
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are an AI assistant named Trinity skilled in general tasks like Alexa or Google Assistant."),
        contents= command
    )
    speak(response.text)
    print(response.text)



def set_reminder(task, time_expression): # Parse natural language time 
    reminder_time = dateparser.parse(time_expression) 
    if reminder_time is None:
         speak("Sorry, I couldn't understand the time.") 
         return 
    # Calculate delay in seconds
    delay_seconds = (reminder_time - datetime.now()).total_seconds()

    if delay_seconds <= 0:
        speak("The time you gave is in the past!")
        return
    # Define reminder function
    def reminder():
        speak(f"Reminder: {task}")

    # Schedule reminder
    threading.Timer(delay_seconds, reminder).start()
    speak(f"Okay, I will remind you to {task} at {reminder_time.strftime('%I:%M %p')}.")




def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com")
    elif "open insta" in c.lower():
        webbrowser.open("http://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open twitter" in c.lower():
        webbrowser.open("http://twitter.com")
    elif "open chat" in c.lower():
        webbrowser.open("http://chatgpt.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://www.whatsapp.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ", 1)[1]   #split the string only once at the first space.
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I don't know that song.")
    elif "news" in c.lower():
        response = requests.get(url)  
        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])
            if articles:
                speak("Here are the top 5 headlines from US.")
                for article in articles[:10]:   # only first 10
                    title = article.get("title", "No title available")
                    print(title + "\n")
                    speak(title)
            else:
                speak("sorry i cant find any news today")
                
        else: 
            speak(f"Failed to fetch the news. Error code {response.status_code}")
    
    elif "remind me" in c.lower():
        try:
            # Example: "remind me to drink water in 2 minutes"
            words = c.lower().split("remind me to", 1)[1].strip()
            parts = words.split(" in ", 1) if " in " in words else words.split(" at ", 1)

            task = parts[0].strip()
            time_expression = parts[1].strip()

            set_reminder(task, time_expression)
        except Exception as e:
            speak("Sorry, I couldn't set the reminder. Please try again.")
    
    else:
        # let openai handle the request:
        output = ai_process(c)
        speak(output)



def recognize_speech(recognizer, audio):
    """Try Google first, then fallback to Sphinx (offline)."""
    try:
        return recognizer.recognize_google(audio)   # online
    except sr.RequestError:
        print(" Google API unreachable, switching to offline mode...")
        try:
            return recognizer.recognize_sphinx(audio)  # offline
        except Exception:
            return None
    except sr.UnknownValueError:
        return None
        



if (__name__=="__main__"):
    speak("initializing Trinity....")
# listen for the wake worg Trinity"
# obtain audio from the microphone
r = sr.Recognizer()
while True:

# recognize speech using google
    print("Recognizing...")
    try:
        with sr.Microphone() as source:
            print("Listening for wake word...")
            audio = r.listen(source, timeout=2, phrase_time_limit=5)

        word = recognize_speech(r, audio)
        print("You said:", word)

        if word and "trinity" in word.lower():
            print("Trinity active")
            speak("ya")   #  should now speak
            # time.sleep(0.3)   # give audio time before reopening mic
            
            with sr.Microphone() as source:          # listen for the command
                print("Trinity active...listening for command")
                audio = r.listen(source)
                command = recognize_speech(r, audio)
                if command:
                    process_command(command)
                else:
                    speak("sorry, i didn't understand the command")

    
    except Exception as e:
        print("Error:", e)


    
