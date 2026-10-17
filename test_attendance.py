
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_mark_attendance():
    driver = webdriver.Chrome()
    try:
        driver.get(os.getenv("ATTENDX_URL", "http://localhost:8000"))

        # Log in using the application's test credentials.
        driver.find_element(By.ID, "username").send_keys(
            os.getenv("ATTENDX_TEST_USER", "test_student")
        )
        driver.find_element(By.ID, "password").send_keys(
            os.getenv("ATTENDX_TEST_PASSWORD", "replace_me")
        )
        driver.find_element(By.ID, "login-button").click()

        # Wait for the attendance page to become available.
        driver.find_element(By.ID, "attendance-menu").click()

        # Mark attendance and verify the displayed status.
        driver.find_element(By.ID, "mark-attendance").click()

        status = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "attendance-status")
            )
        )
        assert "marked" in status.text.lower()
    finally:
        driver.quit()
