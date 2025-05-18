from pydantic import BaseModel
from typing import Literal, Optional, Dict, List

LITE_MODE_FLAGS = [
    "--disable-background-networking",
    "--disable-background-timer-throttling",
    "--disable-backgrounding-occluded-windows",
    "--disable-breakpad",
    "--disable-client-side-phishing-detection",
    "--disable-component-extensions-with-background-pages",
    "--disable-default-apps",
    "--disable-extensions",
    "--disable-features=TranslateUI",
    "--disable-hang-monitor",
    "--disable-ipc-flooding-protection",
    "--disable-popup-blocking",
    "--disable-prompt-on-repost",
    "--disable-sync",
    "--force-color-profile=srgb",
    "--metrics-recording-only",
    "--no-first-run",
    "--password-store=basic",
    "--use-mock-keychain",
]

class BrowserConfig(BaseModel):
    headless: bool = True
    browser_mode: Literal["dedicated", "built-in", "custom"] = "dedicated"
    use_inbuilt_browser: bool = False
    use_persistant_context: bool = False
    user_data_dir: Optional[str] = None
    proxy: Optional[str] = None
    chrome_channel: Literal["chrome", "chromium", "msedge"] = "chrome"
    viewport: Optional[Dict[str, int]] = None  # e.g., {"width": 1280, "height": 720}
    litemode: bool = False
    proxy_config: Optional[Dict[str, str]] = None
    platform: Literal["windows", "linux", "mac"] = "windows"
    headers: Optional[Dict[str, str]] = None # Custom headers if any
    text_only: bool = False
    extra_args: Optional[List[str]] = None

    def __init__(self):
        super().__init__()
        if self.litemode:
            self.extra_args.extend(LITE_MODE_FLAGS)

class AysncCrawlerConfig(BaseModel):
    browser_config: BrowserConfig