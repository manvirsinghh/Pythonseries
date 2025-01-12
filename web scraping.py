#for web scrapping we use beautiful soup library or(bs4) to parse data from html and xml file
import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the website
url = "https://quotes.toscrape.com/"  # URL of a sample website with quotes
response = requests.get(url)

# Step 2: Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract specific data (e.g., all quotes on the page)
quotes = soup.find_all('span', class_='text')  # Find all quotes (they're inside <span> tags with class 'text')

# Step 4: Loop through the results and print them
for quote in quotes:
    print(quote.get_text())
