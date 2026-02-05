# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://clickpay.cpi-outsourcing.com/fai/payroll/downloadpayslip/speriod/2025-12-01")

# driver.implicitly_wait(5)

# tables = driver.find_elements(By.CLASS_NAME, "dataGrid")

# for table in tables:
#     rows = table.find_elements(By.TAG_NAME, "tr")
#     for row in rows:
#         cols = [td.text for td in row.find_elements(By.TAG_NAME, "td")]
#         if cols:
#             print(cols)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("PAYSLIP_USERNAME")
password = os.getenv("PAYSLIP_PASSWORD")
web = os.getenv("WEBSITE")

driver = webdriver.Chrome()
driver.get(web)
# driver.get("https://clickpay.cpi-outsourcing.com/fai/payroll/downloadpayslip/speriod/2025-12-01")

time.sleep(2)

driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "loginbutton").click()
driver.find_element(By.ID, "ico_payroll").click()



time.sleep(5)

# check if login success
print(driver.current_url)

payslip = []

tables = driver.find_elements(By.CLASS_NAME, "dataGrid")

for table in tables:
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        # cols = [td.text for td in row.find_elements(By.TAG_NAME, "td")]
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) >= 2:
            payslip.append({
                "description": cols[0].text,
                "value_1": cols[1].text,
                "value_2": cols[2].text if len(cols) > 2 else ""
            })

df = pd.DataFrame(payslip)
df.to_excel("payslip.xlsx", index=False)
os.startfile("payslip.xlsx")

print(df)