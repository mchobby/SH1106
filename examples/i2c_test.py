# MicroPython SH1106 OLED driver test for I2C

from machine import Pin, I2C
import sh1106

# Pin Map I2C for ESP8266
#   - 3v - xxxxxx   - Vcc
#   - G  - xxxxxx   - Gnd
#   - D2 - GPIO 5   - SCK / SCL
#   - D1 - GPIO 4   - DIN / SDA
#   - D0 - GPIO 16  - Res (required, unless a Hardware reset circuit is connected)
#   - G  - xxxxxx     CS
#   - G  - xxxxxx     D/C
#
# Pin's for I2C can be set almost arbitrary
#
# i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)

# Pin Map I2C for Raspberry-Pi Pico
#  GPIO 6 - I2C(1) Sda
#  GPIO 7 - I2C(1) Scl
i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000 )

display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
display.sleep(False)
display.fill(1) # 1=White
display.text('Bonnjour', 10, 10, 0) # 0=black 
display.show()
