def generate_answer_blocks(questions):

    answers = []

    for q in questions:

        answer = {

            "question": q,

            "summary":
            f"{q}에 대한 핵심 답변입니다. "
            "정확한 정보를 확인하고 꾸준히 관리하는 것이 중요합니다.",


            "details":
            [
                "개인 상황에 따라 결과는 달라질 수 있습니다.",
                "신뢰할 수 있는 정보를 확인하는 것이 중요합니다.",
                "꾸준한 관리와 확인이 필요합니다."
            ]

        }

        answers.append(answer)


    return answers