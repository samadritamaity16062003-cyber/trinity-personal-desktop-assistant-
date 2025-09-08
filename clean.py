import re

def clean_text(text):
    # Remove bold markers **...**
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    # Remove single * (italics or bullets)
    text = text.replace("*", "")
    return text.strip()

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # female voice
    cleaned = clean_text(text)  # ✅ clean markdown
    engine.say(cleaned)
    engine.runAndWait()
