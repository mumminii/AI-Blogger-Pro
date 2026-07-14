import requests


def get_related_keywords(keyword):

    url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={keyword}"

    response = requests.get(url)

    data = response.json()

    return data[1]