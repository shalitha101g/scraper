I've updated the README template with your repository link:

---

# Web Scraper Tool

`scraper.py` is a Python-based tool for web scraping that fetches titles and links from `<h2>` tags on a specified web page. The scraped data is saved to a CSV file for easy access and analysis.

## Features

- Extracts article titles and links from web pages
- Saves the extracted data in a CSV file
- Simple and easy-to-use command-line interface

## Requirements

- Python 3.6+
- Required packages:
  - `requests`
  - `beautifulsoup4`

## Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/shalitha101g/scraper.git
   cd scraper
   ```

2. **Install the Required Packages**  
   Use the following command to install dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

1. Run the script with the command:
   ```bash
   python scraper.py
   ```

2. Enter the URL to scrape when prompted:
   ```plaintext
   Enter the URL to scrape: https://en.wikipedia.org/wiki/Emma_Watson
   ```

3. The script will then scrape all titles and links found in `<h2>` tags from the specified URL and save the data in `output.csv`.

### Example

```plaintext
$ python scraper.py
Enter the URL to scrape: https://en.wikipedia.org/wiki/Emma_Watson
Scraping data from https://en.wikipedia.org/wiki/Emma_Watson...
Data saved to output.csv
```

### Output

The CSV file (`output.csv`) will contain the following columns:
- **Title**: The text content of each `<h2>` tag
- **Link**: The hyperlink (`href`) if present, otherwise `None`

## File Structure

- **scraper.py**: The main Python script that performs the web scraping and data export to CSV.
- **output.csv**: The output file where scraped data is stored.
- **README.md**: Documentation for the project.

## Error Handling

If an error occurs while fetching the URL (e.g., network issues or an invalid URL), an error message will be displayed, and no data will be saved.

