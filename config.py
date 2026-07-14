from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_NAME = "AI Blogger Pro"

VERSION = "1.2.3"

# ======================
# BLOG PLATFORM
# ======================

BLOG_PLATFORM = "naver"

BLOG_STYLE = "information"

USE_SUMMARY_BOX = True

USE_TABLE = True

USE_FAQ = True

USE_CTA = True

# 사용할 AI
# 사용할 AI
AI_PROVIDER = "local"

LOCAL_MODEL = "qwen2.5:7b"
GEMINI_MODEL = "gemini-3.5-flash"

DEFAULT_TONE = "전문가"
DEFAULT_LENGTH = "2000자"
DEFAULT_MODE = "AEO"

DEFAULT_SCORE_THRESHOLD = 80

OUTPUT_PATH = "output/"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")