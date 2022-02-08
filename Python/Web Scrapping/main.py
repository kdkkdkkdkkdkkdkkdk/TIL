import requests
# python -m pip install requests
from bs4 import BeautifulSoup
# python -m pip install beautifulsoup4

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
pagination = indeed_soup.find("div", {"class": "pagination"})
pages = pagination.find_all('a')

spans = []
for page in pages:
    spans.append(page.find("span"))

print(spans[:-1])
