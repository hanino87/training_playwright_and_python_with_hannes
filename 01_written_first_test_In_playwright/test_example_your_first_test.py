# Write three tests with expect and pages metods from Playwright choose your own website. 
    
# Test below for example 

from playwright.sync_api import Page, expect

# Test 1: Check homepage URL
def test_homepage_url(page: Page):
    response = page.goto("https://svt.se)
    
    # Assert the page loaded correctly
    expect(response).to_be_ok()
    
    # Assert the page URL is correct
    expect(page).to_have_url("https://svt.se/")
