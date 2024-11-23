from selenium import webdriver
from selenium.webdriver.common.by import By

def get_url(enter_the_product,driver, url):
    driver.get(url)

    search_box = driver.find_element(By.XPATH, "//input[contains(@class,'col-xs-20 searchformInput keyword')]")
    search_box.send_keys(enter_the_product)
    search_button = driver.find_element(By.XPATH, "//button[contains(@class,'searchformButton col-xs-4 rippleGrey')]")
    search_button.click()

    product_links = driver.find_elements(By.XPATH,"//section[contains(@class,'js-section clearfix dp-widget dp-fired')]/div/div/a")
    links_container = []
    for link in product_links:
        links_container.append(link.get_attribute("href"))
    return links_container
