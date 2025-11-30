from typing import Pattern

from playwright.sync_api import Page, expect

from tools.logger import get_logger

logger = get_logger("BASE_COMPONENT")


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        step = f"Check current url is {expected_url}"
        logger.info(step)
        expect(self.page).to_have_url(expected_url)
        