import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

def scrape_google(sku: str):
    url = f"https://www.google.com/search?q={sku}"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for div in soup.select("div.g"):
        title = div.select_one("h3")
        link = div.select_one("a")

        if title and link:
            results.append({
                "title": title.get_text(),
                "url": link["href"]
            })

    return results
