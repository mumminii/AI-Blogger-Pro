from modules.providers.gemini_provider import generate_text


result = generate_text(
    "안녕하세요. 자기소개를 3줄로 해주세요."
)

print(result)