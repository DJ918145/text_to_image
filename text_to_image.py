# Aim: Generating a image from text

from monsterapi import client
import requests
from PIL import Image

api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImU4OWQ5ZmJjZTdjNDgyNTQzYTIzOTMzNzE1OTZiYWY3IiwiY3JlYXRlZF9hdCI6IjIwMjUtMDQtMjdUMTI6NTA6MTAuMTQyMzIxIn0.yNpBiLxhO6TAZKSCAKSOF3OBVc_hWCriiV5JEGHjCsI'
monster_client = client(api_key)

model = 'txt2img' 

input_data = {
'prompt': 'detailed sketch of lion by greg rutkowski, beautiful, intricate, ultra realistic, elegant, art by artgerm',
'negprompt': 'deformed, bad anatomy, disfigured, poorly drawn face',
'samples': 1,
'steps': 50,
'aspect_ratio': 'square',
'guidance_scale': 7.5,
'seed': 2414,
            }

input_data['prompt'] = input("Enter the idea of image you want : ")

result = monster_client.generate(model, input_data)

img_url = result['output'][0]

file_name = "image.png"

response = requests.get(img_url)
if response.status_code == 200:
    with open(file_name, 'wb') as file:
        file.write(response.content)
        print("Image downloaded")

        img = Image.open(file_name)
        img.show()

else:
    print("Failed to download the image")
