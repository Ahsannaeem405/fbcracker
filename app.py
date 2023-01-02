# ---------------> Import <-----------------
import os, datetime, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime
import configparser
from sys import argv
import random
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=r'chromedriver.exe')  # to open the chromebrowser

# ---------------> Env <-----------------
os.environ["DEBUSSY"] = "1"
# ---------------> Configure browser session <-----------------
def create_browser():
    browser = driver
    return browser
# ---------------> Ask user to log in <-----------------
def fb_login(credentials):
    email = 'cosmosic19@gmail.com'
    password = 'Raptor11122@@'
    browser.get("https://facebook.com/")
    print("[*] Logging to the fb account...")
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('pass').send_keys(password)
    browser.find_element_by_name('login').click()
# ---------------> Scroll to bottom of the page <-----------------
def scroll_to_bottom():
    try:
        while browser.find_element_by_css_selector('#m_more_friends'):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.2)
    except:
        pass
# ---------------> Get list of all friends on page <---------------
def scan_friends():
    print('[*] Scanning the page for friends...')
    friends = []
    friend_cards = browser.find_elements_by_css_selector("div#root div.timeline div[data-sigil='undoable-action'] a")
    friend_mutual_cards = browser.find_elements_by_css_selector("div#root div.timeline div[data-sigil='undoable-action'] [data-sigil='m-add-friend-source-replaceable']")
    index = 0
    for friend in friend_cards:
        friend_name = friend.text
        friend_id = friend.get_attribute('href')
        if friend_id is not None: friend_id = friend_id.split("/")[-1]
        if friend_name:
            friends.append({
                'name': friend_name, #to prevent CSV writing issues .encode('utf-8', 'ignore')
                'id': friend_id
            })
        index += 1
    index = 0
    
    print('[+] Found %r friends on page!' % len(friends))
    print(friends)
    return friends
# -----------------> Load list from CSV <-----------------

def scrape_1st_degrees():


    #Get my Facebook id
    print("[*] Scanning for my ID...")
    time.sleep(1)
    browser.get("https://m.facebook.com/home.php")
    time.sleep(1)
    profile_icon = browser.find_element_by_css_selector("[id='profile_tab_jewel'] > a")
    myid = profile_icon.get_attribute("href").split("?")[0]
    time.sleep(1)

    #Scan your Friends page (1st-degree friends)
    print("[*] Opening the friends page...")
    browser.get("https://m.facebook.com/ahsan.naeem.9484/friends")
    time.sleep(2)
    print("[*] Scrolling...")
    scroll_to_bottom()
    time.sleep(2)
    myfriends = scan_friends()
    return

# ---------------> Vars [2] <---------------
now = datetime.now()
configPath = "config.txt"
# ---------------> Funcs <---------------
def get_config(configPath):
    configObj = configparser.ConfigParser()
    configObj.read(configPath)
    email = configObj.get('credentials', 'email')
    password = configObj.get('credentials', 'password')
    return configObj
def login_from_config():
    fb_login(get_config(configPath))
# ---------------> Main <---------------


if len(argv) >= 1 and len(argv) <= 3:
    browser = create_browser()

def main():

 login_from_config()
 scrape_1st_degrees()

if __name__ == '__main__':
    main()