"""
This class models the form on the Selenium tutorial page
The form consists of some input fields, a dropdown, a checkbox and a button
"""


import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Form_Object():
    "Page object for the Form"

    #locators 
    email_field = locators.e_mail_field
    card_num_field = locators.card_num_field
    expiry_date_field = locators.expiry_date_field
    ccv_no_field = locators.ccv_no_field
    zipcode_field = locators.zipcode_field
    payment_button = locators.payment_button
        
        
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_email(self,email):
        "Set the email on the form"
        result_flag = self.set_text(self.email_field,email)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%email,
            negative='Failed to set the email in the form',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_card_no(self,card_no):
        "Set the card number on the form"
        #for card_num in card_no:    
        result_flag = self.set_text_list(self.card_num_field,card_no)
        self.conditional_write(result_flag,
            positive='Set the card number to: %s'%card_no,
            negative='Failed to set the card number in the form',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_expiry(self,expiry_date):   
        "Set the expiry date on the form"
        #for date in expiry_date:
        result_flag = self.set_text_list(self.expiry_date_field, expiry_date)
        self.conditional_write(result_flag,
            positive='Set the expiry date to: %s'%expiry_date,
            negative='Failed to set the expiry date in the form',
            level='debug')

        return result_flag
    
    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_ccv(self,ccv):
        "Set the ccv on the form"
        result_flag = self.set_text(self.ccv_no_field,ccv)
        self.conditional_write(result_flag,
            positive='Set the ccv to: %s'%ccv,
            negative='Failed to set the ccv in the form',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_zipcode(self,zcode):
        "Set the zipcode on the form"
        result_flag = self.set_text(self.zipcode_field,zcode)
        self.conditional_write(result_flag,
            positive='Set the zipcode to: %s'%zcode,
            negative='Failed to set the zipcode in the form',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_pay(self):
        "Click on 'Pay' button"
        result_flag = self.click_element(self.payment_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "Pay" button',
            negative='Failed to click on "Pay" button',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def submit_form(self,email,card_no,exipiry_date,ccv,zcode):
        "Submit the form"
        result_flag = self.set_email(email)
        result_flag &= self.set_card_no(card_no)
        result_flag &= self.set_expiry(exipiry_date)
        result_flag &= self.set_ccv(ccv)
        result_flag &= self.set_zipcode(zcode)
        result_flag &= self.click_pay()

        return result_flag
    
    


