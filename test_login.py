
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_student_login():
    driver = webdriver.Chrome()
    try:
        driver.get(os.getenv("ATTENDX_URL", "http://localhost:8000"))

        driver.find_element(By.ID, "username").send_keys(
            os.getenv("ATTENDX_TEST_USER", "test_student")
        )
        driver.find_element(By.ID, "password").send_keys(
            os.getenv("ATTENDX_TEST_PASSWORD", "replace_me")
        )
        driver.find_element(By.ID, "login-button").click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "dashboard")
            )
        )

        assert driver.find_element(By.ID, "dashboard").is_displayed()
    finally:
        driver.quit()
