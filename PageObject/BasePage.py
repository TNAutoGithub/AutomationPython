from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_is_visible(self, xpath, time_out):
        wait = WebDriverWait(self.driver, time_out)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH,xpath)))
    def wait_until_page_contains_element(self, xpath, time_out):
        wait = WebDriverWait(self.driver, time_out)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,xpath)))
    def wait_element_is_not_visible(self, xpath, time_out):
        wait = WebDriverWait(self.driver, time_out)
        wait.until(expected_conditions.invisibility_of_element_located((By.XPATH,xpath)))

    def click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()
    def submit(self, xpath):
        self.driver.find_element_by_xpath(xpath).submit()
    def enter(self, xpath, text):
        driver = self.driver
        driver.find_element_by_xpath(xpath).send_keys(text)
        