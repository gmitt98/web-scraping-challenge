from splinter import Browser
from selenium import webdriver

drive = webdriver.Chrome

# Create a new instance of the browser
browser = Browser('chrome')

# Visit a web page
browser.visit('https://www.google.com')

# Find an element on the page and interact with it
search_box = browser.find_by_name('q').first
search_box.fill('Python')
search_box.submit()

# Wait for the page to load and print the title
browser.is_element_present_by_css('h3', wait_time=10)
print(browser.title)

# Close the browser
browser.quit()
