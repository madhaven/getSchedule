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

    #LOAD AJCE LOGIN PORTAL
    browser.get('http://www.ajce.in/') #not sure about urls
    print('Waiting for user to log in')

    #Detect login to continue to daily schedule

    #Obtain schedule into list/dict

    #process data

if __name__=='__main__':
    try:
        main()
    except Exception as e: log(e)
    finally: browser.quit()
