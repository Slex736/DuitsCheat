from playwright.sync_api import sync_playwright
import keyboard

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://apps.noordhoff.nl/se/content/theme/95339555-cf9f-4173-83c8-20057307c414")


    def PageCheat():
        try:
            # Wait for the div to appear
            div_element = page.wait_for_selector(
                "div.MuiTypography-root.MuiTypography-playerBody.MuiTypography-gutterBottom.pl-paragraph",
                timeout=5000
            )
            if div_element:
                # Get the full HTML inside the div
                html_content = div_element.inner_html()
                print(html_content)
        except:
            print("No Worky")
            html = page.content()
        print("Cheat Activated")

    try:
        while True:
            key = keyboard.read_event(suppress=False)
            if key.event_type == 'down':
                if key.name == "esc":
                    break
                elif key.name == "z":
                    PageCheat()
    finally:
        browser.close()