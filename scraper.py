import requests
from bs4 import BeautifulSoup
import csv
import time

# Function to scrape data from a given URL
def scrape_website(url):
    try:
        # Fetch the web page
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request fails

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Extract all article titles and links
        articles = []
        for article in soup.find_all('h2'):  # Adjust this according to your target website's structure
            title = article.text.strip()
            link_tag = article.find('a')
            # Only add if there is an <a> tag
            if link_tag and 'href' in link_tag.attrs:
                link = link_tag['href']
                articles.append((title, link))
            else:
                articles.append((title, None))

        return articles

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return None

# Function to save data into a CSV file
def save_to_csv(data, filename="output.csv"):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Link'])  # Writing headers
        writer.writerows(data)  # Writing the data rows
    print(f"Data saved to {filename}")

# Main automation function
def main():
    # Input URL from the user
    url = input("Enter the URL to scrape: ")

    # Perform scraping
    print(f"Scraping data from {url}...")
    scraped_data = scrape_website(url)

    if scraped_data:
        # Saving to CSV
        save_to_csv(scraped_data)
    else:
        print("No data scraped.")

# Entry point
if __name__ == '__main__':
    main()
