from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# -----------------------------
# Task 1
# -----------------------------

options = webdriver.ChromeOptions()

# Headless mode
options.add_argument("--headless=new")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Implicit Wait
driver.implicitly_wait(10)

driver.get("https://www.lambdatest.com/selenium-playground")

print("Page Title:")
print(driver.title)

# -----------------------------
# Task 2
# -----------------------------

# Navigate to Simple Form Demo
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

assert "simple-form-demo" in driver.current_url

print("URL Verified")
print(driver.current_url)

# Navigate Back
driver.back()

# Open Google in new tab
driver.execute_script("window.open('https://www.google.com');")

# Window Handles
windows = driver.window_handles


print("Available Windows:", windows)

driver.switch_to.window(windows[1])

print("Google Title:")
print(driver.title)

# Switch Back
driver.switch_to.window(windows[0])

# Resize Window
driver.set_window_size(1280, 800)

# Take Screenshot
driver.save_screenshot("playground_screenshot.png")

print("Screenshot Saved")

time.sleep(2)

driver.quit()

print("Execution Completed Successfully")