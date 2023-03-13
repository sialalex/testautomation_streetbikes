import subprocess
import time
import os

absolute_path = os.path.dirname(__file__)
os.system("echo Starting the Restbus Simulation!")

subprocess.Popen(["python3", absolute_path+"/restbus/restbus_canplayer.py"], close_fds=True)
time.sleep(0.5)
