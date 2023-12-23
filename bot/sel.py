from subprocess import Popen, call
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import sys

options = Options()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument('--app=http://127.0.0.1:5000/')
options.add_experimental_option("detach", True)

tele_user = sys.argv[1]
options = list(sys.argv[2])

options = str(options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("http://127.0.0.1:5000/?tele_user={tele_user}&options={options}".format(tele_user=str(tele_user), options = options))

while True:
    pass

#generate(123213)