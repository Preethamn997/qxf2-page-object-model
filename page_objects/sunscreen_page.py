from page_objects.Base_Page import Base_Page
from conf import locators_conf as locator


class SunscreenPage(Base_Page):
    sunscreen_button = locator.buy_sunscreen_btn
    
    def start(self):
        self.click_element(self.sunscreen_button)