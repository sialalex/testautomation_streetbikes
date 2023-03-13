from TestBike import TestBike
import time


duke1290 = TestBike("1290 Duke", "123456", "orange")
#duke1290.start_navigation()
#print(duke1290.hbs_commands_task)
#duke1290.enable_hbs_commands()#duke1290.open_main_screen()

duke1290.start_restbus_simulation()

time.sleep(20)
duke1290.stop_restbus_simulation()