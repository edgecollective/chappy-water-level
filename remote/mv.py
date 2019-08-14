import board
import busio
import digitalio
import time
import adafruit_rfm9x
from analogio import AnalogIn
import gc

vbat_voltage = AnalogIn(board.VOLTAGE_MONITOR)
 
 
def get_voltage(pin):
    return (pin.value * 3.3) / 65536 * 2

# lora radio
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D9) # based on my particular wiring of featherwing: "CS" -- "C" -- pin 9
reset = digitalio.DigitalInOut(board.D6) # based on my particular wiring of feathering: "RESET" -- "D" -- pin 6
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)


led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

uart = busio.UART(board.TX, board.RX, baudrate=1200)

#batt=AnalogIn(board.A6)


def blink(delay,num_times):
    for i in range(num_times):
        led.value=True
        time.sleep(delay)
        led.value=False
        time.sleep(delay)

while True:
    time.sleep(.1)
    #print(uart.readline())
    line=uart.readline()
    print(line)
    if line is not None:
        try:
            battery_voltage = get_voltage(vbat_voltage)
            print("VBat voltage: {:.2f}".format(battery_voltage))
            #print("A6:",A6.value)
            pt = str(line, 'ascii')
            pt = pt.strip('\n')
            pt = pt.strip('\r')
            ls = pt.strip().split(',')
            if len(ls)==3:
                pt = pt + ","+str(battery_voltage)
                print(pt.strip().split(','))
                print("sending ...",pt)
                rfm9x.send(pt)
                blink(.1,1)
        except Exception as e:
            print("error: "+str(e))
    gc.collect()
