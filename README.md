# Quotes Web Scraper & Data Analysis

## Introduction
This project is a Python-based web scraper and data analysis tool designed to extract quotes from a website, store them in a CSV file, and perform insightful queries and exploratory data analysis. The solution demonstrates how to automate web data extraction and leverage both SQL-like queries and Pandas for real-world data analysis.

## Project Type
Data Engineering | Exploratory Data Analysis

## Directory Structure

```
├─ scrapping_part.ipynb        
├─ cleaned_data.csv             
├─ quotes.csv                 
├─ EDA_part (2).ipynb          
├─ SQL_Insights.sql              
├─ README.md                    
```

## Features
- **Automated Web Scraping:** Uses requests and BeautifulSoup to extract author, quote, and tags from multiple pages.
- **Error Handling:** Robust try/except blocks to manage failed requests or parsing errors.
- **Multi-page Support:** Iterates through paginated site structure to collect comprehensive data.
- **CSV Export:** Stores all extracted data in a structured CSV file.
- **SQL Query Examples:** Includes common SQL queries for counting, grouping, filtering, and sorting the data.
- **Pandas EDA Script:** Loads CSV, displays basic info, previews data, counts unique authors, and computes descriptive statistics.

## Design Decisions & Assumptions
- Scraper limits to first 10 pages for demonstration but is structured to support full pagination.
- Assumes website structure remains consistent for HTML parsing.
- Data is saved in CSV format for wide compatibility and ease of analysis.
- Pandas and SQL queries are used to illustrate different analysis approaches.

## Installation & Getting Started
1. Clone the repository:
    ```bash
    git clone https://github.com/Ashish0016op/Quotes-Scraper-Data-Analysis.git
    cd Quotes-Scraper-Data-Analysis
    ```
2. Install dependencies:
    ```bash
    pip install requests beautifulsoup4 pandas
    ```
3. **Run the web scraper:**
    - Open `scrapping_part.ipynb` in Jupyter Notebook and run the cells to scrape and save quotes data.

4. **Clean the data:**
    - Use `EDA_part (2).ipynb` to load `quotes.csv`, clean, and export `cleaned_data.csv`.

5. **Analyze with SQL:**
    - Use the SQL queries in `SQL_Insights.sql` on `cleaned_data.csv` (can be imported into SQLite, MySQL, etc.)

## Usage

- Scrape quotes and save to CSV using the provided notebook.
- Clean and explore the data with EDA notebook.
- Run SQL queries for advanced insights.
- Visualize results in Jupyter or any preferred tool.

## Technology Stack
- Python
- requests (HTTP fetching)
- BeautifulSoup (HTML parsing)
- csv (data export)
- pandas (data analysis)
