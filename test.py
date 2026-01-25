from selenium import webdriver
from selenium.webdriver.common.service import Service
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("PAYSLIP_USERNAME")

service = Service(executable_path="")
driver = webdriver.Chrome(service=service)



