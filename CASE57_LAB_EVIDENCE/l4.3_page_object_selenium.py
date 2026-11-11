from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By


FIXTURE = Path(__file__).with_name("l4.3_validator_fixture.html").resolve()
SCREENSHOT = Path(__file__).with_name("L4.3_page_object_selenium.png")


class DutyValidatorPage:
    DAILY = (By.ID, "daily")
    WEEKLY = (By.ID, "weekly")
    REST = (By.ID, "rest")
    SUBMIT = (By.ID, "submit")
    RESULT = (By.ID, "result")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(FIXTURE.as_uri())

    def validate(self, daily, weekly, rest):
        for locator, value in (
            (self.DAILY, daily),
            (self.WEEKLY, weekly),
            (self.REST, rest),
        ):
            field = self.driver.find_element(*locator)
            field.clear()
            field.send_keys(str(value))
        self.driver.find_element(*self.SUBMIT).click()
        return self.driver.find_element(*self.RESULT).text


def main():
    driver = webdriver.Chrome()
    try:
        page = DutyValidatorPage(driver)
        page.load()

        assert page.validate(10, 60, 10) == "Duty schedule accepted."
        driver.save_screenshot(str(SCREENSHOT))
        print("POM boundary case: PASS")

        assert page.validate(10.5, 40, 12) == "Daily duty limit exceeded."
        print("POM daily violation: PASS")
        print("Screenshot:", SCREENSHOT.name)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
