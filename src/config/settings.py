import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Model Configuration
GEMINI_MODEL = "gemini-1.5-pro"
TEMPERATURE = 0.7
TOP_P = 0.9
TOP_K = 40
MAX_OUTPUT_TOKENS = 2048

# Session Configuration
SESSION_TIMEOUT = 3600  # 1 hour

# Candidate Information Schema
REQUIRED_FIELDS = [
    "full_name",
    "email",
    "phone",
    "experience",
    "desired_position",
    "location",
    "tech_stack"
] 