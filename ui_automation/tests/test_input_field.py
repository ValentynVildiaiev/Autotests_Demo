from Autotests_Demo.ui_automation.pages.text_input import TextInputPage


def test_input_field(browser):
    text_input_page = TextInputPage(browser)
    text_input_page.open_page_text_input()
    assert "Input Field" in browser.title