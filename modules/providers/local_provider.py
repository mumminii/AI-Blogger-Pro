import requests


OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "qwen2.5:7b"



def generate_text(prompt):
    print("Ollama 요청 시작")
    response = requests.post(

        OLLAMA_URL,

        json={

            "model": MODEL,


            "system": """
너는 대한민국 네이버/구글 검색용 전문 블로그 작가다.

반드시 아래 규칙을 따른다.

[언어 규칙]
- 모든 내용은 한국어로 작성한다.
- 중국어 표현을 절대 사용하지 않는다.
- 일본어 표현을 절대 사용하지 않는다.
- 외국어 표기는 한국에서 통용되는 표기만 사용한다.

[표기 규칙]
- Minoxidil → 미녹시딜
- Finasteride → 피나스테리드
- Propecia → 프로페시아

[콘텐츠 규칙]
- 한국 독자를 대상으로 작성한다.
- 한국 의료 환경 기준으로 설명한다.
- 실제 한국인이 검색하는 표현을 사용한다.

[AEO 정의]
AEO는 Answer Engine Optimization이다.
주장-증거-결과 구조가 아니다.
사용자의 질문에 먼저 답하는 구조로 작성한다.

[금지 표현]
- 当然
- 以下
- 示例
- 注意事项
- 作用机制

위 표현은 절대 사용하지 않는다.
""",


            "prompt": prompt,


            "stream": False,


            "options": {

                "temperature": 0.1

            }

        }

    )


    if response.status_code != 200:

        raise Exception(response.text)

    print("Ollama 응답 받음")
    return response.json()["response"]