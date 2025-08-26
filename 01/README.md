# Name rules for testfiles and tests 

test files must follow test_ prefix convention, as test_hannes.py, inside the current working directory or in a sub-directory with the code below. Make sure your test name also follows the test_ prefix convention.

```py

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

```
test_hannes.py 

If you don`t follow the prefix convetion then pytest will not see the files and test as test and 
then the test will not running in your terminal. 


#🧠 Understanding page: Page in Tests
In Playwright's test functions, the page parameter is an instance of the Page class, automatically provided by the Playwright test runner.

✅ What is Page?
Page represents a single tab or browser window.
It provides all the methods you need to navigate, click elements, fill forms, take screenshots, etc.

🔍 Example

```py

def test_go_to_webpage(page: Page):
    page.goto("https://www.svt.se")  # uses metod goto from the Class page to go to a url 

```
Import page class 

```py
from playwright.sync_api import Page

```
Full example of a python file with Page class 

```py

from playwright.sync_api import Page

def test_get_started_link(page: Page):
    page.goto("https://www.svt.se"")
    
```

# 🟩 expect – Playwright's Smart Assertion

It`s better then pythons built in assertion. Bettfor waiting for element to load on pages. 

-  Comes from Playwright's test API
-  Adds automatic waiting and retries (very helpful for dynamic pages)
-  Great for UI assertions, like checking visibility, text content, etc.

✅ Example:

```Py

def test_homepage_url(page):
page.goto("https://www.svt.se")

expect(page).to_have_url("https://www.svt.se/") # do assert that svt homepage has the right url for viewers 

```

Import it in your file 

```py

from playwright.sync_api import expect

```
Full example of a python file with Expect 

```py

from playwright.sync_api import expect

def test_heading(page):
    page.goto("https://www.svt.se")
    
    expect(page).to_have_url("https://www.svt.se/")

```
# Good Links 

List of assertion from expect library https://playwright.dev/python/docs/test-assertions

pages metod https://playwright.dev/python/docs/input







