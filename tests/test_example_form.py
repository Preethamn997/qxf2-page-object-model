"""
This is an example automated test to help you learn Qxf2's framework
Our automated test will do the following:
    #Open Qxf2 selenium-tutorial-main page.
    #Fill the example form.
    #Click on Click me! button and check if its working fine.
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.payment_form_data as conf
import conf.testrail_caseid_conf as testrail_file
import pytest



@pytest.mark.GUI
def test_example_form(test_obj):

    "Run the test"
    try:
        expected_pass = 0
        actual_pass = -1
        test_obj = PageFactory.get_page_object("Main Page", base_url=test_obj.base_url)
        temperature = test_obj.read_temperature()
        print("The temperature is: ", temperature)
        page_name = test_obj.select_category(temperature)
        print("page name is", page_name)
        PageFactory.get_page_object(page_name, base_url=test_obj.base_url) 
        PageFactory.get_page_object("Product Menu Page", base_url=test_obj.base_url)
        PageFactory.get_page_object("Cart", base_url=test_obj.base_url)
        PageFactory.get_page_object("Payment Page", base_url=test_obj.base_url)
        PageFactory.get_page_object("Payment Form Object", base_url=test_obj.base_url)
        
    
         
        #Set start_time with current time
        start_time = int(time.time())

        # Turn on the highlighting feature
        test_obj.turn_on_highlight()

        #4. Get the test details from the conf file
        email = conf.user_email
        card_number = conf.card_number
        expiry_date = conf.card_expiry
        ccv = conf.c_c_v
        zipcode = conf.zcode
        

        #5. Set email in form
        result_flag = test_obj.set_email(email)
        test_obj.log_result(result_flag,
                            positive="email was successfully set to: %s\n"%email,
                            negative="Failed to set email: %s \nOn url: %s\n"%(email,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        #Update TestRail
        #case_id = testrail_file.test_example_form_name
        #test_obj.report_to_testrail(case_id,test_obj.test_run_id,result_flag)
        #test_obj.add_tesults_case("Set email", "Sets the email in the form", "test_example_form", result_flag, "Failed to email: %s \nOn url: %s\n"%(email,test_obj.get_current_url()), [test_obj.log_obj.log_file_dir + os.sep + test_obj.log_obj.log_file_name])
        
        
        #6. Set Card number in form
        result_flag = test_obj.set_card_no(card_number)
        test_obj.log_result(result_flag,
                            positive="card number was successfully set to: %s\n"%card_number,
                            negative="Failed to set card number: %s \nOn url: %s\n"%(card_number,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        #Update TestRail
        #case_id = testrail_file.test_example_form_email
        #test_obj.report_to_testrail(case_id,test_obj.test_run_id,result_flag)
        #test_obj.add_tesults_case("Set card number", "Sets the card number in the form", "test_example_form", result_flag, "Failed to set Card number: %s \nOn url: %s\n"%(card_number,test_obj.get_current_url()), [], {'Email': email}, {'_Email': email})


        #7. Set Phone number in form
        result_flag = test_obj.set_expiry(expiry_date)
        test_obj.log_result(result_flag,
                            positive="Expiry date was successfully set for phone: %s\n"%expiry_date,
                            negative="Failed to set expiry date: %s \nOn url: %s\n"%(expiry_date,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        #Update TestRail
        #case_id = testrail_file.test_example_form_phone
        #test_obj.report_to_testrail(case_id,test_obj.test_run_id,result_flag)
        #test_obj.add_tesults_case("Set expiry date", "Sets the expiry date in the form", "test_example_form", result_flag, "Failed to set phone number: %s \nOn url: %s\n"%(expiry_date,test_obj.get_current_url()), [], {}, {'_Phone': phone, '_AnotherCustomField': 'Custom field value'})


        #8. Set ccv in form
        result_flag = test_obj.set_ccv(ccv)
        test_obj.log_result(result_flag,
                            positive= "ccv was successfully set to: %s\n"%ccv,
                            negative="Failed to set ccv: %s \nOn url: %s\n"%(ccv,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        #Update TestRail
        #case_id = testrail_file.test_example_form_gender
        #test_obj.report_to_testrail(case_id,test_obj.test_run_id,result_flag)
        #test_obj.add_tesults_case("Set ccv", "Sets the ccv in the form", "test_example_form", result_flag, "Failed to set gender: %s \nOn url: %s\n"%(ccv,test_obj.get_current_url()), [])


        #8. Set zipcode in form
        result_flag = test_obj.set_zipcode(zipcode)
        test_obj.log_result(result_flag,
                            positive= "zipcode was successfully set to: %s\n"%zipcode,
                            negative="Failed to set zipcode: %s \nOn url: %s\n"%(zipcode,test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        #Update TestRail
        #case_id = testrail_file.test_example_form_gender
        #test_obj.report_to_testrail(case_id,test_obj.test_run_id,result_flag)
        #test_obj.add_tesults_case("Set zipcode", "Sets the zipcode in the form", "test_example_form", result_flag, "Failed to set zipcode: %s \nOn url: %s\n"%(zipcode,test_obj.get_current_url()), [])

        #10. Set and submit the form in one go
        result_flag = test_obj.submit_form(email,card_number,expiry_date,ccv,zipcode)
        test_obj.log_result(result_flag,
                            positive="Successfully submitted the form\n",
                            negative="Failed to submit the form \nOn url: %s"%test_obj.get_current_url(),
                            level="critical")

        #Update TestRail
        #case_id = testrail_file.test_example_form
        #test_obj.report_to_testrail(case_id,test_obj.test_run_id,result_flag)
        #test_obj.add_tesults_case("Submit Form", "Submits the form", "test_example_form", result_flag,"Failed to submit the form \nOn url: %s"%test_obj.get_current_url(), [])

        #Turn off the highlighting feature
        #test_obj.turn_off_highlight()

        #11. Check the heading on the redirect page
        #Notice you don't need to create a new page object!
        #if result_flag is True:
         #   result_flag = test_obj.check_heading()
        #test_obj.log_result(result_flag,
        #                    positive="Heading on the redirect page checks out!\n",
        #                    negative="Fail: Heading on the redirect page is incorrect!")
        #test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        #test_obj.add_tesults_case("Check Heading", "Checks the heading on the redirect page", "test_example_form", result_flag,"Fail: Heading on the redirect page is incorrect!", [])

         # Turn on the highlighting feature
        #test_obj.turn_on_highlight()

        
        #13. Print out the result
        #test_obj.write_test_summary()
        #expected_pass = test_obj.result_counter
        #actual_pass = test_obj.pass_counter

    except Exception as e:
        #print("Exception when trying to run test: %s"%__file__)
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

        test_example_form(test_obj)

        #teardowm
        test_obj.wait(3)
        test_obj.teardown()
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())
