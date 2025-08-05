import requests
from bs4 import BeautifulSoup
import urllib.parse

def fetch_linkedin_jobs(query):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.linkedin.com/jobs/search/?keywords={encoded_query}&location=India"

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        job_cards = soup.find_all("div", class_="base-card")

        jobs = []
        for card in job_cards[:5]:  # limit to top 5
            title = card.find("h3").text.strip()
            company = card.find("h4").text.strip()
            link = card.find("a", href=True)["href"]
            jobs.append({"title": title, "company": company, "link": link})
        return jobs

    except Exception as e:
        return [{"title": "LinkedIn fetch failed", "company": str(e), "link": ""}]

def fetch_naukri_jobs(query):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.naukri.com/{encoded_query}-jobs-in-india"

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        job_cards = soup.find_all("article", class_="jobTuple")

        jobs = []
        for card in job_cards[:5]:  # limit to top 5
            title = card.find("a", class_="title").text.strip()
            company = card.find("a", class_="subTitle").text.strip()
            link = card.find("a", class_="title")["href"]
            jobs.append({"title": title, "company": company, "link": link})
        return jobs

    except Exception as e:
        return [{"title": "Naukri fetch failed", "company": str(e), "link": ""}]
