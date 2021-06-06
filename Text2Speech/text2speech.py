from tkinter import * 
from gtts import gTTS
from playsound import playsound
import os

root = Tk()
root.geometry("350x300")
root.configure(bg = 'white')
root.title("TEXT 2 SPEECH")

Label(root, text = "TEXT 2 SPEECH", font = "arial 20 bold", bg = 'white').pack()

Msg = StringVar()
Label(root, text = "Enter Text", font = 'arial 15 bold', bg = 'white').place(x = 20, y = 60)

entry_field = Entry(root, textvariable = Msg, width = '50')
entry_field.place(x = 20, y = 100)

def Text_2_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Message.mp3')
    playsound('Message.mp3')
    os.remove('Message.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

Button(root, text = "Play", font = 'arial 15 bold', command = Text_2_speech, width = '4').place(x = 50, y = 140)

Button(root, font = 'arial 15 bold', text = 'Quit', width = '4', command = Exit, bg = 'Orange').place(x = 125, y = 140)

Button(root, font = 'arial 15 bold', text = 'Reset', width = '6', command = Reset).place(x = 200, y = 140)

root.mainloop()