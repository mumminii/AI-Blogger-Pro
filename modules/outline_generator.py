def generate_outline(title, questions=None):

    outline = []


    if questions:

        outline.extend(questions)


    else:

        outline = [
            f"{title}란 무엇인가?",
            f"{title} 주요 특징",
            f"{title} 장점과 단점",
            f"{title} 사용 방법",
            f"{title} 관련 FAQ"
        ]


    return outline