import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

TESTING = True
def log(str, *args, wait=False, **kwargs):
    '''function to log data only if the script is in TESTING mode'''
    if TESTING:
        print(str, *args, **kwargs)
        if wait:
            input()

def main(browser):

    # this function is used to wait for certain time to get the page loaded 
    # !note if no connection or page failed to load, after certain recersion the function will quit itself 
    def loading(classname):
        try:
            browser.find_element_by_class_name(classname)
        except:
            time.sleep(1)
            loading(classname)


    #LOAD AJCE LOGIN PORTAL
    browser.get('http://www.aesajce.in/')
    print('Waiting for user to log in')

    #Detect login to continue to daily schedule
    loading('active-sub')
    print('Accessing information')

    # Obtain schedule into list/dict
    # browser.get('http://www.aesajce.in/zoomschedule.php')
    # print('done')
    # time.sleep(20)
    
    #process data

if __name__=='__main__':
    try:
        browser = webdriver.Chrome(input("drag in your Chrome driver : "))
        # browser = webdriver.Chrome(executable_path = '/Users/alansmathew/Desktop/getSchedule/chromedriver')
        main(browser)
        
    except Exception as e: log(e, wait=True)
    finally: browser.quit()
