from firecrawl import FirecrawlApp
import logging


def scrape_with_firecrawl(url):
    """
    Scrape the given URL using Firecrawl's current API specification
    """
    try:
        app = FirecrawlApp(api_key="fc-495d941e190240099174109675177727")

        # Current working API call (November 2023)
        scraped_data = app.scrape_url(url)

        # Try different content fields in priority order
        return (
                scraped_data.get('markdown') or
                scraped_data.get('html') or
                scraped_data.get('text') or
                ""
        )
    except Exception as e:
        logging.error(f"Scraping failed for {url}: {str(e)}")
        raise