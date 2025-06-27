import os
import launcher
import responder
import datetime
import webbrowser
import re

#  Search files/apps by keyword in given folders
def search_and_open(keyword, search_dirs):
    for folder in search_dirs:
        for root, _, files in os.walk(folder):
            for file in files:
                if keyword.lower() in file.lower():
                    full_path = os.path.join(root, file)
                    try:
                        os.startfile(full_path)
                        responder.speak(f"Opening {file}")
                        return f"Opened: {file}"
                    except Exception as e:
                        return f"Found file but couldn't open it: {str(e)}"
    return f"No file found with keyword: {keyword}"

#  Main command handler
def process_command(user_input):
    if user_input is None:
        return "I didn't hear anything."

    command = user_input.lower().strip()

    #  Greeting with exact match only
    if command in ["hello", "hi", "hey"]:
        responder.speak("Hello! How can I assist you?")
        return "Hello! How can I assist you?"

        #  Who are you functionality
    elif "who are you" in command or "what are you" in command or "tell me about yourself" in command:
        intro = "I’m Deskie, your personal desktop assistant. I can help you open files, get the weather, browse the web, and more."
        responder.speak(intro)
        return intro

    #  Weather: "weather" or "weather in <city>"
    elif "weather" in command:
        match = re.search(r"weather in ([a-zA-Z\s]+)", command)
        if match:
            city_name = match.group(1).strip()
            weather_info = launcher.get_weather(city_name)
        else:
            weather_info = launcher.get_weather()  # current location
        responder.speak(weather_info)
        return weather_info

    #  Time
    elif "what is time now " in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        responder.speak(f"The current time is {time}")
        return f"The current time is {time}"

    #  Date
    elif "today date" in command:
        date = datetime.datetime.now().strftime("%A, %d %B %Y")
        responder.speak(f"Today is {date}")
        return f"Today is {date}"

    #  Open websites
    elif "open youtube for me" in command:
        webbrowser.open("https://www.youtube.com")
        responder.speak("Opening YouTube.")
        return "Opened YouTube."

    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com")
        responder.speak("Opening Gmail.")
        return "Opened Gmail."
    
    elif "open google" in command or "launch google" in command:
        responder.speak("Opening Google.")
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    elif "open vs code" in command or "launch visual studio code" in command or "start code editor" in command:
        try:
            # If 'code' command is available
            os.system("code")
            responder.speak("Opening Visual Studio Code.")
            return "Opening VS Code."
        except:
            # Optional: fallback if code command doesn't work
            try:
                path ="C:/Users/nielit/AppData/Local/Programs/Microsoft VS Code/Code.exe"

                os.startfile(path)
                responder.speak("Opening Visual Studio Code.")
                return "Opening VS Code."
            except:
                responder.speak("Sorry, I couldn't open Visual Studio Code.")
                return "VS Code not found."
    #  Exit
    elif command in ["exit", "bye", "quit"]:
        responder.speak("Goodbye from Deskie!")
        return "Goodbye from Deskie!"
        #  Thank you response
    
    elif "open downloads" in command:
        path = os.path.join(os.path.expanduser("~"), "Downloads")
        os.startfile(path)
        responder.speak("Opening Downloads folder.")
        return "Opened Downloads."
    
    elif "open documents" in command:
        path = os.path.join(os.path.expanduser("~"), "Documents")
        os.startfile(path)
        responder.speak("Opening Documents folder.")
        return "Opened Documents."
    
    elif "open desktop" in command:
        path = os.path.join(os.path.expanduser("~"), "Desktop")
        os.startfile(path)
        responder.speak("Opening Desktop folder.")
        return "Opened Desktop."
    
    elif "open" in command or "play" in command or "launch" in command:
        match = re.search(r"(open|play|launch)\s(.+)", command)
        if match:
            keyword = match.group(2).strip()

            # Folders to search in
            search_folders = [
                r'C:\Users\nielit\Documents',
                r'C:\Users\nielit\Downloads',
                r'C:\Users\nielit\Pictures',
                r'C:\Users\nielit\Videos',
                r'C:\Users\nielit\Desktop',
                r'C:\Program Files',
                r'C:\Program Files (x86)'
            ]

            result = search_and_open(keyword, search_folders)
            return result
        else:
            return "Please specify what you want to open."
    elif "thank" in command:
        responder.speak("You're welcome! Happy to help.")
        return "You're welcome!"

    #  Unknown command
    else:
        responder.speak("Sorry, I didn’t understand that.")
        return "Sorry, I didn’t understand that."
