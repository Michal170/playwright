from playwright.sync_api import sync_playwright
import time
 
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500) #Launch browser
    page = browser.new_page()
    url = "https://bootswatch.com/default"
    page.goto(url)
    
    #Locators
    default_button = page.get_by_role('button', name='Default button')
    default_button.highlight()
    default_button.click()
    
    heading = page.get_by_role('heading', name='Heading 2')
    heading.highlight()
    
    radio_btn = page.get_by_role('radio', name="Option one is this and that—be sure to include why it's great" )
    radio_btn.highlight()
    
    checkbox = page.get_by_role('checkbox', name="Default checkbox")
    checkbox.highlight()
    checkbox.check()
    
    #Input locators
    input_locator = page.get_by_label("Email address").highlight()
    password_locator = page.get_by_label("Password").highlight()
    email_locator = page.get_by_placeholder("Enter email").highlight()
    
    #Select text
    text_locator = page.get_by_text("with muted text").highlight()
    page.get_by_text("Middle").click()
    page.get_by_text("fine print", exact=False).highlight()
    
    #CSS selectors
    page.locator("footer").highlight()
    page.locator("button.btn-outline-success").highlight()
    page.locator("button.btn-outline-success").click()
    
    page.locator("button#btnGroupDrop1").click()
    page.locator("button#btnGroupDrop1").click()
    page.locator("input[value='correct value']").highlight()
    
    
    browser.close()