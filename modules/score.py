def score_keyword(keyword):

    score = 50

    # 키워드 길이
    if len(keyword) >= 4:
        score += 10

    # 사람들이 많이 찾는 형태
    good_words = [
        "추천",
        "가격",
        "후기",
        "비교",
        "효과",
        "사용법",
        "부작용",
        "정리"
    ]

    for word in good_words:
        if word in keyword:
            score += 10

    return min(score, 100)