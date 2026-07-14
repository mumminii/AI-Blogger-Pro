def generate_faq(questions):

    faq = []

    for q in questions:

        item = {
            "question": q,
            "answer": f"{q}에 대한 답변입니다. 정확한 정보를 확인하고 상황에 맞게 판단하는 것이 중요합니다."
        }

        faq.append(item)

    return faq