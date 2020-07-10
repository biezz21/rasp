import RPi.GPIO as GPIO
import time
import pymysql

GPIO.setmode(GPIO.BOARD)

conn = pymysql.connect(host="localhost", user="root", passwd="1234", db="raspi_db")

led = 13
touch = 11

GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(touch, GPIO.IN)

try:
    with conn.cursor () as cur :
	sql = "insert into touch_data values(%s, %s, %s)"
        while 1:
            inputIO = GPIO.input(touch)
            if inputIO == True:
                GPIO.output(led, GPIO.HIGH)
		print "Touch Detected"
                cur.execute(sql, ('Touch', time.strftime("%Y-%m-%d %H:%m:%S", time.localtime()), 1))
                conn.commit()
            else:
                GPIO.output(led, GPIO.LOW)
            time.sleep(0.05)

except KeyboardInterrupt:
    GPIO.cleanup()
