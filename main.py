from Snapdeal_module.url_scraper import get_url
from Snapdeal_module.detail_scraper import get_product_name, get_product_price, get_product_discounted_price, \
    get_product_star, get_seller_name, get_seller_star
from selenium import webdriver
import pandas as pd
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/scrape")
async def scrape():
    user_input = input("search for product:")
    url = 'https://www.snapdeal.com/'
    driver = webdriver.Chrome()

    name1 = []
    price1 = []
    discount1 = []
    star1 = []
    seller_name1 = []
    seller_star1 = []
    link1 = []

    product_links = get_url(enter_the_product=user_input, driver=driver, url=url)

    for link in product_links:

        name = get_product_name(product_link=link, driver=driver)
        name1.append(name)

        price = get_product_price(product_link=link, driver=driver)
        price1.append(price)

        discount = get_product_discounted_price(product_link=link, driver=driver)
        discount1.append(discount)

        star = get_product_star(product_link=link, driver=driver)
        star1.append(star)

        seller_name = get_seller_name(product_link=link, driver=driver)
        seller_name1.append(seller_name)

        seller_star = get_seller_star(product_link=link, driver=driver)
        seller_star1.append(seller_star)

        link1.append(link)


        # dataframe = pd.DataFrame({"name":name1, "price":price1, "discount":discount1, "star":star1, "seller_name":seller_name1, "seller_star":seller_star1, "link":link1})
        #
        # dataframe.to_csv("data.csv")

    return "scrape complete"
