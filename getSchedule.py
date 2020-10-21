import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

TESTING = True
def log(str, *args, wait=False, **kwargs):
    '''function to log data only if the script is in TESTING mode'''
    if TESTING:
        print(str, *args, **kwargs)
        if wait:
            input()

def main():

    browser = webdriver.Chrome(input("drag in your Chrome driver : "))
    # browser = webdriver.Chrome(executable_path = '/Users/alansmathew/Desktop/< support file /chromedriver')
  
    #LOAD AJCE LOGIN PORTAL
    browser.get('http://www.aesajce.in/')
    time.sleep(3)

    print('Waiting for user to log in')
    WebDriverWait(browser, 60*3).until(lambda driv:driv.find_elements(By.CLASS_NAME, 'active-sub'))
    print('Accessing information')
    time.sleep(1)
    browser.find_element_by_xpath("//a[contains(@href,'zoomschedule.php')]").click()
    print("Login Sucessfull")
    
    #Detect login to continue to daily schedule

    #Obtain schedule into list/dict
    print("Obtaining data")
    table=browser.find_element_by_id('demo-dt-addrow')  #getting table object
    data_object = table.find_elements_by_tag_name('td') #getting table data objects (td) inside table
    data= [str(data.text) for data in data_object if data.text != '']   #converting / getting data using table data objects
    print(data) #list of datas

    time.sleep(1)

    table_link=browser.find_elements_by_xpath("//a[contains(@title,'room')]")
    link=[str(link.get_attribute('href')) for link in table_link if link.get_attribute('href') != '']
    print(link) #list of links

    #process data



if __name__=='__main__':
    try:
        main()
    except Exception as e: log(e)
    # finally: browser.quit()
