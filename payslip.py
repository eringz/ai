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

driver = webdriver.Chrome()
# driver.get("https://clickpay.cpi-outsourcing.com/fai/auth")
driver.get("https://clickpay.cpi-outsourcing.com/fai/payroll/downloadpayslip/speriod/2025-12-01")

time.sleep(2)

driver.find_element(By.ID, "username").send_keys("FAI2025213")
driver.find_element(By.ID, "password").send_keys("Dreamplanf1X")
driver.find_element(By.ID, "loginbutton").click()

time.sleep(5)

# check if login success
print(driver.current_url)
