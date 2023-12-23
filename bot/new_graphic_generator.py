from subprocess import Popen
import random
from icecream import ic 
import time
#from sel import *

used_displays = {} #tele_user: display
pids = {} #tele_user: pid





def get_display():
    display = random.randint(1,99)
    if display in used_displays.values():
        return get_display()
    else:
        return display


def record_wheel(tele_user, options):
    for option in options:
        options[options.index(option)] = str(option).replace(" ", "_")
    options = str(options).replace(" ", "")

    tele_user = str(tele_user)
    display = get_display()
    used_displays[tele_user] = display
    cmd = '/usr/bin/xvfb-run --server-num {display} -e /dev/stdout --auth-file /tmp/xvfb.auth -s XVFB_ARGS /usr/local/bin/python3.12 sel.py {tele_user} {options} &'.format(display=str(display), tele_user=str(tele_user), options=str(options)).split()

    for i in cmd:
        if i == "XVFB_ARGS":
            cmd[cmd.index(i)] = "-ac -screen 0 338x338x24"
        #ic(i)
    
    #/usr/bin/xvfb-run --server-num 37 -e /dev/stdout --auth-file /tmp/xvfb.auth -s "-ac -screen 0 338x338x24" /usr/local/bin/python3.12 sel.py 469930185 ['option_7','option_4','option_213'] &
    process = Popen(cmd)

    pid1 = process.pid
    time.sleep(4)
    cmd = "/usr/bin/ffmpeg -y -f x11grab -video_size 338x338 -draw_mouse 0 -i :{display}  -r 12 /data/output_{tele_user}.gif".format(display=display,tele_user=str(tele_user)).split()
    process = Popen(cmd)

    pid2 = process.pid
    pids[tele_user] = [pid1,pid2]
    ic(pids)

    

def stop_recording(tele_user):
    tele_user = str(tele_user)
    ic(pids)

    for pid in pids[tele_user]:
        cmd = 'kill {pid}'.format(pid = pid)
        Popen(cmd.split())
    used_displays.pop(tele_user)
    


#xvfb-run --server-num 44 --auth-file /tmp/xvfb.auth -s "-ac -screen 0 338x338x24" python3.12 bot/sel.py &
#export DISPLAY=:44
#ffmpeg -y -f x11grab -video_size 338x338 -draw_mouse 0 -i :44 -codec:v libx264 -r 12 video.mp4