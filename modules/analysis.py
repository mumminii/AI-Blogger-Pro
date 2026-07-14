def analyze_keyword(keyword, score):

    # 검색 의도
    if any(x in keyword for x in ["가격", "추천", "비교"]):
        intent = "💰 구매"

    elif any(x in keyword for x in ["후기", "사용", "효과"]):
        intent = "📝 정보 탐색"

    else:
        intent = "🔍 일반 검색"

    # 경쟁도
    if score >= 80:
        competition = "★★☆☆☆"

    elif score >= 60:
        competition = "★★★☆☆"

    else:
        competition = "★★★★☆"

    # 추천 이유

    reasons = []

    if "추천" in keyword:
        reasons.append("추천 키워드는 클릭률이 높습니다.")

    if "가격" in keyword:
        reasons.append("가격 검색은 구매 전환율이 높습니다.")

    if "후기" in keyword:
        reasons.append("후기 키워드는 체류시간이 길어집니다.")

    if "부작용" in keyword:
        reasons.append("부작용은 정보성 트래픽 확보에 좋습니다.")

    if len(reasons) == 0:
        reasons.append("일반 정보성 키워드입니다.")

    return intent, competition, reasons