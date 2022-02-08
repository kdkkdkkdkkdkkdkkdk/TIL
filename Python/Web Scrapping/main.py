import requests
# pip install requests
from bs4 import BeautifulSoup
# pip install beautifulsoup4

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text, "html.psarser")
pagination = indeed_soup.find("div", {"class": "pagination"})
pages = pagination.find_all('a')

print(pages)
