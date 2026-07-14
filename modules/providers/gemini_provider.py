from google import genai
from config import GEMINI_API_KEY
import time


client = genai.Client(
    api_key=GEMINI_API_KEY
)


MODELS = [
    "gemini-2.0-flash",
    "gemini-flash-latest",
    "gemini-2.0-flash-lite"
]


def generate_text(prompt):

    for model in MODELS:

        for attempt in range(2):

            try:

                print(
                    f"사용 모델 : {model}"
                )

                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                return response.text


            except Exception as e:

                print(
                    f"{model} 실패 {attempt+1}/2 : {e}"
                )

                time.sleep(3)


    return "AI 생성 서버가 현재 응답하지 않습니다."