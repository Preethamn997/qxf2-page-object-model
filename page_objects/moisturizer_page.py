from conf import locators_conf as locator
from page_objects.Base_Page import Base_Page


class MoisturizerPage(Base_Page):
    moisturizer_button = locator.buy_moisture_btn
    def start(self):
        print("moisturizer url")
        self.click_element(self.moisturizer_button)
        