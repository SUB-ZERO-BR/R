# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com")
time.sleep(8)

soup = BeautifulSoup(driver.page_source, 'html.parser')
video_links = [link.get('href') for link in soup.find_all('a', id='thumbnail')]

first_video = video_links[2]
driver.get(f'https://www.youtube.com{first_video}')
time.sleep(6)
wait = WebDriverWait(driver, 10)
skip_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ytp-ad-skip-button.ytp-button')))
skip_button.click()
time.sleep(120)