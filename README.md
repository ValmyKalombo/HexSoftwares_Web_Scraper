# HexSoftwares Web Scraper

## Overview
This project contains Python scripts for web scraping. It demonstrates how to extract data from websites and save it in a structured format like CSV, as well as display it neatly in the terminal.

The project includes scrapers for:  
1. **Quotes** – Scrapes quotes and their authors from [Quotes to Scrape](http://quotes.toscrape.com).  
2. **Job Listings** – Scrapes job titles, companies, and locations from a fake jobs website ([Real Python Fake Jobs](https://realpython.github.io/fake-jobs/)).

## Features
- Extracts relevant data from websites using `BeautifulSoup`.
- Saves scraped data to CSV files in an `outputs/` folder.
- Prints data neatly on the terminal.
- UTF-8 encoding ensures proper formatting of characters.
- Handles folder creation automatically to avoid errors.

## Project Structure
HexSoftwares_Web_Scraper/
│
├─ outputs/ # CSV files generated after scraping
│
├─ quotes_scraper.py # Scrapes quotes and authors
├─ jobs_scraper.py # Scrapes job listings
├─ requirements.txt # Dependencies (e.g., beautifulsoup4, requests, lxml)
├─ README.md # Project documentation
├─ .gitignore # Ignores pycache/ and other unnecessary files
