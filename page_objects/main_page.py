"""
This class models the main Selenium tutorial page.
URL: selenium-tutorial-main
The page consists of a header, footer, form and table objects
"""
import time

from page_objects.form_object import Form_Object
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Tutorial_Main_Page(Base_Page,Form_Object):
    "Page Object for the weather shopper home page"
    temperature = locators.temperature
    moisturizer = locators.buy_moisture_btn
    sunscreen = locators.buy_sunscreen_btn
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        
        url = '/'
        self.open(url)
     
    @Wrapit._exceptionHandler   
    def read_temperature(self):
        # Call the _get_text method of the base class to get the text of the temperature web element
        temp = self.get_text(self.temperature)
        current_temperature = int(temp.strip().split()[0])
        return current_temperature
        
        
    def select_category(self, current_temperature):    
        if current_temperature < 30:
            page_name = "Moisturizer Page"
        else:
            page_name = "Sunscreen Page"
        
        return page_name
            
        
        

            
        