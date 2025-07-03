from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

# Set Chrome options (disable password manager)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

# Start WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Step 1: Open login page
    driver.get("https://app.phytopian.com/login")
    wait = WebDriverWait(driver, 10)

    # Step 2: Fill Email
    email_input = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "MuiInputBase-input")))
    email_input.send_keys("company@phytopian.com")
    time.sleep(3)

    # Step 3: Fill Password
    password_input = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "MuiInputBase-inputAdornedEnd")))
    password_input.send_keys("12345678")
    time.sleep(3)

    # Step 4: Click Login Button
    login_button = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "MuiButton-containedPrimary")))
    login_button.click()
    time.sleep(5)  # Wait for popup

    # Step 5: Click "OK" on popup using pyautogui
    pyautogui.click(x=856, y=347)  # Adjust if needed
    time.sleep(5)

    # Step 6: Click Avatar (left sidebar)
    avatar_icon = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "MuiAvatar-img")))
    avatar_icon.click()
    time.sleep(5)

    # Step 7: Click Logout button
    logout_button = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "MuiButton-containedError")))
    logout_button.click()
    time.sleep(5)

finally:
    # Step 8: Close browser
    driver.quit()
