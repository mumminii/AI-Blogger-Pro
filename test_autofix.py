from modules.autofix import improve_blog

blog = """
탈모약은 탈모 치료에 사용됩니다.
"""

report = """
글 길이가 짧습니다.
FAQ가 없습니다.
"""

print(improve_blog(blog, report))