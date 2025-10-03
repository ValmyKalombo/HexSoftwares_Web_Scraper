import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "lxml")
    quotes_cards = soup.find_all("div", class_="quote")

    quotes_data = []

    for idx, quote in enumerate(quotes_cards, start=1):
        text = quote.find("span", class_="text").get_text(strip=True)
        author = quote.find("small", class_="author").get_text(strip=True)

        # Add to list for CSV
        quotes_data.append([text, author])

        # Print neatly
        print(f"\nQuote {idx}:")
        print(f"“{text}”")
        print(f"— {author}")
        print("-" * 80)

    # Save to CSV
    with open("outputs/quotes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Quote", "Author"])
        writer.writerows(quotes_data)

    print("\nQuotes saved to quotes.csv")

if __name__ == "__main__":
    scrape_quotes()