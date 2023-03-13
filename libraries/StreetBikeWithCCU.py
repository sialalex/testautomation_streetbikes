import can
import subprocess
import time
import os

class StreetBikeWithCCU():

    def __init__(self, name, vin, color):
        self.name = name
        self.vin = vin
        self.color = color

        self.hbs_commands_task = None
        
    def start_navigation(self):
        raise NotImplementedError("Subclasses have to implement this method!")
    
    def open_main_screen(self):
        raise NotImplementedError("Subclasses have to implement this method!")

    def open_navigation_menu(self):
        raise NotImplementedError("Subclasses have to implement this method!")

    def open_ktmconnect_menu(self):
        raise NotImplementedError("Subclasses have to implement this method!")  

    def enable_hbs_commands(self):
        print("Enabled HBS Commands")
        # create a bus instance
        # many other interfaces are supported as well (see documentation)
        
        bus = can.Bus(interface='socketcan',
              channel='can0',
              receive_own_messages=True)

        # send a message
        msg = can.Message(arbitration_id=0x140, is_extended_id=False,
                      data=[0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88])
        print(msg)
        #bus.send(msg, timeout=0.2)

        self.hbs_commands_task = bus.send_periodic(msg, 0.20)

    def disable_hbs_commands(self):
        print("Disabled HBS Commands")
        self.hbs_commands_task.stop()
        

    def start_restbus_simulation(self):
        absolute_path = os.path.dirname(__file__)
        print("Starting the Restbus Simulation!")

        subprocess.Popen(["python3", absolute_path+"/restbus/restbus_canplayer.py"], close_fds=True)
        time.sleep(0.5)


    def stop_restbus_simulation(self):
        print("Stopping the Restbus Simulation!")
        os.system("sudo pkill canplayer")

