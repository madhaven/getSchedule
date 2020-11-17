import time
import sys
from os import system
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

TESTING = False
def log(str, *args, wait=False, **kwargs):
    '''function to log data only if the script is in TESTING mode'''
    if TESTING:
        print(str, *args, **kwargs)
        if wait:
            input()


try:
    path = input("drag in your Chrome driver : ")
#    path = '/Users/alansmathew/Desktop/< support file /chromedriver'
#    path = 'D:\\SETUPS\\chromedriver.exe'
    chrome_options = Options()
    chrome_options.add_argument('--log-level=3')

    try:
        #check for a cookie file spec in cli arg or try reading file
        if len(sys.argv)>1:
            exec(open(sys.argv[1], 'r').read())
        else:
            exec(open('cookies.txt','r').read())

    except IOError:
        #cookie file not found: Cookie Creation
        cookiefile = input("Drag and Drop your cookies.txt file here.\nIf you don't have your cookies file, you'll have to press enter to create one.\nThis will ask you to log in and solve a bunch of CAPTCHAS.\ncookies.txt or Enter : ")
        if cookiefile != '':
            exec(open(cookiefile, 'r').read())
        else:
            #fetch cookie from manual user signin
            browser = webdriver.Chrome(
                executable_path = path,
                options = chrome_options
            )
            browser.get("http://www.aesajce.in")
            input('Press Enter here after Loging into your account.')
            browser.get("https://www.aesajce.in/students/zoomschedule.php")
            open("cookies.txt","w").write('global cookies; cookies = '+str(browser.get_cookies()))
            cookies = browser.get_cookies()
            print("cookies downloaded. Yay")
            browser.close()

    except Exception as e:
        log(e, wait=True);exit()

    #open browser and fetch schedule
    if not TESTING: chrome_options.add_argument('headless')
    browser = webdriver.Chrome(
        executable_path = path,
        options = chrome_options
    )
    system('cls')

    print('Fetching Daily Schedule')
    log('loading page')
    browser.get('https://www.aesajce.in/')

    log('loading cookies')
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.get('https://www.aesajce.in/students/zoomschedule.php')
    browser.get('https://www.aesajce.in/students/zoomschedule.php')

    log("obtaining table")
    try:
        table = (browser
            .find_element_by_tag_name('table')
            .find_element_by_tag_name('tbody')
            )
    except NoSuchElementException:
        print('Looks like you have no more classes scheduled')
        raise Exception('noClassException')

    log('obtaining link elements')
    link = table.find_elements_by_tag_name("a")

    log('obtaining details')
    details = [
        [
            td.text
            for td in tr.find_elements_by_tag_name('td')
            if td.text != ''
        ]
        for tr in table.find_elements_by_tag_name('tr')
    ]

    log('obtaining realinks')
    links=[
        str(a.get_attribute('href'))
        for a in link
    ]

    log('Cooking Data\n')
    data = [
        detail[1:-1]+[link]
        for detail, link in zip(details, links)
	if detail[3][:10] == time.strftime('%d-%m-%Y')[:10]
    ]

    browser.close()
    system('cls')
    for subject in data:
        print(*subject, sep='\n', end='\n\n')

except NoSuchElementException as e:
    print('Looks like this program was made for a different version of AES.')
    log(e, wait=True)
except Exception as e:
    if (str(e) != 'noClassException'):
        print('Something Went Wrong')
        log(e, wait=True)

finally:
    input()
    print('Closing Browsing Sessions')
    try: browser.quit()
    except: pass
