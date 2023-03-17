from page_objects.Base_Page import Base_Page
import conf.locators_conf as locators

class SelectCategory(Base_Page):
    #location of moisturizer and sunscreen button
    moisturizer = locators.buy_moisture_btn
    sunscreen = locators.buy_sunscreen_btn

    
    def select_moisturizer(self):
        # Call the _click method of the base class to click the Buy moisturizers button
        self.click_element(self.moisturizer)

    def select_sunscreen(self):
        # Call the _click method of the base class to click the Buy sunscreens button
        super().click_element(self.sunscreen)