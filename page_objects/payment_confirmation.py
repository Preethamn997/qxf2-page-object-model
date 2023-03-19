from page_objects.Base_Page import Base_Page
from conf import locators_conf as locator


class Payment_confirmation(Base_Page):
    payment_status = locator.check_payment_status
    def start(self):
        try:
            status = self.get_text(self.payment_status)
            print(status)
            assert "PAYMENT SUCCESS" in status, "Test failed"
        except Exception as e:
            print(f"An error occurred while checking the payment status: {e}")
        else:
            print("Test passed")
    