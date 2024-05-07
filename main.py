import os
from typing import Final
from dotenv import load_dotenv
from scraping import scrape_items
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

load_dotenv()

FORMS_URL: Final[str] = os.getenv('FORMS_URL')

def fill_form(item) -> None:
    """Get the elements to fill, fills the elements and clicks the submit button."""
    # Get the elements using XPATH
    title_input: WebElement = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    image_input: WebElement = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price: WebElement = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link: WebElement = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    delivery_cost: WebElement = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    delivery_time: WebElement = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    send_button: WebElement = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    # Fill in the information
    title_input.send_keys(item['title'])
    image_input.send_keys(item['image_url'])
    price.send_keys(item['price'])
    link.send_keys(item['link'])
    delivery_cost.send_keys(item['delivery_cost'])
    delivery_time.send_keys(item['delivery_time'])
    send_button.click()

if __name__ == '__main__':
    # Keep the chrome open
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    # Initialize the browser
    driver = webdriver.Chrome(options=chrome_options)

    # Go to the form
    driver.get(FORMS_URL)

    # Get the list of items
    items_list: list = scrape_items()

    # For each item fill the form and then refresh the page
    for item in items_list:
        fill_form(item)
        driver.refresh()