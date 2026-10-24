import time
import os
import random
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class sutochno_parser():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=3') 
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(options=options)

        self.links_list = []
        self.driver.get('https://sutochno.ru/front/searchapp/search?guests_adults=1&occupied=2026-10-30;2026-10-31&term=%D0%9A%D0%B0%D0%BC%D1%87%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B9+%D0%BA%D1%80%D0%B0%D0%B9&SW.lat=48.695403231714&SW.lng=152.05073012499992&NE.lat=66.24193467093268&NE.lng=177.89057387499994&id=19851&type=region&price&price&is_apartment=1')
        
    def accept_cookies(self):
        clickable_element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "modal-cookies-accept"))
        )
        clickable_element.click()

    def get_links_on_the_page(self):
        time.sleep(4)

        elements = self.driver.find_elements(By.CSS_SELECTOR, 'a.card-content')
        for element in elements:
            self.links_list.append(element.get_attribute('href'))

    def go_to_the_next_page(self):
        selector = "ul > li.navigation:last-child div.pagination-arrow"
        
        try:
            clickable_element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
            )
            clickable_element.click()
            return True
            
        except TimeoutException:
            return False

    def get_page_info(self):
        for link in self.links_list:
            self.driver.get(link)
        #section-info > div > section > span:nth-child(2) > span
        guest_element = self.driver.find_element(By.CSS_SELECTOR, "#section-info > div > section > span:nth-child(2) > span")
        guest = guest_element.text
        #section-info > div > section > span:nth-child(3) > span
        bed_element = self.driver.find_element(By.CSS_SELECTOR, "section-info > div > section > span:nth-child(3) > span")
        bed = bed_element.text   
        #section-info > div > section > span:nth-child(4) > span
        room_element = self.driver.find_element(By.CSS_SELECTOR, "section-info > div > section > span:nth-child(4) > span")
        room = room_element.text
        #  span.sc-detail-map__location
        address_element = self.driver.find_element(By.CSS_SELECTOR, "span.sc-detail-map__location")
        address = address_element.text.strip()
        #section-aside > aside > div > div.sc-detail-aside-price > div > span.sc-detail-aside-price__cost
        price_element = self.driver.find_element(By.CSS_SELECTOR, "#section-aside > aside > div > div.sc-detail-aside-price > div > span.sc-detail-aside-price__cost")
        price = price_element.text.strip().replace("&nbsp;", "")        
    def __del__(self):
        print('ustal')