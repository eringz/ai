from selenium import webdriver
from selenium.webdriver.common.service import Service
from dotenv import load_dotenv
import os
import time

load_dotenv()

username = os.getenv("PAYSLIP_USERNAME")
password = os.getenv("PAYSLIP_PASSWORD")

service = Service(executable_path="")
driver = webdriver.Chrome(service=service)




time.sleep(2)
