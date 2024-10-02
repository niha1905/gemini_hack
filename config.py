import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    GOOGLE_AI_API_KEY = os.getenv('GOOGLE_AI_API_KEY')
