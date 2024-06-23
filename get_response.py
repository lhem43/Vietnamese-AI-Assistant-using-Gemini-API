import os
import google.generativeai
google.generativeai.configure(api_key="AIzaSyBGwLOriTuP6LTS4rjdDYpANDkPv3THzSo")

generation_config = {
    "temperature" : 1,
    "top_p" : 0.95,
    "top_k" : 64,
    "max_output_tokens" : 8192,
    "response_mime_type" : "text/plain"
}

model = google.generativeai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config= generation_config,
)

chat_session = model.start_chat(
    history=[
        
    ]
)

with open('i_o/input.txt', 'r', encoding='utf-8') as file:
    inputString = file.read()
    
response = chat_session.send_message(inputString)

with open('i_o/output.txt', 'w', encoding='utf-8') as file:
    file.write(response.text)
    
