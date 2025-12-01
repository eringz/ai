import time, random
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth


def shopee_scrape(keyword, max_items=20):
    options = Options()

    # HINDI HEADLESS (Shopee blocks headless 100%)
    # options.add_argument("--headless=new")  # do not use

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")

    # Random realistic fingerprint
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122 Safari/537.36"
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # MAGIC: Selenium Stealth (Shopee still fails here)
    stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    # url = f"https://shopee.ph/search?keyword={keyword}"
    url = "https://shopee.ph/search?keyword=laptop"
    driver.get(url)
    print(url)

    print("⌛ Loading page…")
    time.sleep(5 + random.random() * 2)

    # RANDOM HUMAN-LIKE SCROLLING
    for _ in range(8):
        driver.execute_script(f"window.scrollBy(0, {random.randint(300, 800)});")
        time.sleep(1 + random.random())

    # FIND ITEMS
    items = driver.find_elements(By.XPATH,
        "//div[contains(@class,'shopee-search-item-result__item')]"
    )

    if len(items) == 0:
        print("❌ BLOCKED again! Selector didn’t load.")
        driver.quit()
        return None

    print(f"✔ Found {len(items)} items")

    products = []

    for i, item in enumerate(items):
        if i >= max_items:
            break

        try:
            title = item.find_element(By.XPATH, ".//div[contains(@class,'_10Wbs-')]").text
        except:
            title = "N/A"

        try:
            price = item.find_element(By.XPATH, ".//span[contains(@class,'_29R_un')]").text
        except:
            price = "N/A"

        try:
            link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        except:
            link = "N/A"

        products.append({
            "title": title,
            "price": price,
            "link": link,
        })

    driver.quit()

    return pd.DataFrame(products)


# RUN
if __name__ == "__main__":
    df = shopee_scrape("laptop", max_items=15)

    if df is not None:
        print(df)
        df.to_csv("shopee_results.csv", index=False)
        print("✔ Saved to shopee_results.csv")
