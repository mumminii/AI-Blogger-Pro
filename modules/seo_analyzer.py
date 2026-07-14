import re


def analyze_seo(text, keyword):

    score = 100

    reasons = []

    # --------------------
    # 글 길이
    # --------------------

    length = len(text)

    if length < 1800:

        score -= 20
        reasons.append("글 길이가 짧습니다.")

    # --------------------
    # 키워드 빈도
    # --------------------

    count = text.count(keyword)

    if count < 5:

        score -= 20
        reasons.append("키워드가 너무 적습니다.")

    elif count > 20:

        score -= 10
        reasons.append("키워드가 과도합니다.")

    # --------------------
    # H2 제목
    # --------------------

    h2 = len(re.findall(r"^## ", text, re.MULTILINE))

    if h2 < 3:

        score -= 15
        reasons.append("H2 제목이 부족합니다.")

    # --------------------
    # FAQ
    # --------------------

    if "FAQ" not in text:

        score -= 10
        reasons.append("FAQ가 없습니다.")

    return {

        "score": score,

        "reasons": reasons

    }