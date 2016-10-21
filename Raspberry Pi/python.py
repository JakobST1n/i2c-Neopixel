""" Imports """
import logging
import smbus
import sys
import time
import json
import i2cPixel

""" Decalrations """
pixels = 348 # Change this to the appropriate number for your setup
addresses = [0, 24, 25, 35] # legg til en start og en stopp for hvert trinn

def hexToRgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

def lightStaircase(direction):
    repeats = len(addresses)
    repeats = repeats / 2
    
    if direction == "up":
        loopCondition = repeats
        
            
    else:
        loopCondition = 0
    
    return true
    
def errorHandler(type, errorMsg):
    if type == 1: # Debug
        logging.debug(errorMsg)
        print("Debug Message: See logfile")
    elif type == 2: # info
        logging.info(errorMsg)
    elif type == 3: # Warning 
        logging.warning(errorMsg)
    elif type == 4: # Error
        logging.error(errorMsg)
        print("Error: See logfile")
    elif type == 5: # Error
        logging.critical(errorMsg)
        print("Critical Error: See logfile")
    else:
        logging.critical(errorMsg)
        print("Something went terribly wrong! Not even the errorhandler was able to find out what. Which basically means 'You are doomed'") 
    
def setup():
    
    """ Setup Log File """
    logging.basicConfig(filename='error.log',level=logging.DEBUG,mode='w')
    
    """ Print first line of log file """
    logging.info('Starting App')

    """ Set time """
    start_time = time.time()

    """ Setup i2c communication """
    i2cPixel.version()
    i2cPixel.setBus(1)
    i2cPixel.setAddress(0x04)

    """ Wait for heartbeat from Arduino """
    while True:
        try:
            if i2cPixel.greeting():
                print "Arduino is Online"
                time.sleep(1)
            break
        except Exception:
            pass
    
    """i = 0
    while i < pixels:
        i2cPixel.setPixel(i, 0, 0, 0)
    i2cPixel.show()"""

    
def main():

    print "GO!"
    timer = time.time()
    i = 0
    while i < pixels:
        i2cPixel.setPixel(i, 255, 255, 255)
        i2cPixel.show()
        i = i + 1
    print("--- %s seconds ---" % (time.time() - timer))

    timer = time.time()
    i = 0
    while i < pixels:
        i2cPixel.setPixel(i, 255, 255, 255)
        i = i + 1
    i2cPixel.show()
    print("--- %s seconds ---" % (time.time() - timer))
    
    pixelsPerStair = [21, 23, 23, 24, 25, 27, 31, 33, 28, 26, 25, 24, 24]

    i = 0
    o = 0
    j = 0
    timer = time.time()
    while i < len(pixelsPerStair):
        time1 = time.time()
        mellomRekning = o + pixelsPerStair[i]

        if j == 0:
            color = (255, 0, 225)
            j = j + 1
        elif j == 1:
            color = (0, 63, 255)
            j = j + 1
        elif j == 2:
            color = (25, 255, 0)
            j = j + 1
        elif j == 3:
            color = (255, 0, 4)
            j = j + 1
        else:
            color = (255, 250, 0)
            j = 0
                
        while o <= mellomRekning:
            i2cPixel.setPixel(o, *color)
            o = o + 1   
        i2cPixel.show()
        i = i + 1
    print("--- %s seconds ---" % (time.time() - timer))
    
    
   
    
    
    
""" Start script """
setup() #configure
main() #Start main
