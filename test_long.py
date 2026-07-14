from modules.ai_engine import generate_ai_text


prompt = """
탈모약에 대한 블로그 글을 작성해주세요.

조건:
- 2000자
- Markdown
- H2/H3 사용
- FAQ 포함
- AEO 최적화
"""

result = generate_ai_text(prompt)

print(result)