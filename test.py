from selenium import webdriver
from selenium.webdriver.common.service import Service
from dotenv import load_dotenv

load_dotenv()

service = Service(executable_path="")
driver = webdriver.Chrome(service=service)


