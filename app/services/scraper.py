import requests
from bs4 import BeautifulSoup

def scrape_google(sku: str):
    url = f"https://www.google.com/search?q={sku}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for result in soup.select("div.g"):
        title = result.select_one("h3")
        link = result.select_one("a")

        if title and link:
            results.append({
                "title": title.get_text(),
                "url": link.get("href")
            })

    return results
