from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://whatmyuseragent.com/")
    page.screenshot(path="sync_demo.png")
    browser.close()