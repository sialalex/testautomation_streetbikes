import can
import time

# create a bus instance
# many other interfaces are supported as well (see documentation)
bus = can.Bus(interface='socketcan',
              channel='can0',
              receive_own_messages=True)

# send a message
msg = can.Message(arbitration_id=0x140, is_extended_id=False,
                      data=[0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88])
#bus.send(message, timeout=0.2)

task = bus.send_periodic(msg, 0.20)
#assert isinstance(task, can.CyclicSendTaskABC)
#time.sleep(10)
#task.stop()
#print("stopped cyclic send")
