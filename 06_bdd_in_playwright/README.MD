# Beginner's Guide: BDD POM with Playwright

This is a simple introduction on how to combine **BDD (Behavior Driven
Development)** and **Page Object Model (POM)** with **Playwright** in
Python.

## Prerequisites

Before running the tests, install the following:

### 1. Python
- Python 3.8 or higher: [Python Downloads](https://www.python.org/downloads/)

### 2. Node.js
- Playwright requires Node.js v14+: [Node.js Downloads](https://nodejs.org/)

### 3. Playwright
```bash
pip install playwright
playwright install
```

### 4. pytest
```bash
pip install pytest
```

### 5. pytest-bdd
```bash
pip install pytest-bdd
```

### 6. Optional: HTML reports
```bash
pip install pytest-html
```

### 7. Folder Setup
```
models/            # Page Object Model classes
features/          # .feature files
step_definitions/  # Step implementation files
tests/             # Optional direct pytest tests
```


## What is BDD?

-   **BDD** means describing tests based on behavior, often in a
    human-readable format (e.g., Gherkin: Given/When/Then).
-   The purpose is to make tests understandable for developers, testers,
    and business stakeholders.

## What is POM?

-   **Page Object Model (POM)** is a design pattern where page elements
    and functionality are encapsulated in separate classes (Page
    Objects).
-   The benefit is that test code becomes more **readable, reusable, and
    easier to maintain**.

## Example Project Structure without BDD 
```
    tests/
    │   test_login.py
    models/
    │   login.py
```

## Example Test with Playwright and POM in file test_products.py

``` python
from playwright.sync_api import Page
from models.login import LoginPage

def test_valid_login(page: Page):
    po_login = LoginPage(page)
    po_login.navigate()
    po_login.login('test', 'test_pass')
```

## Example LoginPage Class (POM)

``` python
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # page_(element-type)_(descriptive-name)
        self.login_header_main_title = page.get_by_text('Nackademin Course App')
        self.login_input_username = page.get_by_placeholder('Username')
        self.login_input_password = page.get_by_placeholder('Password')
        self.login_btn_login = page.locator('button.button-primary')  # CSS locator
        self.login_label_have_account = page.get_by_text("Don't have an account?")
        self.login_btn_signup = page.locator('#signup')

    def navigate(self):
        self.page.goto("http://localhost:5173/")

    def login(self, username: str, password: str):
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_btn_login.click()
```

## In BDD you add a feauture file to the file structure 

### What is a feature file ? 

A feature file is a text file (usually ending with .feature) where you describe the expected behavior of your application in plain language using Gherkin syntax for user scenarios.

It’s the heart of BDD (Behavior-Driven Development), because it allows developers, testers, and even non-technical people (like product owners) to read and understand what the system should do.

### Example of a feature file for the Loginpage with 2 diffrent user scenarios for that login page 
```gherkin
Feature: Login functionality
  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I log in with username "test" and password "test_pass"
    Then I should see the application main title
  
  Scenario: Login fails with invalid password
    Given I am on the login page
    When I log in with username "test" and password "wrong_pass"
    Then I should see an error message
```

## Example Project Structure with POM + BDD 
```
tests/
│
├── features/
│   └── login.feature
│
├── step_definitions/
│   └── test_login_steps.py
│
├── models/
│   └── login.py
```
## Example Test with Playwright and POM with BDD style for one login page 

```py 

import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page, expect
from models.login import LoginPage

# Link to the feature file with Gherkin given/when/then syntax for the loginpage 
scenarios("../features/login.feature")

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@given("I am on the login page")
def go_to_login(login_page):
    login_page.navigate()

@when('I log in with username "test" and password "test_pass"')
def perform_login(login_page):
    login_page.login("test", "test_pass")

@then("I should see the application main title")
def verify_main_title(login_page):
    # Use Playwright expect instead of assert
    expect(login_page.login_header_main_title).to_be_visible()


```
## One feature file for all scenarios on that Page as for POM ?

Usually, it’s practical to group behaviors by page or functional area:
login.feature → all login-related scenarios
signup.feature → all signup-related scenarios
dashboard.feature → scenarios for the dashboard

But it’s not strictly “one page = one feature file.” Sometimes a feature can cover multiple pages if it represents a user journey (e.g., login → dashboard → create post).

💡 Tip:
Don’t overcomplicate. If a page has 10 tiny behaviors, you can put them all as separate scenarios in a single feature file. If a behavior spans multiple pages (like checkout flow), put it in one feature file that describes the full journey.

### Behavior spanning multiple pages (full journey) in one feature file checkout.feature 
```gherkin
Feature: Checkout process

  Scenario: Successful checkout
    Given I am logged in as "test_user"
    And I am on the shopping cart page
    When I proceed to checkout
    And I enter valid payment details
    Then I should see the order confirmation page

  Scenario: Checkout fails with invalid payment
    Given I am logged in as "test_user"
    And I am on the shopping cart page
    When I proceed to checkout
    And I enter invalid payment details
    Then I should see a payment error message
```

✅ Here, a single scenario spans login → cart → checkout → confirmation, so it’s all in one feature file.

### Example a test steps file that cover multiple pages in POM 

```py
import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page, expect
from models.login import LoginPage
from models.cart import CartPage
from models.checkout import CheckoutPage

# Link to the feature file
scenarios("../features/checkout.feature")

# Fixtures for each page
@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page: Page):
    return CheckoutPage(page)

# Step definitions

@given('I am logged in as "test_user"')
def login_user(login_page):
    login_page.navigate()
    login_page.login("test_user", "password123")

@given('I am on the shopping cart page')
def go_to_cart(cart_page):
    cart_page.navigate()

@when('I proceed to checkout')
def proceed_to_checkout(cart_page):
    cart_page.proceed_to_checkout()

@when('I enter valid payment details')
def enter_valid_payment(checkout_page):
    checkout_page.enter_payment(
        card_number="4111111111111111",
        expiry="12/25",
        cvv="123"
    )

@when('I enter invalid payment details')
def enter_invalid_payment(checkout_page):
    checkout_page.enter_payment(
        card_number="0000000000000000",
        expiry="01/20",
        cvv="000"
    )

@then('I should see the order confirmation page')
def verify_order_confirmation(checkout_page):
    expect(checkout_page.order_confirmation_message).to_be_visible()

@then('I should see a payment error message')
def verify_payment_error(checkout_page):
    expect(checkout_page.payment_error_message).to_be_visible()

```

## Key takeaway

Single page behaviors → multiple scenarios in one feature file
Cross-page behaviors / user journeys → put the flow in one feature file
This keeps things organized and readable, and avoids unnecessary fragmentation.

## When to USE BDD and not BDD in Playwright ? 

•	BDD + POM + Playwright → adds an extra layer (Gherkin feature files + step definitions). This is great if you have non-technical stakeholders who want to read test cases in plain English or if your team practices BDD in development.
•	POM + Playwright only → much simpler. You don’t need feature files or step mappings. You just write tests in Python using pytest directly, while still keeping Page Objects for clean structure.
👉 For most automation projects where developers/testers are the main audience, POM with Playwright is enough.

👉 Use BDD only if you specifically need business-readable test cases or are working in a strict BDD environment.

📌 Recommendation for you as a beginner:
•	Start with POM + Playwright only → it’s simpler, easier to debug, and gets you productive faster.
•	Once you’re comfortable 


------------------------------------------------------------------------

✍️ This README is a beginner's guide to quickly get started with **BDD +
POM + Playwright** in Python.

