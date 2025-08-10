# AI-Powered E-commerce Web Crawler

A specialized web crawler that extracts detailed product information from e-commerce sites using the crawl4ai framework and Groq's large language models.

## Overview

![Overview](WebScrap.mp4)

This project implements an intelligent web crawler that goes beyond traditional HTML scraping. It leverages AI to understand product listings on e-commerce websites and extract structured data, including:

- Product names and titles
- Pricing information
- Discount details
- Product ratings
- Categories
- Stock availability status
- Brief product descriptions

## Features

- **Intelligent Data Extraction**: Uses Groq's LLM models to understand and extract relevant product information
- **Structured Output**: All data is extracted into a well-defined schema
- **Pagination Support**: Can crawl through multiple pages of product listings
- **Duplicate Detection**: Avoids extracting duplicate products
- **Error Handling**: Manages rate limits and API errors gracefully
- **CSV Export**: Automatically saves extracted data to CSV for further analysis

## Prerequisites

- Python 3.x
- An API key from Groq (set as environment variable `GROQ_API_KEY`)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dharun36/webscraping-craw4ai.git

```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
```bash
# On Windows
set GROQ_API_KEY=your_api_key_here

# On macOS/Linux
export GROQ_API_KEY=your_api_key_here
```

## Usage

1. Configure the settings in `config.py` to specify the target URL and CSS selectors.

2. Run the main script:
```bash
python main.py
```

3. The extracted product data will be saved to `complete_venues.csv`.

## Project Structure

```
deepseek-ai-web-crawler/
├── config.py              # Configuration settings
├── main.py                # Main execution script
├── requirements.txt       # Project dependencies
├── complete_venues.csv    # Output file for extracted data
├── last_page.txt          # Tracks the last crawled page for resuming
├── models/
│   ├── __init__.py
│   └── venue.py           # Data model for product/venue information
└── utils/
    ├── __init__.py
    ├── data_utils.py      # Utilities for data handling
    └── scraper_utils.py   # Web scraping and LLM extraction logic
```

## Configuration

Edit `config.py` to customize:
- The target website URL
- CSS selectors for product elements
- Required fields for product data
- Maximum pages to crawl

## Handling Rate Limits

The crawler is designed to handle rate limits by:
1. Configuring appropriate token limits
2. Using smaller models when needed (e.g., llama3-8b-8192)
3. Implementing retry mechanisms with exponential backoff

## Future Improvements

- Add support for more e-commerce platforms
- Implement advanced filtering options
- Add sentiment analysis for product reviews
- Create a dashboard for visualizing extracted data

  

## Acknowledgments

- [crawl4ai](https://docs.crawl4ai.com/) framework for the core scraping functionality
- [Groq](https://groq.com/) for the LLM API used in data extraction
