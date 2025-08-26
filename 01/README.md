# Name rules for testfiles and tests 

test files must follow test_ prefix convention, as test_hannes.py, inside the current working directory or in a sub-directory with the code below. Make sure your test name also follows the test_ prefix convention.

```py

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

```
test_hannes.py 

If you don`t follow the prefix convetion then pytest will not see the files and test as test and 
then the test will not running in your terminal. 





