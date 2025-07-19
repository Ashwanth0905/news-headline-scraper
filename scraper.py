import requests
from bs4 import BeautifulSoup

# Step 1: Fetch HTML content
url = "https://www.reuters.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise error for bad responses
except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
    exit()

# Step 2: Parse HTML and extract headlines
soup = BeautifulSoup(response.text, "html.parser")

# Generic method to capture all <h3> elements
headline_tags = soup.find_all("h3")

# Step 3: Save headlines to a text file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for index, tag in enumerate(headline_tags, 1):
        text = tag.get_text(strip=True)
        if text:
            file.write(f"{index}. {text}\n")

print("✅ Successfully saved headlines to headlines.txt")
