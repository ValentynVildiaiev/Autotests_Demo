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


def create_venue(page: Page):
    page.get_by_label("Venue").select_option("/venues")
    page.goto("https://congenial-pancake-q7qx9g7qwqp5c4q66-8000.app.github.dev/venues")
    page.get_by_role("button", name="Add a Venue").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("My Venue")
    page.get_by_role("textbox", name="Adress").click()
    page.get_by_role("textbox", name="Adress").fill("31 157th Ave SE")
    page.get_by_role("textbox", name="Contact Number").click()
    page.get_by_role("textbox", name="Contact Number").fill("5181234567")
    page.get_by_role("textbox", name="Contact Email Address").click()
    page.get_by_role("textbox", name="Contact Email Address").fill("testing@example.com")
    page.get_by_role("spinbutton", name="Venue Capacity").click()
    page.get_by_role("spinbutton", name="Venue Capacity").fill("100")
    page.get_by_role("textbox", name="Notes").click()
    page.get_by_role("textbox", name="Notes").fill("New test venue")
    page.get_by_role("button", name="Submit").click()

def create_client(page: Page):
    page.get_by_role("link", name=" Clients").click()
    page.get_by_role("button", name="Add a Client").click()
    page.get_by_role("textbox", name="Enter the Client's first name").click()
    page.get_by_role("textbox", name="Enter the Client's first name").fill("Val")
    page.get_by_role("textbox", name="Enter the Client's last name").click()
    page.get_by_role("textbox", name="Enter the Client's last name").fill("Vild")
    page.locator("#client-address").click()
    page.locator("#client-address").fill("31 157th Ave Se")
    page.locator("#client-city").click()
    page.locator("#client-city").fill("Bell")
    page.locator("#client-contact_number").click()
    page.locator("#client-contact_number").fill("9181238765")
    page.locator("#client-contact_email").click()
    page.locator("#client-contact_email").fill("test_val@example.com")
    page.get_by_role("button", name="Submit").click()

def create_gig_with_venue_and_client(page: Page):
    page.get_by_role("link", name=" Home").click()
    page.get_by_role("button", name="Add a Gig").click()
    page.get_by_role("textbox", name="Gig Name").click()
    page.get_by_role("textbox", name="Gig Name").fill("val_test")
    page.get_by_role("textbox", name="Gig Date").fill("2025-05-15")
    page.get_by_label("Venue").select_option("60")
    page.get_by_label("Client").select_option("55")
    page.get_by_role("button", name="Submit").click()

def run(_playwright: Playwright):
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.get_by_role("button", name="Continue", exact=True).click()
    open_gig_form(page)
    create_venue(page)
    create_client(page)
    create_gig_with_venue_and_client(page)

    page.pause()

    browser.close()


with sync_playwright() as playwright:
    run(playwright)
