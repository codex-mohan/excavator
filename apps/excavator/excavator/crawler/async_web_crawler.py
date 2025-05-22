import asyncio
from .config.aysnc_config import AysncCrawlerConfig, BrowserConfig
from .browser_manager import BrowserManager

from markdownify import markdownify as md

import aiohttp
from bs4 import BeautifulSoup

class AsyncWebCrawler:
    def __init__(self, config: AysncCrawlerConfig):
        self.config = config
        self.browser_manager = None

    async def init(self):
        """Asynchronously initializes the crawler resources."""
        if self.config.crawler_mode == "browser" and self.config.browser_config:
            # Initialize BrowserManager if in browser mode and config is provided
            self.browser_manager = BrowserManager(self.config.browser_config)
            await self.browser_manager.init()

    async def __aenter__(self):
        """Enters the asynchronous context, initializing resources."""
        await self.init()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        """Exits the asynchronous context, closing resources."""
        await self.close()
        # # Return False to propagate exceptions, or True to suppress them
        # return False
        """Asynchronously initializes the crawler resources."""
        if self.config.crawler_mode == "browser" and self.config.browser_config:
            # Initialize BrowserManager if in browser mode and config is provided
            self.browser_manager = BrowserManager(self.config.browser_config)
            await self.browser_manager.init()

    async def start_crawl(self, start_url: str):
        """Starts the web crawling process."""
        print(f"Starting crawl with config: {self.config}")

        if self.config.crawler_mode == "browser" and self.browser_manager:
            print("Using browser mode...")
            # Placeholder for browser-based crawling logic
            # This is where you would use self.browser_manager to navigate pages,
            # extract data, etc.
            # Example:
            # page = await self.browser_manager.browser_context.new_page()
            # await page.goto(start_url)
            # content = await page.content()
            # print(f"Crawled content from {start_url}: {content[:100]}...") # Print first 100 chars
            # await page.close()
            pass # Replace with actual crawling logic

        elif self.config.crawler_mode == "simple":
            print("Using simple mode (aiohttp + BeautifulSoup)...")
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(start_url) as response:
                        response.raise_for_status() # Raise an exception for bad status codes
                        html_content = await response.text()

                soup = BeautifulSoup(html_content, 'lxml')
                body_content = soup.body.prettify() if soup.body else "" # Get content inside body, or empty string if no body
                print(f"Crawled content from {start_url}: {body_content[:500]}...")
                print("Simple crawl finished.")
            except aiohttp.ClientError as e:
                print(f"Error during simple crawl: {e}")
                return None # Return None or raise the exception

        else:
            print(f"Unknown crawler mode: {self.config.crawler_mode}")

        # Check for the return format
        match self.config.save_type:
            case "md":
                return md(body_content)
            case _:
                return body_content

    async def close(self):
        """Closes any resources used by the crawler."""
        if self.browser_manager:
            await self.browser_manager.browser.close()
            await self.browser_manager.session.stop()

# Example usage
async def main():
    crawler_cfg_simple = AysncCrawlerConfig(crawler_mode="simple", save_type="md")

    async with AsyncWebCrawler(crawler_cfg_simple) as crawler:
        body_content = await crawler.start_crawl("http://example.com")
        if body_content:
            print("Successfully crawled body content:")
            print(body_content[:500])
        else:
            print("Failed to crawl content.")

if __name__ == "__main__":
    asyncio.run(main())





