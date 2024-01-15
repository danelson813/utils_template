# utils.selenium_soup.py
import pandas as pd
import os.path
from utils import webdriver
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from time import sleep
from logger_module import setup_logger


def get_soup_sel(url_: str, filename: str) -> bs:
    logger = setup_logger()
    options = Options()
    options.add_arguement('--headless')
    ua = UserAgent()
    user_agent = ua.random
    options.add_arguement(f"user-agent:{user_agent}")
    with webdriver.Firefox(service=Service('Users/geckodriver'),
                            options = options) as driver:
        driver.get(url_)
        sleep(2)
        driver.maximize_window()
        driver.save_screenshot("data/homepage.png")
        soup = bs(driver.page_source, 'html.parser')
        save_soup(soup, filename)

        return(soup)


def save_soup(soup: bs, filename: str) -> None:
    with open(f'{filename}', 'w') as f:
        f.write(str(soup))


def retrieve_soup(filename: str) -> bs:
    with open(filename, 'r') as f:
        text_ = f.read()
        return bs(text_, 'html.parser')


def obtain_soup(url_, filename: str) -> bs:
    logger = setup_logger()
    path = filename
    if os.path.isfile(path):
        soup = retrieve_soup(filename=filename)
        logger.info("Used the file to retreive soup")
    else: 
        logger.info("Used selenium to retreive soup")
        soup = get_soup_sel(url_)
    return soup


def create_dataframe(results_: list, filename: str) -> pd.core.frame.DataFrame:
    df = pd.DataFrame(results_)
    df.to_csv(filename)
    return df