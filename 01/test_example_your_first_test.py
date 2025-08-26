´´´ Write a test with one expect choose your website and try to do some metods from page Class Library and use 
    expect library for implementing end-to-end frontend testing. 

    For expect metods see https://playwright.dev/python/docs/test-assertions

    For page metods 
´´´


### Test below for example 

def test_homepage_url(page):
page.goto("https://www.svt.se")

expect(page).to_have_url("https://www.svt.se/") 

