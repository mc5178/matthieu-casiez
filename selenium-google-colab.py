!apt-get update
!apt install -y chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
!pip install selenium

import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

def get_page_metadata(url):
    driver.get(url)

    title = driver.title

    try:
        meta_description = driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute("content")
    except:
        meta_description = None

    try:
        meta_robots = driver.find_element(By.XPATH, "//meta[@name='robots']").get_attribute("content")
    except:
        meta_robots = None

    try:
        first_h1 = driver.find_element(By.TAG_NAME, "h1").text
    except:
        first_h1 = None

    return {
        "title": title,
        "meta_description": meta_description,
        "meta_robots": meta_robots,
        "first_h1": first_h1
    }

url = "https://www.matthieucasiez.com/fr/"

metadata = get_page_metadata(url)

print(metadata["title"])
print(metadata["meta_description"])
print(metadata["meta_robots"])
print(metadata["first_h1"])

driver.quit()