from playwright.sync_api import sync_playwright
import time
 
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500) #Launch browser
    page = browser.new_page()
    page.goto("https://playwright.dev/python/")
   
    #Click on button
    docs_button = page.get_by_role('link', name="Docs")
    docs_button.click()
    
    #Get page url
    url = "https://bootswatch.com/default"
    page.goto(url)
    
    browser.close()