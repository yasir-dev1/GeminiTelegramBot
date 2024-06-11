import os
import dotenv
import google.generativeai as genai
from PIL import Image

# Configure your API key
dotenv.load_dotenv()

# Get the Telegram bot token
api = os.getenv("API") 
genai.configure(api_key=api)

# Model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 10000,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings
)

def generate_content(prompt, image_path=None):
    if image_path:
        image = Image.open(image_path)
        response = model.generate_content([prompt, image])
    else:
        response = model.generate_content([prompt])
    return response.candidates[0].content.parts[0].text
