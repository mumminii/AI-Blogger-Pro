from config import AI_PROVIDER


from modules.providers.local_provider import generate_text as local_generate

from modules.providers.gemini_provider import generate_text as gemini_generate

from modules.providers.openai_provider import generate_text as openai_generate



def generate_ai_text(prompt):


    if AI_PROVIDER == "local":

        return local_generate(prompt)


    elif AI_PROVIDER == "gemini":

        return gemini_generate(prompt)


    elif AI_PROVIDER == "openai":

        return openai_generate(prompt)


    else:

        return "지원하지 않는 AI Provider입니다."