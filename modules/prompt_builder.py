from config import BLOG_PLATFORM


def build_naver_prompt(
    title,
    outline,
    answers,
    faq,
    tone,
    length,
    mode
):

    prompt = f"""
당신은 네이버 블로그를 10년 이상 운영한 콘텐츠 마케터입니다.

- AI 말투 금지
- 사람처럼 작성
- 문단은 2~3줄
- 모바일 최적화
- 첫 문단에서 궁금증 해결
- 과장 금지
- 경험담처럼 작성
- 자연스러운 연결
- 마지막 요약
- FAQ
- 댓글을 유도하는 마무리

반드시 아래 순서대로 작성하세요.

1. 도입부
2. 핵심 요약
3. 본문
4. 표
5. 결론
6. FAQ
7. 댓글 유도

당신은 대한민국의 전문 콘텐츠 에디터이며,
AEO(Answer Engine Optimization)에 최적화된 블로그 작성 전문가입니다.

# 제목
{title}

# 작성 모드
{mode}

# 문체
{tone}

# 글 길이
{length}

# 목차
{outline}

# AEO 핵심 답변
{answers}

# FAQ
{faq}

# 작성 규칙

- 블로그를 처음부터 끝까지 하나의 글처럼 작성
- 질문 제목을 그대로 반복하지 않는다.
- Answer Block은 참고만 하고 자연스럽게 재작성한다.
- FAQ는 마지막에만 작성한다.
- 같은 표현을 반복하지 않는다.
- AI 말투 금지
- 반드시 한국어만 사용
- H2/H3 제목 사용
- 표(Table)를 적극 활용
- 자연스럽게 이어지는 글 작성

지금부터 완성된 블로그를 작성하세요.
"""

    return prompt


def build_blog_prompt(
    title,
    outline,
    answers,
    faq,
    tone="전문가",
    length="2000자",
    mode="AEO"
):

    if BLOG_PLATFORM == "naver":

        return build_naver_prompt(
            title,
            outline,
            answers,
            faq,
            tone,
            length,
            mode
        )

    raise ValueError(f"지원하지 않는 플랫폼 : {BLOG_PLATFORM}")