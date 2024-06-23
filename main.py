import subprocess
import pyttsx3

import speech_recognition as sr
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Nghe...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Đang nhận diện...")
        text = recognizer.recognize_google(audio, language="vi_VN")
        return text.lower()
    except sr.UnknownValueError:
        return listen()
    except sr.RequestError as e:
        return f"Lỗi kết nối: {e}"

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    
def get_response():
    subprocess.run(['312_venv/Scripts/python.exe', 'get_response.py'])

speak("Xin chào, tôi là chatbot! Hãy hỏi tôi bất cứ điều gì bạn cần, và nói goodbye để dừng lại.")
while True:
    command = listen()
    with open('i_o/input.txt', 'w', encoding='utf-8') as file:
        file.write(command)
    print("Bạn nói: ", command)
    if "goodbye" in command:
        speak("Good bye! See you later.")
        break
    else:
        get_response()
        with open('i_o/output.txt', 'r', encoding='utf-8') as file:
            response = file.read()
        print("Chatbot: " + response)
        speak(response)
        