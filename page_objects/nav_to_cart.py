from page_objects.Base_Page import Base_Page
import conf.locators_conf as locators


class Cart(Base_Page):
    cart_button_locator = locators.click_cart
    
    def start(self):
        self.click_element(self.cart_button_locator)    