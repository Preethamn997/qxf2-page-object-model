"""
The program is designed to automate the process of purchasing beauty products from 
the website https://weathershopper.pythonanywhere.com/ using Selenium web driver based on the temperature displayed
on the website. The program opens the website in a Chrome browser and selects moisturizers
and adds items to the cart if the temperature is less than 30 degrees Celsius. 
If the temperature is 30 degrees Celsius or higher, the program selects sunscreens and adds items to the cart.
The program then opens the cart, fills in the payment form, and completes the payment process. 
Finally, the program checks the payment status and prints the message "PAYMENT SUCCESS" if the payment is successful.
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.payment_form_data as conf
import pytest


@pytest.mark.GUI
def test_weather_shopper(test_obj):

    "Run the test"
    try:
        expected_pass = 0
        actual_pass = -1
        test_obj = PageFactory.get_page_object("Main Page", base_url=test_obj.base_url)
        temperature = test_obj.read_temperature()
        page_name = test_obj.select_category(temperature)
        PageFactory.get_page_object(page_name, base_url=test_obj.base_url) 
        PageFactory.get_page_object("Product Menu Page", base_url=test_obj.base_url)
        PageFactory.get_page_object("Cart", base_url=test_obj.base_url)
        PageFactory.get_page_object("Payment Page", base_url=test_obj.base_url)
        PageFactory.get_page_object("Payment Form Object", base_url=test_obj.base_url)
        

        #Set start_time with current time
        start_time = int(time.time())


        # Turn on the highlighting feature
        test_obj.turn_on_highlight()


        # Get the test details from the conf file
        email = conf.user_email
        card_number = conf.card_number
        expiry_date = conf.card_expiry
        ccv = conf.c_c_v
        zipcode = conf.zcode
        

        # Set email in form
        result_flag = test_obj.set_email(email)
        test_obj.log_result(result_flag,
                            positive="email was successfully set to: %s\n"%email,
                            negative="Failed to set email: %s \nOn url: %s\n"%(email,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        
        # Set Card number in form
        result_flag = test_obj.set_card_no(card_number)
        test_obj.log_result(result_flag,
                            positive="card number was successfully set to: %s\n"%card_number,
                            negative="Failed to set card number: %s \nOn url: %s\n"%(card_number,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        

        # Set Expiry date in form
        result_flag = test_obj.set_expiry(expiry_date)
        test_obj.log_result(result_flag,
                            positive="Expiry date was successfully set for : %s\n"%expiry_date,
                            negative="Failed to set expiry date: %s \nOn url: %s\n"%(expiry_date,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        

        # Set ccv in form
        result_flag = test_obj.set_ccv(ccv)
        test_obj.log_result(result_flag,
                            positive= "ccv was successfully set to: %s\n"%ccv,
                            negative="Failed to set ccv: %s \nOn url: %s\n"%(ccv,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        

        #Set zipcode in form
        result_flag = test_obj.set_zipcode(zipcode)
        test_obj.log_result(result_flag,
                            positive= "zipcode was successfully set to: %s\n"%zipcode,
                            negative="Failed to set zipcode: %s \nOn url: %s\n"%(zipcode,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        

        #Set and submit the form in one go
        result_flag = test_obj.submit_form(email,card_number,expiry_date,ccv,zipcode)
        test_obj.log_result(result_flag,
                            positive="Successfully submitted the form\n",
                            negative="Failed to submit the form \nOn url: %s"%test_obj.get_current_url(),
                            level="critical")
        
        PageFactory.get_page_object("payment confirmation", base_url=test_obj.base_url)
                
         # Turn on the highlighting feature
        test_obj.turn_on_highlight()

        
        # Print out the result
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter


    except Exception as e:
        print("Exception when trying to run test: %s"%__file__)
        print("Python says:%s"%str(e))


    assert expected_pass == actual_pass, "Test failed: %s"%__file__


#---START OF SCRIPT
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()

    #Run the test only if the options provided are valid
    if options_obj.check_options(options):
        test_obj = PageFactory.get_page_object("Zero", base_url=test_obj.base_url)

        #Setup and register a driver
        test_obj.register_driver(options.remote_flag,options.os_name,options.os_version,options.browser,options.browser_version,options.remote_project_name,options.remote_build_name)

        #Setup TestRail reporting
        if options.testrail_flag.lower()=='y':
            if options.test_run_id is None:
                test_obj.write('\033[91m'+"\n\nTestRail Integration Exception: It looks like you are trying to use TestRail Integration without providing test run id. \nPlease provide a valid test run id along with test run command using -R flag and try again. for eg: pytest -X Y -R 100\n"+'\033[0m')
                options.testrail_flag = 'N'
            if options.test_run_id is not None:
                test_obj.register_testrail()
                test_obj.set_test_run_id(options.test_run_id)

        if options.tesults_flag.lower()=='y':
            test_obj.register_tesults()

        test_weather_shopper(test_obj)

        #teardowm
        test_obj.wait(3)
        test_obj.teardown()
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())
