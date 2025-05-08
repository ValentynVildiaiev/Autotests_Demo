from playwright.async_api import async_playwright
import asyncio


async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://whatmyuseragent.com/")
        await page.screenshot(path="asyncdemo.png")
        print(await page.title())
        await browser.close()


asyncio.run(main())
