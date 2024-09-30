from openai import OpenAI
import os
import base64

# OpenAI API Key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  
# Path to your image
image_path = "img.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image? Answer with the single word."},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}",
            "detail": "low"
          },
        },
      ],
    }
  ],
  max_tokens=100,
)
# print(response)
print(response.choices[0].message.content)