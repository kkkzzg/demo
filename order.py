from selenium import webdriver
import settings
from pages.login_page import LoginPage
from pages.order_page import OrderPage
import sys


def set_up_browser():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("focusmanager.testmode", True)
    profile.set_preference("dom.max_script_run_time", 600)
    profile.set_preference('network.http.phishy-userpass-length', 255)
    selenium = webdriver.Firefox(firefox_profile=profile)
    selenium.implicitly_wait(settings.LONG)
    return selenium


def close_browser(selenium):
    selenium.quit()


class OrderSystem(object):

    def __init__(self):
        self.selenium = set_up_browser()

    def prepare(self):
        login_page = LoginPage(self.selenium).goto_full_url(settings.URL)
        login_page.login(settings.USER, settings.PASSWORD)

    def order_dish(self, dish_type):
        order_page = OrderPage(self.selenium)
        try:
            self.prepare()
            func = {
                settings.DishType.lunch: order_page.select_lunch,
                settings.DishType.breakfast: order_page.select_breakfast,
            }
            func[dish_type]()
            order_page.click_random_dish()
            order_page.click_cart()
            order_page.select_deliver_floor()
            order_page.click_billing()
        finally:
            order_page.take_snapshot()
            close_browser(self.selenium)

if __name__ == '__main__':
    try:
        dish_type = int(sys.argv[1])
        OrderSystem().order_dish(dish_type)
    except (IndexError, ValueError):
        print "2 for lunch, 1 for breakfast?"