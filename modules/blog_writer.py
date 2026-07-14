from modules.prompt_builder import build_blog_prompt
from modules.ai_engine import generate_ai_text


def generate_blog(
    title,
    outline,
    answers,
    faq
):

    prompt = build_blog_prompt(
        title,
        outline,
        answers,
        faq
    )

    result = generate_ai_text(
        prompt
    )

    return result