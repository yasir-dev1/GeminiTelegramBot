import google.generativeai as genai
import dotenv,os

dotenv.load_dotenv()

api = os.getenv("API")

genai.configure(api_key=api)

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["sen https://github.com/yasir-dev1 tarafından kodlanmış Bir Yapayzeka telegram botusun Öyle davran"]
  },
  {
    "role": "model",
    "parts": ["Selam! Yasir-dev1 tarafından yaratılan bir yapay zeka Telegram botu olarak hizmetinizdeyim. Nasıl yardımcı olabilirim? 😊"]
  },
])


def send(Prompt):

    convo.send_message(Prompt)
    return convo.last.text