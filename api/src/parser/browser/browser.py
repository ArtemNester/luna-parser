from dataclasses import dataclass

from playwright.async_api import (
    BrowserType as PBType,
    Playwright,
)

from src.parser.browser.enums import BrowserType


@dataclass
class BrowserFactory:
    @staticmethod
    def get_browser(playwright: Playwright, browser_type: str) -> PBType:
        if BrowserType.CHROMIUM == browser_type:  # Guard clauses style
            return playwright.chromium
        if BrowserType.FIREFOX == browser_type:
            return playwright.firefox
        if BrowserType.WEBKIT == browser_type:
            return playwright.webkit
        raise ValueError(f"Unsupported browser type: {browser_type}")
