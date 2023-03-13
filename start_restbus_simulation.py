import subprocess
import time
import os

os.system("echo Starting the Restbus Simulation!")

subprocess.Popen(["python3", "can_play_restbus.py"], close_fds=True)
time.sleep(0.5)
