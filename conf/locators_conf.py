#Common locator file for all locators

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

# Define class variables for the web elements
buy_moisture_btn = "xpath,//button[text()='Buy moisturizers']"
buy_sunscreen_btn = "xpath,//button[text()='Buy sunscreens']"
add_button = "xpath,//button[contains(text(),'Add')]"
item_price = "xpath,//div[@class='container']//div//p[2]"
temperature = "xpath,//span[@id='temperature']"

pay_with_card_btn = "xpath,//*[contains(text(),'Pay with Card')]"
payment_form = "xpath,//iframe[@name='stripe_checkout_app']"
form_heading = "xpath,//h1[contains(text()='Stripe.com']"

#Locators for product_menu.py
add_button = "xpath,//button[contains(text(),'Add')]"
item_price = "xpath,//div[@class='container']//div//p[2]"
click_cart = "xpath,//*[@class= 'thin-text nav-link']"

#locators for payment form fields
e_mail_field = "xpath,//input[@id='email']"
card_num_field = "xpath,//input[@id='card_number']"
expiry_date_field = "xpath,//input[@id='cc-exp']"
ccv_no_field = "xpath,//input[@id='cc-csc']"
zipcode_field = "xpath,//input[@id='billing-zip']"
payment_button = "xpath,//button[@id='submitButton']"
check_payment_status= "xpath,//*[@class='row justify-content-center']//h2"

