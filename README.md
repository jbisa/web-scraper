# Web Scraper

The `WebScraper.py` script can be used to hit a URL (configurable in the script), grab the HTML contents on the page using `BeautifulSoup` and then parsing the contents for data points that you care about. The data is then written into a CSV file for analysis and data storage purposes.

## Dependencies

- Python 3.*
- bs4 (`BeautifulSoup`)

## How to Run This Program

First, start the virtual environment from the project root directory:

```
source web-scraper-venv/bin/activate
```

Next, run the script:

```
python3 WebScraper.py
```