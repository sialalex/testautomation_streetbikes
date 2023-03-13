# GPIO-Bibliothek laden
import RPi.GPIO as GPIO

# BCM-Nummerierung verwenden
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

# GPIO 20 als Ausgang setzen
GPIO.setup(20, GPIO.OUT)

# GPIO 20 auf HIGH setzen
GPIO.output(20, True)

# GPIO 21 als Ausgang setzen
GPIO.setup(21, GPIO.OUT)

# GPIO 21 auf HIGH setzen
GPIO.output(21, True)

print("Ignition/Power ON")
