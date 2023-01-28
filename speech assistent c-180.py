from tkinter import * 
import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import subprocess


root = Tk()
root.geometry("500x500")
root.configure(bg="#de9071")

label=Label(root,text="Hello I am Jarvis, your personal Desktop assistent",bg="#de9071",font=("Comic Sans ms",15,"bold"))
label.place(relx=0.5,rely=0.2,anchor=CENTER)

text_to_speech=pyttsx3.init()
def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()


def r_audio():
    speak("How can i help you..?")
    speech_recognisor = sr.Recognizer()
    with sr.Microphone() as source:
        audio= speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data= speech_recognisor.recognize_google(audio, language='en-in')
        except sr.UnknownValueError:
            print('please repeat i did not get that')
            speak("Please repeat I did not get that")
            
        respond(voice_data)
        
def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)
    if "name" in voice_data:
        speak("My name is Jarvis")
        print("my name is Jarvis")
        
    if "time" in voice_data:
        speak("Current Time is")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
        
    if "search" in voice_data:
        speak("Opening Google")
        print("Opening Google")
        webbrowser.get().open("https://www.google.com/")
        
    if "youtube" in voice_data:
        speak("Opening youtube")
        print("Opening youtube")
        webbrowser.get().open("https://www.youtube.com/")
        
    if "games" in voice_data:
        speak("Opening poki")
        print("Opening poki")
        webbrowser.get().open("https://poki.com/")
        
    if "notepad" in voice_data:
        speak("Opening Notepad")
        print("Opening Notepad")
        subprocess.Popen(["notepad.exe"])
        
    if "paint" in voice_data:
        speak("Opening ms paint")
        print("Opening Mspaint")
        subprocess.Popen(["mspaint.exe"])\
            
btn=Button(root, text="Activate",bg="red3", fg="white",padx=10,pady=1, font=("Arial",11, "bold"),relief=FLAT, command=r_audio)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
    



root.mainloop()
