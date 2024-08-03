# Description: This file contains the constants used in the blog package.
# Dependencies: dotenv, os
from dotenv import load_dotenv
import os

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# Constants
SECRET_KEY = os.getenv('SECRET_KEY')
GMAIL_ADDR = os.getenv('GMAIL_ADDRESS')
GMAIL_PASS = os.getenv('GMAIL_PASSWORD')
PERSONAL_EMAIL = os.getenv('PERSONAL_EMAIL')