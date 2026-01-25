from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

search_content = input("Enter the content that you want to search: ")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.youtube.com/")

search_bar = driver.find_element(By.CSS_SELECTOR, ".ytSearchboxComponentInput" )
search_bar.send_keys(search_content)
search_icon = driver.find_element(By.CSS_SELECTOR, ".ytSearchboxComponentSearchButton")
search_icon.click()

input("The browser is open! To close it press ENTER")
driver.quit()
