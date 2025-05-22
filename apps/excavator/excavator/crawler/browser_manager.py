from patchright.async_api import async_playwright
from .config.aysnc_config import BrowserConfig

class BrowserManager:
    def __init__(self, browser_config: BrowserConfig):
        self.browser_config = browser_config
        self.session = None
        self.browser = None
        self.browser_context = None

    async def init(self):
        self.session = await async_playwright().start()
        self.browser = await self.session.chromium.launch(
            headless=self.browser_config.headless,
            channel=self.browser_config.channel,
            args=self.build_browser_flags()
        )
        self.browser_context = await self.browser.new_context()

    @staticmethod
    def build_browser_flags():

        flags = [
            "--disable-gpu",
            "--disable-gpu-compositing",
            "--disable-software-rasterizer",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--no-first-run",
            "--no-default-browser-check",
            "--disable-infobars",
            "--window-position=0,0",
            "--ignore-certificate-errors",
            "--ignore-certificate-errors-spki-list",
            "--disable-blink-features=AutomationControlled",
            "--window-position=400,0",
            "--disable-renderer-backgrounding",
            "--disable-ipc-flooding-protection",
            "--force-color-profile=srgb",
            "--mute-audio",
            "--disable-background-timer-throttling",
        ]