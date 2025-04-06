import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.shl.com/solutions/products/product-catalog/"

def scrape_assessments():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.select("table tr")  # Table rows
    assessments = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 4:
            continue  # skip header or invalid rows

        try:
            name_tag = cols[0].find("a")
            if not name_tag:
                continue

            name = name_tag.text.strip()
            url = name_tag['href']
            remote = "Yes" if "✓" in cols[1].text else "No"
            adaptive = "Yes" if "✓" in cols[2].text else "No"
            test_type = cols[3].text.strip()

            assessments.append({
                "name": name,
                "url": url if url.startswith("http") else f"https://www.shl.com{url}",
                "remote_testing": remote,
                "adaptive_support": adaptive,
                "test_type": test_type
            })

        except Exception as e:
            continue  # ignore broken rows

    with open("data/assessments.json", "w") as f:
        json.dump(assessments, f, indent=2)

    print(f"Scraped {len(assessments)} assessments.")

if __name__ == "__main__":
    scrape_assessments()