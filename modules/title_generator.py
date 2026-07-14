def generate_titles(keyword):

    templates = [

        "{} 추천 TOP10",
        "{} 완벽 정리",
        "{} 가격 비교 총정리",
        "{} 효과와 부작용 알아보기",
        "{} 실제 후기 및 경험담",
        "{} 선택 기준 완벽 가이드",
        "{} 처음 시작하는 사람을 위한 정보",
        "{} 장점과 단점 비교",
        "{} 꼭 알아야 할 핵심 정보",
        "{} 전문가가 알려주는 {}",

        "2026 {} 추천 가이드",
        "2026 {} 최신 정보 총정리",
        "{} 구매 전 반드시 확인해야 할 내용",
        "{} 비용과 유지 관리 방법",
        "{} 실패하지 않는 선택 방법",
        "{}에 대한 모든 것",
        "{} 사용 전 알아야 하는 주의사항",
        "{} 비교 분석",
        "{} FAQ 총정리",
        "{} 초보자를 위한 완벽 가이드"

    ]


    titles = []

    for template in templates:

        if template.count("{}") == 2:

            title = template.format(
                keyword,
                keyword
            )

        else:

            title = template.format(
                keyword
            )


        titles.append(title)


    return titles