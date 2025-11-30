from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Chrome Options
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # run browser in background
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Path to chromedriver
service = Service(ChromeDriverManager().install()) # download from chromedriver site

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://ph.indeed.com/jobs?q=Python")

# jobs = []

# job_cards = driver.find_elements(By.CSS_SELECTOR, "a.tapItem")

# print("Jobs found:", len(job_cards))

# driver.quit()

try:
    job_cards = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.tapItem"))
    )
    print(f"Jobs found: {len(job_cards)}")
except:
    print("No jobs found!")
    
driver.quit()