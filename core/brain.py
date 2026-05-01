import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure the API
genai.configure(api_key=api_key)

# System prompt
system_prompt = "You are SIASTA, a highly advanced, loyal AI created to assist your user, Tushar. You are polite, highly intelligent, and speak with a refined British-style cadence. Keep responses very concise (1-2 sentences). You are multi-modal: you will receive text and sometimes an image from the webcam. If an image is provided, analyze it as if you are looking out into the real world. Act natively."
model = genai.GenerativeModel('gemini-1.5-pro', system_instruction=system_prompt)

def get_response(user_text, image_path=None):
    content = [user_text]
    if image_path:
        with Image.open(image_path) as image:
            content.append(image.copy())

    response = model.generate_content(content)
    return response.text

if __name__ == "__main__":
    # Example usage
    response = get_response("Hello SIASTA", "path/to/image.jpg")
    print(response)
