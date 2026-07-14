from modules.providers.local_provider import generate_text


result = generate_text(
"""
탈모약에 대한 AEO 최적화 블로그 글 목차를 작성하세요.

조건:
- 한국 독자 대상
- 한국어만 사용
- 피나스테리드, 미녹시딜 등 한국식 명칭 사용
- AEO 구조 적용
"""
)


print(result)