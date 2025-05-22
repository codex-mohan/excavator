from pydantic import BaseModel
from typing import Literal, Optional, Dict, List
from uuid import uuid4

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
    channel: Literal["chrome", "chromium", "msedge"] = "chrome"
    viewport: Optional[Dict[str, int]] = None  # e.g., {"width": 1280, "height": 720}
    lightmode: bool = False
    proxy_config: Optional[Dict[str, str]] = None
    platform: Literal["windows", "linux", "mac"] = "windows"
    headers: Optional[Dict[str, str]] = None # Custom headers if any
    extra_args: Optional[List[str]] = None

    def model_post_init(self, __context):
        if self.lightmode:
            if self.extra_args is None:
                self.extra_args = []
            self.extra_args.extend(LITE_MODE_FLAGS)

        if self.use_persistant_context:
            if self.extra_args is None:
                self.extra_args = []
            self.extra_args.append("--no-default-browser-check")
            if self.user_data_dir is None:
                # Create the temp directory
                import os
                self.user_data_dir = os.path.join("/tmp/.playwright/", str(uuid4()))
                os.makedirs(self.user_data_dir, exist_ok=True)

class AysncCrawlerConfig(BaseModel):
    crawler_mode: Literal["simple", "browser"]
    browser_config: Optional[BrowserConfig] = None
    ignored_tags: List[str] = []
    save_type: Literal["json", "html", "md", "mhtml", "pdf"]