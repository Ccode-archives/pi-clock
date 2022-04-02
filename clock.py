from machine import Pin, I2C
from time import sleep, gmtime
from pico_i2c_lcd import I2cLcd

i2c = I2C(0,
            sda=machine.Pin(0),
            scl=machine.Pin(1),
            freq=400000)

I2C_ADDR = i2c.scan()[0]

#components
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
#offbutton = Pin(13, Pin.IN, Pin.PULL_DOWN)

lcd.backlight_on()
sleep(1)
lcd.putstr("Booting...")
sleep(.5)
lcd.clear()
lcd.putstr("12" + ":" + "0")
try:
    while True:
        lcd.clear()
        lcd.putstr(str(gmtime()[3]) + ":" + str(gmtime()[4]))
        sleep(1)
        #if offbutton.value() == 1:
            #raise OSError("turn off pressed")
except:
    lcd.clear()
    sleep(.1)
    lcd.putstr("Booting off...")
    sleep(.5)
    lcd.backlight_off()
    sleep(.1)
    lcd.clear()
