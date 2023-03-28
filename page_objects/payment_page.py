from page_objects.Base_Page import Base_Page
import conf.locators_conf as locators


class Payment_Page(Base_Page):
    pay_with_card_locator = locators.pay_with_card_btn
    payment_form_locator = locators.payment_form
    
    def start(self):
        self.click_element(self.pay_with_card_locator)
        self.switch_to_payment_form()
    
    #def switch_to_payment_form(self):
        #self.switch_frame(name=self.payment_form_locator)
     #   self.switch_frame(name="stripe_checkout_app")
        
    def switch_to_payment_form(self):
        try:
    
            self.switch_frame(name="stripe_checkout_app")
            
        except Exception as e:
            print("Failed to switch to payment form iframe:", str(e))
