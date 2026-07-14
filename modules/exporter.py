import os


def save_markdown(blog, title):

    os.makedirs(
        "output",
        exist_ok=True
    )

    filename = f"output/{title}.md"

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(blog)

    return filename