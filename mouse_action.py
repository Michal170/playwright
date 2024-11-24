from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
   browser =  playwright.chromium.launch(headless=False, slow_mo=1000)
   page = browser.new_page()
   url = "https://bootswatch.com/default"
   page.goto(url)
   
   page.get_by_role("button", name="Block button").highlight()
   button = page.get_by_role("button", name="Block button").first
   button.click()
   
   button.dblclick()
   
   button.dblclick(delay=500)
   
   button.click(button="right")
   button.click(modifiers=["Shift"])
   outline_button = page.locator("button.btn-outline-primary")
   outline_button.hover()
   
   
   
   browser.close()