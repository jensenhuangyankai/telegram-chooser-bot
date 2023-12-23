from subprocess import Popen, call
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

from pyvirtualdisplay import Display
os.environ['PYVIRTUALDISPLAY_DISPLAYFD'] = '0'
os.environ['DISPLAY'] = ':0'

options = Options()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--verbose')
options.add_experimental_option("detach", True)

 

#print(driver.title)
#driver.close()


def terminate(process):
    call(['killall', 'ffmpeg'])

class Recorder:
    def __init__(self):
        self.process = ""

    def record(self):
        with Display(backend="xvfb", size=(1000,1000) ) as disp:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            print(disp.is_alive())
            driver.get("http://127.0.0.1:5000/")
            #cmd = "xwd -display :0.0 -out pic"
            #cmd = cmd.split()
            #call(cmd)
            print(disp._obj)
            cmd = 'ffmpeg -y -f x11grab -i :0 -r 10 -s 1000x1000 test.mp4'
            cmd = cmd.split()
            #cmd = 'ffmpeg -y -rtbufsize 2000M -f x11grab -framerate 30 -s 500x500 -b:v 512k -r 20 -vcodec libx264 test.avi'
            self.process = Popen(cmd) # start recording

    def stop(self):
        terminate(self.process)   # terminates recording
        driver.quit()


recorder = Recorder()
recorder.record()
time.sleep(20)
recorder.stop()












