from modules.ai_engine import generate_ai_text


def improve_blog(blog, report):

    prompt = f"""
다음 블로그를 개선해주세요.

[SEO 평가]
{report}

규칙

- 부족한 부분만 수정
- 좋은 부분은 유지
- 글을 처음부터 새로 쓰지 말 것
- 한국어만 사용
- AI 말투 금지
- 자연스럽게 수정

블로그

{blog}
"""

    return generate_ai_text(prompt)