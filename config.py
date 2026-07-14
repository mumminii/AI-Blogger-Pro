from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_NAME = "AI Blogger Pro"

VERSION = "1.2.3"

# 사용할 AI
AI_PROVIDER = "local"
AI_MODEL = "gemini-3.5-flash"

DEFAULT_TONE = "전문가"
DEFAULT_LENGTH = "2000자"
DEFAULT_MODE = "AEO"

DEFAULT_SCORE_THRESHOLD = 80

OUTPUT_PATH = "output/"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")