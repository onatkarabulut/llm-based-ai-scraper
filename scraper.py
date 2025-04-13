import os
import time
import logging as lg
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
load_dotenv()

lg.basicConfig(filename='logs/scraper.log',
               level=lg.INFO,
               format='%(levelname)s:%(asctime)s:%(message)s',
               datefmt="%Y-%m-%d %H:%M:%S")


class Scraper:
    def __init__(self):
        chrome_binary_path = os.getenv("CHROME_BINARY_PATH")
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = chrome_binary_path
        chrome_options.add_argument("--headless")  # Headless mode for the background running
        chrome_options.add_argument("--no-sandbox")  # For some Linux distros
        chrome_options.add_argument("--disable-dev-shm-usage")  # To optimize memory usage 
        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                       options=chrome_options)

    def scrape_website(self, website):
        lg.info("--> Browser is starting..")
        try:
            self.driver.get(website)


            lg.info("Page is opening..")
            page = self.driver.page_source
            time.sleep(7)
            return page
        finally:
            self.driver.quit()

    def extract_html(self, html):
        soup = bs(html, "html.parser")
        if soup.body: return str(soup.body)
        return ""

    def clean_html(self, html_body):
        soup = bs(html_body, "html.parser")

        for i in soup(["script", "style"]):
            i.extract()

        clean_html = soup.get_text(separator="\n")
        clean_html = "\n".join(line.strip() for line in clean_html.splitlines() if line.strip())

        return clean_html
    
    def split_html_dom(self, dom_content, lenght_max=8000):
        return [
            dom_content[i: i + lenght_max] for i in range(0, len(dom_content), lenght_max)
        ]