import os

from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv('SECRET')
print(secret_key)
