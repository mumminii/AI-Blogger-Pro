def remove_ai_phrases(text):

    replacements = {
        "정확한 정보를 확인하세요.": "",
        "상황에 맞게 판단하는 것이 중요합니다.": "",
        "개인의 상황에 따라 달라질 수 있습니다.": "",
        "AI가 작성": "",
        "물론입니다.": "",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def improve_connectors(text):

    replacements = {
        "또한": "그리고",
        "따라서": "그래서",
        "그러므로": "결국",
        "한편": "반면",
        "즉": "쉽게 말하면",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def split_long_paragraphs(text):

    connectors = [
        "하지만",
        "반면",
        "그리고",
        "또한",
        "특히",
        "예를 들어",
        "즉",
        "다만",
        "따라서",
        "그래서",
        "결국",
    ]

    for word in connectors:
        text = text.replace(f" {word}", f"\n\n{word}")

    return text


def add_mobile_spacing(text):
    return text


def humanize_blog(text):

    text = remove_ai_phrases(text)
    text = improve_connectors(text)
    text = split_long_paragraphs(text)
    text = add_mobile_spacing(text)

    return text