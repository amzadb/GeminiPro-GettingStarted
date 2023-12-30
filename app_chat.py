import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
# print(chat)

response = chat.send_message("Whose slogan is 'I have a dream'?")
print(response.text)

response = chat.send_message("Who is this person? Tell me in 2-3 sentences.")
print(response.text)

print(chat.history)