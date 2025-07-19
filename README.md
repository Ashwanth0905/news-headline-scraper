 Task 3: Web Scraper for News Headlines

This is a simple Python project that scrapes top news headlines from the [Reuters](https://www.reuters.com/) website using the `requests` and `BeautifulSoup` libraries.

Objective
> Scrape the top news headlines from a public website and save them into a `.txt` file.

Tools Used
- **Python**
- **Requests**
- **BeautifulSoup**

Files Included
- `scraper.py` – Python script to scrape news headlines
- `headlines.txt` – Output file containing the scraped headlines
- `README.md` – Documentation for the project

Project Instructions
1. Use `requests` to fetch the HTML content of a webpage.
2. Parse the HTML using `BeautifulSoup`.
3. Extract headline tags (e.g., `<h2>` or `<h3>`) with relevant classes.
4. Write the extracted headlines to a `.txt` file.

Key Concepts
- HTTP requests and status codes
- Parsing HTML with BeautifulSoup
- Using User-Agent headers
- Writing to files in Python

How to Run This Script
1. Clone this repository or download the files.
2. Make sure you have `requests` and `beautifulsoup4` installed:
   ```bash

   TO RUN THE PROGRAM 
python scraper.py
   pip install requests beautifulsoup4
