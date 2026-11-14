
import requests
from bs4 import BeautifulSoup

url = "https://www.pewresearch.org/global/2026/09/17/globally-more-people-expect-ai-to-cause-job-loss-than-growth/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=15)

print("Status Code:", response.status_code)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract article title
    title = soup.find("h1")

    if title:
        print("\nARTICLE TITLE:")
        print(title.get_text(strip=True))

    # Extract article headings
    print("\nARTICLE HEADINGS:")

    for heading in soup.find_all(["h2", "h3"]):
        print(heading.get_text(strip=True))

    # Extract article paragraphs
    print("\nARTICLE PARAGRAPHS:")

    main_content = soup.find("main")

    if main_content:
        for paragraph in main_content.find_all("p"):
            text = paragraph.get_text(" ", strip=True)

            if text:
                print(text)

else:
    print("Failed to retrieve website.")
