#!/usr/bin/python3

# Dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By

# Instantiate driver and browser
driver = webdriver.Firefox()

# Open webpage in headfull mode
driver.get("https://dev.to")

# Confirm desired page has been reached
assert "DEV" in driver.title

# Look for search bar element
search_bar = driver.find_element(By.NAME, "q")
# print(search_bar)

# Input "hello" into the search bar
search_bar.send_keys("Hello")

# Start the search
# Tip: Replace spaces by dots and include the tag name at the beginning
search_button = driver.find_element(By.CSS_SELECTOR, "button.c-btn.c-btn--icon-alone.absolute.inset-px.left-auto.mt-0.py-0")
# print(search_button)
search_button.click()

