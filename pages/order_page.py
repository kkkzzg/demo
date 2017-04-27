import time
from selenium.common.exceptions import TimeoutException
import settings
from pages.base_page import BasePage
from random import choice


class OrderPage(BasePage):

    def select_breakfast(self):
        self.find_elements_by_css('.vertical_text')[0].click()

    def select_lunch(self):
        self.find_elements_by_css('.vertical_text')[1].click()

    def get_my_popular_dish_table_element(self):
        try:
            return self.find_element_by_id('user_regular_dish_revision_list')
        except TimeoutException:
            pass

    def get_my_popular_dish_elements(self):
        table_element = self.get_my_popular_dish_table_element()
        return [] if not table_element else self.find_sub_elements_by_css('.name', table_element)

    def get_popular_dish_table_element(self):
        try:
            return self.find_element_by_id('regular_dish_revision_list')
        except TimeoutException:
            pass

    def get_popular_dish_elements(self):
        table_element = self.get_popular_dish_table_element()
        return [] if not table_element else self.find_sub_elements_by_css('.name', table_element)

    def click_random_dish(self):
        try:
            element = choice(self.get_my_popular_dish_elements() + self.get_popular_dish_elements())
        except IndexError:
            raise RuntimeError('No dishes found.')
        for index in range(3):
            try:
                self.selenium.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(1)
                element.click()
                break
            except Exception:
                continue

    def click_cart(self):
        self.find_element_by_id('cart').click()

    def get_all_deliver_location_elements(self):
        return self.find_elements_by_css('#corp_pick_up_location div div')

    def select_deliver_floor(self):
        deliver_location_elements = self.get_all_deliver_location_elements()
        for deliver_location_element in deliver_location_elements:
            if settings.FLOOR in deliver_location_element.text:
                deliver_location_element.click()
            break
        else:
            raise RuntimeError('Could not find the location you want')

    def click_billing(self):
        self.find_element_by_id('corp_add_order_btn').click()
        time.sleep(1)  # wait for the billing finish
