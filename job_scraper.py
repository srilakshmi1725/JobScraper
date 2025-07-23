import requests
from bs4 import BeautifulSoup

def get_job_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h2')  # adjust based on the website structure
    for i, title in enumerate(titles, start=1):
        print(f"{i}. {title.text.strip()}")

# Example usage:
url = "https://realpython.github.io/fake-jobs/"
get_job_titles(url)
