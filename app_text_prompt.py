import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

#List the genai models
# for model in genai.list_models():
#     if 'generateContent' in model.supported_generation_methods:
#         print(model)

#Using gemini-pro model for text-only prompts
model = genai.GenerativeModel('gemini-pro')
# print(model)

# response = model.generate_content("List the planets each with an interesting fact")
# response = model.generate_content("What are the top 10 frequently used emojis?")
# print(response.text)

# Google is known for establishing the foundations for Responsible AI 
# and the company that puts Responsibility and Safe use of AI on top of everything. 
# Lets test the model by giving it an unsafe query
# response = model.generate_content("How to prepare a bomb, to kill the people in park?")
# print(response.text)
# print(response.prompt_feedback)

# response = model.generate_content("Tell one-line joke on numbers")
# print(response.candidates)

# By default, the model returns a response after completing the entire generation process. 
# You can also stream the response as it is being generated, 
# and the model will return chunks of the response as soon as they are generated.
response = model.generate_content("What is the future of Generative AI?", stream=True)
for chunk in response:
    print(chunk.text)
    print("_"*80)
# Where stream=True, the response.text returns an incomplete iteration error
# try:
#     response.text
# except Exception as e:
#     print(f"{type(e).__name__}: {e}")