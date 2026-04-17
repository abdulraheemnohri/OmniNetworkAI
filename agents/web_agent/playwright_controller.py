from playwright.sync_api import sync_playwright

class PlaywrightController:
    def __init__(self):
        pass

    def automate_website(self, url, actions):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)
            title = page.title()
            browser.close()
            return f"Automated {url}. Title: {title}"

    def scrape_data(self, url, selector):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)
            content = page.inner_text(selector)
            browser.close()
            return content
