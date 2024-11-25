from fastapi import FastAPI
from Snapdeal_module.url_scraper import get_url
from Snapdeal_module.detail_scraper import get_product_name, get_product_price, get_product_discounted_price, \
    get_product_star, get_seller_name, get_seller_star
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
# import json
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/scrape")
async def scrape(user_input: str):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chromedriver_path = "/usr/bin/chromedriver"
    service = Service(chromedriver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = 'https://www.snapdeal.com/'
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

    dataframe = pd.DataFrame({
        "name": name1,
        "price": price1,
        "discount": discount1,
        "star": star1,
        "seller_name": seller_name1,
        "seller_star": seller_star1,
        "link": link1
    })


    csv_path = "static/data.csv"
    dataframe.to_csv(csv_path, index=False)

    # json_data = dataframe.to_json(orient='records')
    # beautified_json = json.dumps(json.loads(json_data), indent=4)


    return {
        "csv_url": "/static/data.csv"
    }
