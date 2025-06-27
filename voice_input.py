import speech_recognition as sr
import responder

def capture_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        responder.speak("Listening...")
        try:
            audio_data = recognizer.listen(source, timeout=5)
            return recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            responder.speak("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            responder.speak("Please check your internet connection.")
            return None
        except sr.WaitTimeoutError:
            responder.speak("No voice detected. Please try again.")
            return None
