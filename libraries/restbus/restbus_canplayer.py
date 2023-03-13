import os

absolute_path = os.path.dirname(__file__)
os.system("canplayer -I "+absolute_path+"/restbus.log -l i")

