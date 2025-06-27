import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', engine.getProperty('rate') - 70)
    engine.say(text)
    engine.runAndWait()
