from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from bs4 import BeautifulSoup

class VSCOScraper:
    def __init__(self, url):
        self.path_webdriver = "C:/Users/Nicolas/OneDrive/Área de Trabalho/Github/SocialMine/scraper/config/chromedriver.exe"
        self.url = url
        
        self.option = Options()
        self.option.add_argument("--headless")
        
        self.service = Service(self.path_webdriver)
        self.driver = webdriver.Chrome(service=self.service, options=self.option)
        
    def get_image_srcs(self):
        self.driver.get(self.url)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        
        images_of_divs = soup.find_all("img", {"class": "disableSave-mobile css-6dp941"})
        srcs = [div.get('src').lstrip('//') for div in images_of_divs]
        
        self.driver.quit()
        return srcs

"""
if "__main__" == __name__:
    path_webdriver = "C:/Users/Nicolas/OneDrive/Área de Trabalho/Github/SocialMine/scraper/config/chromedriver.exe"
    url = "https://vsco.co/coltonolxa/gallery"

    scraper = VSCOScraper(path_webdriver, url)
    srcs = scraper.get_image_srcs()
    print(srcs)
"""