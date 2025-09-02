# Write three tests with expect and pages metods from Playwright choose your own website. 
    
# Test below for example 

def test_homepage_url(page):
page.goto("https://www.svt.se") # uses page metod goto to go to a website 

expect(page).to_have_url("https://www.svt.se/") # assert webpage has right url for user 

expect(response).to_be_ok() # assert repsonse from webiste is okay 

