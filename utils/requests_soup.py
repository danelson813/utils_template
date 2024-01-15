# utils/requests_soup.py
from logger_module import setup_logger
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import requests


def soup_requests(url_: str, filename: str) -> bs:
    logger = setup_logger()
    ua = UserAgent()
    headers = {f"user-agent:{ua.random}"}
    resp = requests.get(url_, headers=headers)
    soup = bs(resp.text, 'html.parser')
    save_soup(soup,filename)
    return soup

def save_soup(soup: bs, filename: str) -> None:
    with open(f"{filename}", 'w') as f:
        f.write(str(soup))
