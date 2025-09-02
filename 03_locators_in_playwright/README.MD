# Playwright Locators: Without Semantic vs Semantic Styles

## Introduction

Playwright provides multiple ways to locate elements on a web page:
- **Semantic Locators:** Use the intent or role of elements, like buttons, links, or text. They are human-readable and more resilient to UI changes.
- **CSS Locators:** Use CSS selectors to target elements based on their classes, IDs, or hierarchy in the DOM. They are precise but more brittle when UI changes.

## Playwright Locators Without Semantic Styles

```python
# --- ID locator ---
element_by_id = page.locator("#signup")
element_by_id.click()

# --- XPath locator ---
element_by_xpath = page.locator('//input[@placeholder="Username"]')
element_by_xpath.fill("my_username")

# --- Class locator ---
element_by_class = page.locator(".button-primary")
element_by_class.click()

# --- Text locator (button or link text) ---
element_by_text = page.locator('text="Login"')
element_by_text.click()

# --- Text locator using :has-text() ---
element_by_text = page.locator('button:has-text("Login")')
element_by_text.click()

# --- Name attribute locator ---
element_by_name = page.locator('input[name="email"]')
element_by_name.fill("test@example.com")
```

## Playwright Semantic Style Locators

**Advantage:**
If someone changes your button HTML from `<button class="button-primary">Create Product</button>` → `<button class="btn btn-success">Create Product</button>`, your old CSS locator breaks, but `get_by_role("button", name="Create Product")` will still work because it relies on the **accessible role & name** instead of styling.

```python
# --- ID locator (semantic style) ---
element_by_id = page.get_by_id("signup")  # replaces: page.locator("#signup")
element_by_id.click()

# --- Placeholder locator (semantic style) ---
element_by_placeholder = page.get_by_placeholder("Username")  # replaces: page.locator('//input[@placeholder="Username"]')
element_by_placeholder.fill("my_username")

# --- Role-based locator for button ---
element_by_role_button = page.get_by_role("button", name="Submit")  # replaces: page.locator(".button-primary") if button text is "Submit"
element_by_role_button.click()

# --- Text locator (semantic style) ---
element_by_text = page.get_by_text("Login")  # replaces: page.locator('text="Login"')
element_by_text.click()

# --- Role + text (better than :has-text) ---
element_by_role_text = page.get_by_role("button", name="Login")  # replaces: page.locator('button:has-text("Login")')
element_by_role_text.click()

# --- Name attribute locator (semantic style) ---
element_by_label = page.get_by_label("Email")  # replaces: page.locator('input[name="email"]')
element_by_label.fill("test@example.com")
```

**Key Takeaway:**
- **Semantic locators** are more resilient and readable.
- **CSS/XPath/text locators** may break if UI styling or structure changes.


