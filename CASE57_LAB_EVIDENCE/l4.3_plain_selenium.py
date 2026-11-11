from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By


FIXTURE = Path(__file__).with_name("l4.3_validator_fixture.html").resolve()
SCREENSHOT = Path(__file__).with_name("L4.3_plain_selenium.png")


def main():
    driver = webdriver.Chrome()
    try:
        driver.get(FIXTURE.as_uri())

        driver.find_element(By.ID, "daily").send_keys("10")
        driver.find_element(By.ID, "weekly").send_keys("60")
        driver.find_element(By.ID, "rest").send_keys("10")
        driver.find_element(By.ID, "submit").click()
        assert driver.find_element(By.ID, "result").text == "Duty schedule accepted."
        driver.save_screenshot(str(SCREENSHOT))
        print("Plain Selenium boundary case: PASS")

        driver.find_element(By.ID, "daily").clear()
        driver.find_element(By.ID, "daily").send_keys("10.5")
        driver.find_element(By.ID, "weekly").clear()
        driver.find_element(By.ID, "weekly").send_keys("40")
        driver.find_element(By.ID, "rest").clear()
        driver.find_element(By.ID, "rest").send_keys("12")
        driver.find_element(By.ID, "submit").click()
        assert driver.find_element(By.ID, "result").text == "Daily duty limit exceeded."
        print("Plain Selenium daily violation: PASS")
        print("Screenshot:", SCREENSHOT.name)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
