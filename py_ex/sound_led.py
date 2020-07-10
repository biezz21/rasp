import RPi.GPIO as GPIO
import time
import pymysql

GPIO.setmode(GPIO.BOARD)

conn = pymysql.connect(host="localhost", user="root", passwd="1234", db="raspi_db")

soundpin = 11
led = 13
GPIO.setup(soundpin,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

try:
    with conn.cursor () as cur :
	sql = "insert into sound_data values(%s, %s, %s)"
        while(True):
            soundlevel = GPIO.input(soundpin)
            if  soundlevel == True:
	        print "Sound Deteced"
       	        GPIO.output(led,GPIO.HIGH)
       	        cur.execute(sql, ('Sound', time.strftime("%Y-%m-%d %H:%m:%S", time.localtime()), 1))
	        conn.commit()
	        time.sleep(0.3)

	    else:
	        GPIO.output(led,GPIO.LOW)
            time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()
