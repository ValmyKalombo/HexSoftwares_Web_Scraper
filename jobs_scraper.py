import requests
from bs4 import BeautifulSoup
import csv
import os

def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "lxml")
    job_cards = soup.find_all("div", class_="card-content")

    # Ensure outputs folder exists
    os.makedirs("outputs", exist_ok=True)

    jobs_data = []

    for idx, job in enumerate(job_cards, start=1):
        title = job.find("h2", class_="title").get_text(strip=True)
        company = job.find("h3", class_="company").get_text(strip=True)
        location = job.find("p", class_="location").get_text(strip=True)

        # Add to list for CSV
        jobs_data.append([title, company, location])

        # Print neatly
        print(f"\nJob {idx}:")
        print(f"Title   : {title}")
        print(f"Company : {company}")
        print(f"Location: {location}")
        print("-" * 60)

    # Save to CSV
    with open("outputs/jobs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Job Title", "Company", "Location"])
        writer.writerows(jobs_data)

    print("\n✅ Jobs saved to outputs/jobs.csv")

if __name__ == "__main__":
    scrape_jobs()
