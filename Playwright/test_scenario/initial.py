
from playwright.sync_api import Page, Playwright, sync_playwright
import requests


url = "https://congenial-pancake-q7qx9g7qwqp5c4q66-8000.app.github.dev/"
def open_gig_form(page: Page):
    page.get_by_role("button", name="Add a Gig").click()

def create_venue():
    venue_data = {
        "name": "Test Venue",
        "address": "123 Main St",
        "city": "Springfield",
        "contact_number": "555-555-5555",
        "contact_email": "test@test.com",
        "capacity": 100,
        "notes": "Great venue!",
    }
    response = requests.post(f"{url}/api/venues",json=venue_data)



def run(_playwright: Playwright):
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.get_by_role("button", name="Continue", exact=True).click()
    open_gig_form(page)
    page.get_by_label("Venue").click()
    page.get_by_label("Venue").select_option("58")
    for i in range(2):
        create_venue()
        page.get_by_label("Venue").click()
        page.reload()
        open_gig_form(page)
        counter = 58 + i
        page.get_by_label("Venue").select_option(f"{counter}")
        #page.pause()

    browser.close()


with sync_playwright() as playwright:
    run(playwright)
