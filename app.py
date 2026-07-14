import streamlit as st

from config import PROJECT_NAME, VERSION

from modules.trending import get_trending_keywords
from modules.analysis import analyze_keyword
from modules.keyword import get_related_keywords
from modules.score import score_keyword
from modules.title_generator import generate_titles
from modules.outline_generator import generate_outline
from modules.blog_writer import generate_blog
from modules.exporter import save_markdown
from modules.question_generator import generate_questions
from modules.faq_generator import generate_faq
from modules.answer_generator import generate_answer_blocks
from modules.post_processor import process_blog
from modules.seo_analyzer import analyze_seo

st.set_page_config(
    page_title=PROJECT_NAME
)


if "keyword" not in st.session_state:
    st.session_state.keyword = ""

if "titles" not in st.session_state:
    st.session_state.titles = []

if "selected_title" not in st.session_state:
    st.session_state.selected_title = ""

if "outline" not in st.session_state:
    st.session_state.outline = []

if "blog" not in st.session_state:
    st.session_state.blog = ""

if "questions" not in st.session_state:
    st.session_state.questions = []

if "faq" not in st.session_state:
    st.session_state.faq = []

if "answer_blocks" not in st.session_state:
    st.session_state.answer_blocks = []

st.title(
    f"🤖 {PROJECT_NAME} v{VERSION}"
)


st.write("### AI 키워드 추천 시스템")


# ==========================
# 오늘의 추천 키워드
# ==========================

st.subheader("🔥 오늘의 추천 키워드")

trending = get_trending_keywords()

cols = st.columns(2)


for i, word in enumerate(trending):

    with cols[i % 2]:

        if st.button(
            word,
            key=f"trend_{i}"
        ):

            st.session_state.keyword = word



# ==========================
# 키워드 입력
# ==========================

keyword = st.text_input(
    "키워드를 입력하세요",
    value=st.session_state.keyword
)



if st.button(
    "키워드 추천",
    key="keyword_search"
):

    if keyword == "":

        st.warning(
            "키워드를 입력해주세요."
        )

    else:

        keywords = get_related_keywords(keyword)

        st.subheader("추천 키워드")


        for k in keywords:

            score = score_keyword(k)


            if score >= 80:
                icon = "🟢"

            elif score >= 60:
                icon = "🟡"

            else:
                icon = "🔴"


            intent, competition, reasons = analyze_keyword(
                k,
                score
            )


            with st.expander(
                f"{icon} {score}점 | {k}"
            ):

                st.write(
                    f"### 🔍 검색 의도 : {intent}"
                )

                st.write(
                    f"### ⚔ 경쟁도 : {competition}"
                )

                st.write(
                    "### 📌 추천 이유"
                )


                for r in reasons:
                    st.write(
                        "✔",
                        r
                    )



# ==========================
# SEO 제목 생성
# ==========================

st.divider()

st.subheader(
    "🔥 SEO 제목 생성"
)


if st.button(
    "제목 생성",
    key="generate_title"
):

    if keyword == "":

        st.warning(
            "먼저 키워드를 입력해주세요."
        )

    else:

        st.session_state.titles = generate_titles(keyword)



if st.session_state.titles:

    st.session_state.selected_title = st.selectbox(
        "작성할 제목을 선택하세요",
        st.session_state.titles
    )

# ==========================
# SEO 목차 생성
# ==========================

st.divider()

st.subheader(
    "📑 SEO 목차 생성"
)


if st.button(
    "목차 생성",
    key="generate_outline"
):

    if st.session_state.selected_title == "":

        st.warning(
            "먼저 제목을 선택해주세요."
        )

    else:

        st.session_state.outline = generate_outline(
            st.session_state.selected_title,
            st.session_state.questions
        )

        for i, item in enumerate(st.session_state.outline):

            st.write(
                f"{i+1}. {item}"
            )

# ==========================
# AEO 질문 생성
# ==========================

st.divider()

st.subheader(
    "❓ AEO 질문 생성"
)


if st.button(
    "질문 생성",
    key="generate_questions"
):

    if keyword == "":

        st.warning(
            "먼저 키워드를 입력해주세요."
        )

    else:

        st.session_state.questions = generate_questions(
            keyword
        )


if st.session_state.questions:

    for i, q in enumerate(
        st.session_state.questions
    ):

        st.write(
            f"{i+1}. {q}"
        )

# ==========================
# AEO FAQ 생성
# ==========================

st.divider()

st.subheader(
    "❓ AEO FAQ 생성"
)


if st.button(
    "FAQ 생성",
    key="generate_faq"
):

    st.session_state.faq = generate_faq(
        st.session_state.questions
    )


if st.session_state.faq:

    for item in st.session_state.faq:

        st.write(
            f"### Q. {item['question']}"
        )

        st.write(
            f"A. {item['answer']}"
        )



st.divider()

st.subheader(
    "💡 AEO Answer Block 생성"
)


if st.button(
    "답변 블록 생성",
    key="generate_answer_blocks"
):

    if not st.session_state.questions:

        st.warning(
            "먼저 질문을 생성해주세요."
        )

    else:

        st.session_state.answer_blocks = generate_answer_blocks(
            st.session_state.questions
        )

# ==========================
# AEO Answer Block 생성
# ==========================

if st.session_state.answer_blocks:

    for item in st.session_state.answer_blocks:


        st.write(
            f"## ❓ {item['question']}"
        )


        st.write(
            "### 💡 핵심 답변"
        )

        st.write(
            item["summary"]
        )


        st.write(
            "### 📌 핵심 포인트"
        )


        for detail in item["details"]:

            st.write(
                "✔",
                detail
            )

# ==========================
# AI 블로그 본문 생성
# ==========================

st.divider()

st.subheader(
    "✍️ AI 블로그 작성"
)


if st.button(
    "본문 생성",
    key="generate_blog"
):

    if not st.session_state.outline:

        st.warning(
            "먼저 목차를 생성해주세요."
        )

    else:

        raw_blog = generate_blog(
            st.session_state.selected_title,
            st.session_state.outline,
            st.session_state.answer_blocks,
            st.session_state.faq
        )


        st.session_state.blog = process_blog(
            raw_blog
        )


if st.session_state.blog:

    st.markdown(
        st.session_state.blog
    )

if st.session_state.blog:

    result = analyze_seo(

        st.session_state.blog,

        keyword

    )

    st.divider()

    st.subheader("📈 SEO 분석")

    st.metric(

        "SEO 점수",

        f"{result['score']}점"

    )

    for r in result["reasons"]:

        st.write("✔", r)

## ==========================
# 파일 저장
# ==========================

st.divider()

st.subheader(
    "💾 파일 저장"
)


if st.button(
    "Markdown 저장",
    key="save_markdown"
):

    if st.session_state.blog == "":

        st.warning(
            "먼저 본문을 생성해주세요."
        )

    else:

        file_path = save_markdown(
            st.session_state.blog,
            st.session_state.selected_title
        )

        st.success(
            f"저장 완료: {file_path}"
        )