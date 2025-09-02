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

## Example: Login Page

```python
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Semantic locators
        self.username_input = page.get_by_placeholder("Username")  # Input field for username
        self.password_input = page.get_by_placeholder("Password")  # Input field for password
        self.login_button = page.get_by_role("button", name="Login")  # Login button

    def login(self, username: str, password: str):
        self.username_input.fill(username)  # Fill username
        self.password_input.fill(password)  # Fill password
        self.login_button.click()  # Click login
```

### Using the Page Object in a Test

```python
from models.login import LoginPage

def test_login(page: Page):
    login_page = LoginPage(page)
    page.goto("http://localhost:5173/login")  # Navigate to login page
    login_page.login(username="admin", password="admin123")  # Use POM method
```

---

## Example: Home Page

```python
from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.product_name_input = page.get_by_placeholder("Product Name")  # Input field for product name
        self.create_product_button = page.get_by_role("button", name="Create Product")  # Create Product button
        self.product_list = page.locator(".product-grid")  # Product grid container

    def create_product(self, name: str):
        self.product_name_input.fill(name)  # Fill product name
        self.create_product_button.click()  # Click create product
        # Return locator for the last product with that name
        return self.product_list.locator(f".product-item:has-text('{name}')").last
```

---

## Test Example Using POM

```python
from models.login import LoginPage
from models.home import HomePage

def test_add_product_to_catalog(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.navigate()  # Go to homepage
    login_page.login(username="admin", password="admin123")  # Log in user
    home_page.create_product("New Product")  # Add a product
```

This demonstrates **clean, readable, and maintainable tests** using semantic locators and POM.

---

## Long Test Without POM (Demonstration)

```python
from playwright.sync_api import Page, expect

def test_add_product_to_catalog_without_pom(page: Page):
    # Navigate to homepage
    page.goto("http://localhost:5173/")  # Go to homepage

    # Navigate to signup page
    page.get_by_role("link", name="Sign Up").click()  # Click Sign Up link

    # Register or login admin user
    page.get_by_placeholder("Username").fill("admin")  # Fill username
    page.get_by_placeholder("Password").fill("admin123")  # Fill password
    page.get_by_role("button", name="Login").click()  # Click login button

    # Add a product
    page.get_by_placeholder("Product Name").fill("New Product")  # Fill product name
    page.get_by_role("button", name="Create Product").click()  # Click create product button

    # Verify product appears
    last_product = page.locator(".product-grid .product-item").last  # Get last product
    expect(last_product).to_have_text("New Product")  # Assert product text

    # Delete product
    last_product.locator(".product-item-button").click()  # Click delete button

    # Assert product removed
    all_products = page.locator(".product-grid .product-item")  # Get all products
    expect(all_products.locator("text=New Product")).to_have_count(0)  # Verify product removed
```

### Why POM is Better

- The test above is long and repetitive.  # Comment: Shows duplication without POM
- Every locator and action is written directly in the test.  # Comment: Hard to maintain
- Any UI change requires editing **every test**.  # Comment: Maintains risk
- Using POM reduces duplication, improves readability, and centralizes maintenance.  # Comment: Cleaner, maintainable code


