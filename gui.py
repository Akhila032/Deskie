from tkinter import *
from PIL import Image, ImageTk
import voice_input
import process
import responder

# Main Window
root = Tk()
root.title("Deskie - AI Assistant")
root.state("normal")  # For Windows
root.geometry("500x620")
root.resizable(False, False)
root.config(bg="#6af371")  # Light blue background

# Title Label
Label(root, text="Deskie - Your Smart Assistant", font=("Arial", 16, "bold"),
      bg="#6af371", fg="#333333").pack(pady=10)

# Load Assistant Image
try:
    img = Image.open("doremon.jfif").resize((150, 150))
    photo = ImageTk.PhotoImage(img)
    Label(root, image=photo, bg="#6af371").pack(pady=5)
except:
    Label(root, text="🤖", font=("Arial", 60), bg="#6af371").pack(pady=10)

# Deskie Response Display
response_label = Label(root, text="Hello! I’m Deskie. How can I assist you today?",
                       font=("Helvetica", 12), bg="#ffffff", fg="#333333",
                       width=50, height=4, wraplength=400, justify="left",
                       relief="ridge", bd=3)
response_label.pack(pady=20)

# Input Field
input_field = Entry(root, font=("Helvetica", 13), width=40, bg="white", fg="black", relief="flat")
input_field.pack(pady=10)

# Functions
def ask():
    voice_text = voice_input.capture_voice()
    if voice_text:
        reply = process.process_command(voice_text)
        response_label.config(text=reply)

def send():
    user_text = input_field.get()
    input_field.delete(0, END)
    if user_text.strip():
        reply = process.process_command(user_text)
        response_label.config(text=reply)

def delete():
    input_field.delete(0, END)
    response_label.config(text="")

def clear_conversation():
    response_label.config(text="")  # Clears the response display completely

def minimize_window():
    root.iconify()

def maximize_window():
    root.state("zoomed")


# Buttons Frame
button_frame = Frame(root, bg="#6af371")
button_frame.pack(pady=20)

# Button Style
btn_style = {
    "font": ("Helvetica", 11, "bold"),
    "bg": "#4ea8de",  # Blue
    "fg": "white",
    "width": 12,
    "bd": 0,
    "activebackground": "#4098d7",
    "activeforeground": "white"
}

# Ordered Buttons in Grid (2 rows)
ask_btn = Button(button_frame, text="ASK", command=ask, **btn_style)
ask_btn.grid(row=0, column=0, padx=10, pady=5)

send_btn = Button(button_frame, text="SEND", command=send, **btn_style)
send_btn.grid(row=0, column=1, padx=10, pady=5)

delete_btn = Button(button_frame, text="DELETE", command=delete, **btn_style)
delete_btn.grid(row=1, column=0, padx=10, pady=5)

clear_btn = Button(button_frame, text="CLEAR", command=clear_conversation, **btn_style)
clear_btn.grid(row=1, column=1, padx=10, pady=5)

minimize_btn = Button(button_frame, text="MINIMIZE", command=minimize_window, **btn_style)
minimize_btn.grid(row=2, column=0, padx=10, pady=5)

maximize_btn = Button(button_frame, text="MAXIMIZE", command=maximize_window, **btn_style)
maximize_btn.grid(row=2, column=1, padx=10, pady=5)

# Start GUI
root.mainloop()
