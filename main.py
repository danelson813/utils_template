# main.py
from utils.logger_module import setup_logger
from utils.selenium_soup import obtain_soup, create_dataframe
from utils.util import to_sqlite3, csv_to_df, view_db

# Enter the values below
url1 = ""
filename1_soup = "html_for_soup.txt"
url2 = ''
filename2_soup = 'html_for_soup2.txt'

filename_db = "data/data.db"
tablename = "items"

filename_csv = 'data/results.csv'
filename_from_csv = 'data/results.csv'

selector_items = "div"
selector_text_items = "'data-testid': 'property-card'"


logger = setup_logger()
logger.info("The logger has started . . .")

urls = [url1, url2]
for index, url in enumerate(urls):
    if index == 0:
        filename = filename1_soup
        url = url1
    if index == 1:
        filename = filename2_soup
        url = url2
    soup = obtain_soup(url, filename)

    results = []

    #  parse the soup for the information
    items = soup.find_all(f"{selector_items}", f"{{selector_text_items}}")

    for item in items:

        result = {
            
        }
    results.append(results)

df = create_dataframe(results, filename_csv)
test_df = csv_to_df(filename_csv)
to_sqlite3(df, filename_db, tablename )
