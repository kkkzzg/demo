import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected

from settings import SHORT, LONG

class BasePage(object):

    def __init__(self, selenium):
        self.selenium = selenium

    def goto_full_url(self, url):
        return self._selenium_get_url(url)

    def find_element_by_css(self, selector, wait_time=LONG, poll_frequency=SHORT):
        return WebDriverWait(self.selenium, wait_time, poll_frequency).until(
            expected.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def find_elements_by_css(self, selector, wait_time=LONG, poll_frequency=SHORT):
        return WebDriverWait(self.selenium, wait_time, poll_frequency).until(
            expected.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

    def find_elements_by_link_text(self, selector, wait_time=LONG, poll_frequency=SHORT):
        return WebDriverWait(self.selenium, wait_time, poll_frequency).until(
            expected.presence_of_all_elements_located((By.LINK_TEXT, selector)))

    def find_element_by_link_text(self, selector, wait_time=LONG, poll_frequency=SHORT):
        return WebDriverWait(self.selenium, wait_time, poll_frequency).until(
            expected.visibility_of_element_located((By.LINK_TEXT, selector)))

    def find_element_by_id(self, selector, wait_time=LONG, poll_frequency=SHORT):
        return WebDriverWait(self.selenium, wait_time, poll_frequency).until(
            expected.visibility_of_element_located((By.ID, selector)))

    def find_element_by_xpath(self, selector, wait_time=LONG, poll_frequency=SHORT):
        return WebDriverWait(self.selenium, wait_time, poll_frequency).until(
            expected.visibility_of_element_located((By.XPATH, selector)))

    def find_element_by_name(self, selector, wait_time=LONG, poll_frequency=SHORT):
        return WebDriverWait(self.selenium, wait_time, poll_frequency).until(
            expected.visibility_of_element_located((By.NAME, selector)))

    def find_elements_by_xpath(self, selector, wait_time=LONG, poll_frequency=SHORT):
        return WebDriverWait(self.selenium, wait_time, poll_frequency).until(
            expected.presence_of_all_elements_located((By.XPATH, selector)))

    def find_sub_element_by_css(self, selector, elem):
        return elem.find_element(By.CSS_SELECTOR, selector)

    def find_sub_elements_by_css(self, selector, elem):
        return elem.find_elements(By.CSS_SELECTOR, selector)

    def _selenium_get_url(self, url):
        try:
            self.selenium.get(str(url))
        except Exception as ex:
            print "Can not open the url:[{}]".format(url)
            raise ex
        return self

    def take_snapshot(self):
        file_name = 'finish.png'
        self.selenium.save_screenshot(os.path.join(os.getcwd(), file_name))
