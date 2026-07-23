
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException

import time

# -----------------------------
# Browser Setup
# -----------------------------

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://www.lambdatest.com/selenium-playground")

# =====================================================
# TASK 1
# =====================================================

print("\nTASK 1")

# Open Simple Form Demo
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

# Wait for page
wait.until(
    EC.visibility_of_element_located(
        (By.ID, "user-message")
    )
)

print("\nLocator Examples")

# -----------------------------
# By.ID
# -----------------------------

textbox = driver.find_element(By.ID, "user-message")
textbox.clear()
textbox.send_keys("Testing using ID")

# -----------------------------
# By.NAME
# -----------------------------

textbox = driver.find_element(By.NAME, "user-message")
textbox.clear()
textbox.send_keys("Testing using NAME")

# -----------------------------
# By.CLASS_NAME
# -----------------------------

textbox = driver.find_element(By.CLASS_NAME, "form-control")
textbox.clear()
textbox.send_keys("Testing using CLASS")

# -----------------------------
# By.TAG_NAME
# -----------------------------

textbox = driver.find_element(By.TAG_NAME, "input")
textbox.clear()
textbox.send_keys("Testing using TAG")

# -----------------------------
# Absolute XPath
# -----------------------------

textbox = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/section[2]/div/div/div[1]/div/input"
)

textbox.clear()
textbox.send_keys("Absolute XPath")

# -----------------------------
# Relative XPath
# -----------------------------

textbox = driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)

textbox.clear()
textbox.send_keys("Relative XPath")

print("All Locator Strategies Executed Successfully")

# =====================================================
# CSS SELECTORS
# =====================================================

print("\nCSS Selectors")

# CSS by ID
driver.find_element(
    By.CSS_SELECTOR,
    "#user-message"
)

# CSS by Attribute
driver.find_element(
    By.CSS_SELECTOR,
    "input[name='user-message']"
)

# Parent Child CSS
driver.find_element(
    By.CSS_SELECTOR,
    "div > input"
)

print("CSS Selectors Verified")

# =====================================================
# CHECKBOX DEMO
# =====================================================

driver.get("https://www.lambdatest.com/selenium-playground")

driver.find_element(
    By.LINK_TEXT,
    "Checkbox Demo"
).click()

wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//label[text()='Option 1']")
    )
)

# XPath text()

option1 = driver.find_element(
    By.XPATH,
    "//label[text()='Option 1']"
)

print(option1.text)

# XPath contains()

options = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)

print("Checkbox Labels")

for option in options:
    print(option.text)

# =====================================================
# TASK 2
# =====================================================

print("\nTASK 2")

driver.get("https://www.lambdatest.com/selenium-playground")

driver.find_element(
    By.LINK_TEXT,
    "Bootstrap Alerts"
).click()

# Explicit Wait

button = wait.until(

    EC.element_to_be_clickable(

        (By.CSS_SELECTOR,
         ".btn-success")

    )

)

button.click()

success_alert = wait.until(

    EC.visibility_of_element_located(

        (By.CSS_SELECTOR,
         ".alert-success")

    )

)

assert "success" in success_alert.text.lower()

print("Explicit Wait Passed")

# =====================================================
# time.sleep() Comparison
# =====================================================

print("\nSleep vs Explicit Wait")

start = time.time()

time.sleep(3)

end = time.time()

print("Sleep Time")

print(end - start)

start = time.time()

wait.until(

    EC.visibility_of_element_located(

        (By.CSS_SELECTOR,
         ".alert-success")

    )

)

end = time.time()

print("Explicit Wait Time")

print(end - start)

# =====================================================
# element_to_be_clickable()
# =====================================================

button = wait.until(

    EC.element_to_be_clickable(

        (By.CSS_SELECTOR,
         ".btn-success")

    )

)

print("Button is Clickable")

# =====================================================
# Fluent Wait
# =====================================================

print("\nFluent Wait")

fluent_wait = WebDriverWait(

    driver,

    timeout=10,

    poll_frequency=0.5,

    ignored_exceptions=[NoSuchElementException]

)

fluent_wait.until(

    EC.presence_of_element_located(

        (By.CSS_SELECTOR,
         ".alert-success")

    )

)

print("Fluent Wait Successful")

driver.quit()

print("\nExecution Completed Successfully")