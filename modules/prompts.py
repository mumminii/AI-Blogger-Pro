def blog_prompt(keyword, tone, length):

    return f"""
당신은 네이버 SEO 전문가입니다.

다음 키워드로 블로그 글을 작성하세요.

키워드 : {keyword}

조건

- {tone} 스타일

- {length}

- 제목

- 목차

- 본문

- FAQ

- 태그 10개

- 사람처럼 자연스럽게 작성
"""