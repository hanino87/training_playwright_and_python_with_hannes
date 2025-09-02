# Playwright Page Object Model (POM) Guide

## Introduction

The **Page Object Model (POM)** is a design pattern in test automation that encourages separating page structure from test logic. Each page in the application is represented by a class containing:
- Locators for elements on that page
- Methods to interact with those elements

Using POM in Playwright improves **readability, maintainability, and reusability** of tests.

---

## Benefits of Using POM

1. **Readability**: Test steps become more descriptive and human-readable.
2. **Reusability**: Common actions can be reused across multiple tests.
3. **Maintainability**: UI changes require updating locators in only one place.
4. **Consistency**: Reduces duplicate code and makes tests cleaner.

---

## Example: Login Page (POM)

``` python
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Semantic locators
        self.username_input = page.get_by_placeholder("Username")  # Input field for username
        self.password_input = page.get_by_placeholder("Password")  # Input field for password
        self.login_button = page.get_by_role("button", name="Login")  # Login button

    def navigate_to_homepage(self):
        self.page.goto("http://localhost:5173/")

    def login(self, username: str, password: str):
        self.username_input.fill(username)  # Fill username
        self.password_input.fill(password)  # Fill password
        self.login_button.click()  # Click login
```

------------------------------------------------------------------------

## Using the Page Object in a Test

### ✅ With POM (clean & maintainable)

``` python
from playwright.sync_api import Page
from models.login import LoginPage

def test_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_homepage()  # Use POM navigation
    login_page.login(username="admin", password="admin123")  # Use POM login method
```

------------------------------------------------------------------------

### ❌ Without POM (longer & harder to maintain)

``` python
from playwright.sync_api import Page

def test_login_without_pom(page: Page):
    page.goto("http://localhost:5173/")  # Navigate directly
    page.get_by_placeholder("Username").fill("admin")  # Fill username
    page.get_by_placeholder("Password").fill("admin123")  # Fill password
    page.get_by_role("button", name="Login").click()  # Click login
```

------------------------------------------------------------------------

## Why Use POM?

-   ✅ **Reduces code duplication**\
-   ✅ **Centralizes locators** (easy to update when UI changes)\
-   ✅ **Improves readability** (tests read like business logic)\
-   ✅ **Reusable methods** across multiple test files

------------------------------------------------------------------------

📌 This README demonstrates how **POM improves test structure** by
comparing a short, clean POM-based test with a longer,
harder-to-maintain test without POM.
