from subprocess import Popen
import random

from sel import *

used_displays = {} #tele_user: display
pids = {} #tele_user: pid


def get_display():
    display = random.randint(1,99)
    if display in used_displays.values():
        return get_display()
    else:
        return display


def record_wheel(tele_user, options):
    options = str(options)
    tele_user = str(tele_user)
    display = get_display()
    cmd = '/usr/bin/xvfb-run --server-num {display} --auth-file /tmp/xvfb.auth -s "-ac -screen 0 338x338x24" /usr/bin/python3.12 "sel.py {tele_user} {options}" &'.format(display=display, tele_user=tele_user, options=str(options)).split()
    process = Popen(cmd)
    pid = process.pid
    pids[tele_user] = pid

    cmd = "/usr/bin/ffmpeg -y -f x11grab -video_size 338x338 -draw_mouse 0 -i :{display} -codec:v libx264 -r 12 /data/video.mp4".format(display=display).split()
    process = Popen(cmd)
    pid = process.pid
    pids[tele_user] = pids[tele_user].append(pid)
    

def stop_recording(tele_user):
    tele_user = str(tele_user)
    for pid in pids[tele_user]:
        Popen("kill {pid}".format(pid).split())
    used_displays.pop(tele_user)
    


#xvfb-run --server-num 44 --auth-file /tmp/xvfb.auth -s "-ac -screen 0 338x338x24" python3.12 bot/sel.py &
#export DISPLAY=:44
#ffmpeg -y -f x11grab -video_size 338x338 -draw_mouse 0 -i :44 -codec:v libx264 -r 12 video.mp4