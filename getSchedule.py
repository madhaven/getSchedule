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

def main():

    browser = webdriver.Chrome(input("drag in your Chrome driver : "))
    # browser = webdriver.Chrome(executable_path = '/Users/alansmathew/Desktop/getSchedule/chromedriver')

    # this function is used to wait for certain time to get the page loaded 
    # !note if no connection or page failed to load, after certain recersion the function will quit itself 
    def loading(classname):
        try:
            browser.find_element_by_class_name(classname)
        except:
            time.sleep(1)
            loading(classname)


    #LOAD AJCE LOGIN PORTAL
    browser.get('http://www.aesajce.in/') #not sure about urls
    time.sleep(3)

    print('Waiting for user to log in')
    loading('active-sub')

    browser.get('http://www.aesajce.in/zoomschedule.php')
    print('done')
    time.sleep(20)

    

    #Detect login to continue to daily schedule

    #Obtain schedule into list/dict

    #process data

if __name__=='__main__':
    try:
        main()
    except Exception as e: log(e)
    # finally: browser.quit()
