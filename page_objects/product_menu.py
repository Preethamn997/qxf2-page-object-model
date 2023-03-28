import re
from page_objects.Base_Page import Base_Page
import conf.locators_conf as locators


class Product_Menu(Base_Page):
    add_button_locator = locators.add_button
    product_prices = locators.item_price
    cart_button_locator = locators.click_cart
    
    
    def start(self):
       add_button = self.get_elements(self.add_button_locator)
       self.product_price(add_button)
    
    
    def product_price(self, add_button):
        product_price = self.get_elements(self.product_prices)
        self.lowest_price_product(add_button,product_price)
    
    
    def lowest_price_product(self,add_button,product_price):
        prices = []
        for price in product_price:
            price_text = price.text
            price_value = re.findall(r'\d+', price_text)
            if price_value:
                prices.append(int(price_value[0]))        
        lowest_prices = sorted(prices)[:2]
        self.add_to_cart_lowest_price_product(prices, lowest_prices,add_button)
                
    
    def add_to_cart_lowest_price_product(self, prices, lowest_prices, add_button):
        for price, add_btn in zip(prices, add_button):
            try:
                if price in lowest_prices:
                    add_btn.click()
                    #element = self.get_element(add_btn)
                    print("Clicked on add button for price:", price)
            except Exception as e:
                print("Error clicking add button:", str(e))

        
        
        
        
        