"""
PageFactory uses the factory design pattern.
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. Tutorial main page
2. Tutorial redirect page
3. Contact Page
4. Bitcoin main page
5. Bitcoin price page
"""

from page_objects.moisturizer_page import MoisturizerPage
from page_objects.payment_page import Payment_Page
from page_objects.sunscreen_page import SunscreenPage
from page_objects.zero_page import Zero_Page
from page_objects.main_page import Tutorial_Main_Page
from page_objects.product_menu import Product_Menu
from page_objects.payment_confirmation import Payment_confirmation
import conf.base_url_conf


class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url=conf.base_url_conf.base_url):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        if page_name in ["zero","zero page","agent zero"]:
            test_obj = Zero_Page(base_url=base_url)
        elif page_name == "main page":
            test_obj = Tutorial_Main_Page(base_url=base_url)
        elif page_name == "moisturizer page":
            test_obj = MoisturizerPage(base_url=base_url)
        elif page_name == "sunscreen page":
            test_obj = SunscreenPage(base_url=base_url)    
        elif page_name == "product menu page":
            test_obj = Product_Menu(base_url=base_url)
        elif page_name == "payment page":
            test_obj = Payment_Page(base_url=base_url)
        elif page_name == "payment confirmation":
            test_obj = Payment_confirmation(base_url=base_url)
        return test_obj

    get_page_object = staticmethod(get_page_object)