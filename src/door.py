import RPi.GPIO as GPIO
import time
import datetime
import mail 

last_sent = 0
send_interval = 1 * 60
doorToggle = False
PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        state = GPIO.input(PIN)
        if state == GPIO.LOW:
            if doorToggle == False:
                mail.sendMessage('[CLOSED]')
                #print('[DEBUG MESSAGE]:\n\nDOOR CLOSED\n\nsimulating email sending...\n[TIME]: ' + str(datetime.datetime.now()))
                doorToggle = True
            last_sent = 0
        else:
            current_time = time.time()
            if current_time - last_sent >= send_interval:
                doorToggle = False 
                mail.sendMessage('[OPEN]')
                last_sent = current_time
                #print('[DEBUG MESSAGE]:\n\nDOOR OPEN\n\nsimulating email sending...\n[TIME]: ' + str(datetime.datetime.now()))
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
