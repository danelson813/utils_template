# utils/playwright_soup.py

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

url = "https://demo.opencart.com/admin/"


def make_soup(url: str) -> BeautifulSoup:
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.fill('input#input-username', 'demo')
        page.fill('input#input-password', 'demo')
        page.click('button[type=submit]')
        page.click('button.btn-close')
        page.is_visible('div.tile-body')
        time.sleep(5)
        html_ = page.inner_html('#content')
        soup = BeautifulSoup(html_, 'html.parser')
        total_orders = soup.find("h2").text
        print(f"total orders = {total_orders}")
        return soup


if __name__ == '__main__':
    soup_ = make_soup(url)
    # print(soup_)