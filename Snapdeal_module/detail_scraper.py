
from selenium.webdriver.common.by import By

def get_product_name(product_link, driver):
    driver.get(product_link)
    try:
        product_names = driver.find_element(By.XPATH, '//div[contains(@class,"row")]/div/h1')
        return product_names.text
    except:
        return None

def get_product_price(product_link, driver):
    driver.get(product_link)
    try:
        product_price = driver.find_element(By.CLASS_NAME, 'pdp-final-price')
        return product_price.text
    except:
        return None

def get_product_discounted_price(product_link, driver):
    driver.get(product_link)
    try:
        discounted_price = driver.find_element(By.CLASS_NAME, "pdpCutPrice")
        return discounted_price.text
    except:
        return None

def get_product_star(product_link, driver):
    driver.get(product_link)
    try:
        star = driver.find_element(By.CLASS_NAME, "avrg-rating")
        return star.text
    except:
        return None

def get_seller_name(product_link, driver):
    driver.get(product_link)
    try:
        seller_name = driver.find_element(By.XPATH, '//div[contains(@class,"sellerNameContainer h2 blackText")]/a/span')
        return seller_name.text
    except:
        return None

def get_seller_star(product_link, driver):
    driver.get(product_link)
    try:
        seller_star = driver.find_element(By.XPATH,'//span[contains(@class,"sellerRatingContainer reset-padding lfloat marR5")]/span[2]')
        return seller_star.text
    except:
        return None













