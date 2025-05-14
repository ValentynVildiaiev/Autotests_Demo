from playwright.sync_api import sync_playwright, Playwright

url = "https://congenial-pancake-q7qx9g7qwqp5c4q66-8000.app.github.dev/"
def run(playwright: Playwright):
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.get_by_role("button", name="Continue", exact=True).click()
    page.get_by_role("button", name="Add a Gig").click()
    page.get_by_role("textbox", name="Gig Name").click()
    page.get_by_role("textbox", name="Gig Name").fill("Searchable gig test")
    page.get_by_role("textbox", name="Gig Date").fill("2025-05-23")
    page.get_by_label("Venue").select_option("5")
    page.get_by_label("Client").select_option("2")
    page.get_by_role("button", name="Submit").click()
    assert page.get_by_role("cell", name="Year boy believe.").text_content()== "Year boy believe."
    page.locator(".bi").first.click()
    page.get_by_role("textbox", name="Search").click()
    page.get_by_role("textbox", name="Search").fill("searchable")
    page.keyboard.press("Enter")
    page.pause()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)