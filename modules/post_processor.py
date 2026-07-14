import re


def clean_language(text):

    """
    언어 혼합 제거
    """

    replacements = {

        "미诺地尔": "미녹시딜",
        "Minoxidil": "미녹시딜",

        "Finasteride": "피나스테리드",

        "Propecia": "프로페시아",

        "脱发": "탈모",

        "药物": "약물",

        "当然": "",
        "以下": "",
        "示例": "",

    }


    for old, new in replacements.items():

        text = text.replace(
            old,
            new
        )


    return text



def remove_ai_expression(text):

    """
    AI 느낌 제거
    """

    patterns = [

        "물론입니다.",
        "도움이 되셨길 바랍니다.",
        "필요하시면 추가로",
        "제가 작성해드리겠습니다.",
        "아래는"

    ]


    for p in patterns:

        text = text.replace(
            p,
            ""
        )


    return text



def normalize_markdown(text):

    """
    Markdown 정리
    """

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text
    )


    return text



def process_blog(text):

    """
    전체 후처리
    """

    text = clean_language(text)

    text = remove_ai_expression(text)

    text = normalize_markdown(text)


    return text