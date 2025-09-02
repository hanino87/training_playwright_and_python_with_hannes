# Playwright: Context, Page, and Frame (Python)

This is a beginner-friendly guide to understand **Browser Contexts, Pages, and Frames** in [Playwright](https://playwright.dev/python/).

---

## What is a Browser Context?

A **Browser Context** in Playwright is like a **new browser session**. Each context has its own cookies, cache, and storage.  
- You can use multiple contexts to test different users **without interference**.  

```text
Browser
 ├── Context 1
 │    └── Page 1
 └── Context 2
      └── Page 2
```

---

## What is a Page?

A **Page** represents a **single tab** in the browser.  
- You can open multiple pages in the same context.  
- Each page can navigate, interact, and take screenshots.

---

## What is a Frame?

A **Frame** is a sub-section of a page, usually inside an `<iframe>`.  
- You can interact with a frame like a page.  
- Frames are useful for testing **embedded content**.

---

## Simple Examples (Python)

### 1. Browser – whole browser instance
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")
    print("Title of example.com:", page.title())
    browser.close()
```

### 2. Context – isolated session inside a browser
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context1 = browser.new_context()
    context2 = browser.new_context()
    page1 = context1.new_page()
    page1.goto("https://www.wikipedia.org")
    print("Context1 page title:", page1.title())
    page2 = context2.new_page()
    page2.goto("https://www.python.org")
    print("Context2 page title:", page2.title())
    browser.close()
```

### 3. Page – a tab inside a context
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page1 = context.new_page()
    page1.goto("https://www.reddit.com")
    print("Page1 title:", page1.title())
    page2 = context.new_page()
    page2.goto("https://news.ycombinator.com")
    print("Page2 title:", page2.title())
    browser.close()
```

### 4. Frame – embedded content inside a page
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.w3schools.com/html/html_iframe.asp")
    frame = page.frame(url=r".*default.asp")
    if frame:
        header = frame.text_content("h1")
        print("Iframe header:", header)
    browser.close()
```

---

## Key Takeaways

- **Browser** → the whole browser instance.  
- **Context** → isolated session inside a browser.  
- **Page** → a tab inside a context.  
- **Frame** → embedded content inside a page.  

Use contexts and pages to simulate multiple users. Use frames to interact with embedded content.

---

## References

- [Playwright Python Docs: Browser Contexts](https://playwright.dev/python/docs/api/class-browsercontext)  
- [Playwright Python Docs: Frames](https://playwright.dev/python/docs/api/class-frame)

