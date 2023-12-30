import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Using gemini-pro-vision model for text and image prompts
model = genai.GenerativeModel('gemini-pro-vision')
# print(model)

import PIL.Image
img = PIL.Image.open("./images/dog-boy-ball.jpg")
# print(img)

# response = model.generate_content(img)
# print(response.text)

# img = PIL.Image.open("./images/food-items.jpg")
# response = model.generate_content(["Generate a json of items from the picture",img])
# print(response.text)

# img = PIL.Image.open("./images/Social-Test.jpg")
# response = model.generate_content(["Please answer question 3 of section B",img])
# print(response.text)

img = PIL.Image.open("./images/spartan1.jpg")
response = model.generate_content(["Prepare a blog about the picture given",img], stream=True)
response.resolve()
print(response.text)

