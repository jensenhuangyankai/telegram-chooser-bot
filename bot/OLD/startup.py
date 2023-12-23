import glob
import os

def startup():
    files = glob.glob("./png/*")
    files2 = glob.glob("./eps/*")
    files3 = glob.glob("./*.gif")
    for f in files:
        os.remove(f)
    for f in files2:
        os.remove(f)
    for f in files3:
        os.remove(f)