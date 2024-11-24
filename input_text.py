from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1500)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    
    page.get_by_label("Email address").highlight()
    page.locator("footer").highlight()
    
    input = page.get_by_placeholder("Enter email")
    
    input.fill("ex@gmail.com")
    input.clear()
    
    input.type("sd@gmail.com")
    
    
    browser.close()