from subprocess import Popen, call
from selenium import webdriver
#from selenium.webdriver.chrome.service import Options
#from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import sys
from icecream import ic

ic(len(sys.argv))
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-setuid-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disables-features=dbus')
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument('--app=http://127.0.0.1:5000/test')
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)


tele_user = sys.argv[1]
choices = sys.argv[2]

link = "http://generator:5000/generate?tele_user={tele_user}&options={options}".format(tele_user=str(tele_user), options = str(choices))
ic(link)
driver.get(str(link))
while True:
    pass

#generate(123213)