#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : Original author WindVoiceVox
# Original Author Github: https://github.com/WindVoiceVox/Raspi_SG90
# http://elecrow.com/

import RPi.GPIO as GPIO
import time
import sys

# Buzzer 1
# represents the start of the milling process
buzzer_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

# Make buzzer sound
GPIO.output(buzzer_pin, GPIO.HIGH)
time.sleep(1)
# Stop buzzer sound
GPIO.output(buzzer_pin, GPIO.LOW)

GPIO.cleanup()


# LED Matrix
# Represent machine status
# Import all the modules 
import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

time.sleep(1)
def main(cascaded, block_orientation, rotate):
    
    # create matrix device
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=cascaded or 1, block_orientation=block_orientation, rotate=rotate or 0)
    # debugging purpose
    print("[-] Matrix initialized")

    # print Balrog Brewery on the matrix display
    msg = "Balrog Brewery"
    
    time.sleep(3)
    # print Brewing process initializing...
    msg1 = "Brewing process initializing..."
    
    # for debugging purpose
    print("[-] Printing: %s" % msg)
    show_message(device, msg, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)

    # for debugging purpose
    print("[-] Printing: %s" % msg1)
    show_message(device, msg1, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)
    
    
    

if __name__ == "__main__":
    
    # cascaded = Number of cascaded MAX7219 LED matrices, default=1
    # block_orientation = choices 0, 90, -90, Corrects block orientation when wired vertically, default=0
    # rotate = choices 0, 1, 2, 3, Rotate display 0=0°, 1=90°, 2=180°, 3=270°, default=0
   
    try:
        main(cascaded=1, block_orientation=90, rotate=0)
    except KeyboardInterrupt:
        pass
    
# LCD display
# Show employees the current brewing stage


# Vibration
# define vibration pin
time.sleep(5)
vibration_pin = 13

# Set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BOARD)

# Setup vibration pin to OUTPUT
GPIO.setup(vibration_pin, GPIO.OUT)

# turn on vibration
GPIO.output(vibration_pin, GPIO.HIGH)
# wait half a second
time.sleep(3)
# turn off vibration
GPIO.output(vibration_pin, GPIO.LOW)
# cleaup GPIO
GPIO.cleanup()

# LED Display 2
# Show that this process is done


# Buzzer 2
# Represent the START of the milling process
time.sleep(2)
buzzer_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

# Make buzzer sound
GPIO.output(buzzer_pin, GPIO.HIGH)
time.sleep(.5)
# Stop buzzer sound
GPIO.output(buzzer_pin, GPIO.LOW)

GPIO.cleanup()

# LED Matrix 3
# Inform that the weight measuring process is finish
# Ready to mill
def main(cascaded, block_orientation, rotate):
    
    # create matrix device
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=cascaded or 1, block_orientation=block_orientation, rotate=rotate or 0)
    # debugging purpose
    print("[-] Matrix initialized")

    # print Balrog Brewery on the matrix display
    msg3 = "Start milling..."
    
    # for debugging purpose
    print("[-] Printing: %s" % msg3)
    show_message(device, msg3, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)
    

if __name__ == "__main__":
    
    # cascaded = Number of cascaded MAX7219 LED matrices, default=1
    # block_orientation = choices 0, 90, -90, Corrects block orientation when wired vertically, default=0
    # rotate = choices 0, 1, 2, 3, Rotate display 0=0°, 1=90°, 2=180°, 3=270°, default=0
   
    try:
        main(cascaded=1, block_orientation=90, rotate=0)
    except KeyboardInterrupt:
        pass

# Step motor
import math

class Stepmotor:

    def __init__(self):

        # set GPIO mode
        GPIO.setmode(GPIO.BCM)
        # These are the pins which will be used on the Raspberry Pi
        self.pin_A = 5
        self.pin_B = 6
        self.pin_C = 13
        self.pin_D = 19
        self.interval = 0.010

        # Declare pins as output
        GPIO.setup(self.pin_A,GPIO.OUT)
        GPIO.setup(self.pin_B,GPIO.OUT)
        GPIO.setup(self.pin_C,GPIO.OUT)
        GPIO.setup(self.pin_D,GPIO.OUT)
        GPIO.output(self.pin_A, False)
        GPIO.output(self.pin_B, False)
        GPIO.output(self.pin_C, False)
        GPIO.output(self.pin_D, False)

    def Step1(self):

        GPIO.output(self.pin_D, True)
        time.sleep(self.interval)
        GPIO.output(self.pin_D, False)

    def Step2(self):

        GPIO.output(self.pin_D, True)
        GPIO.output(self.pin_C, True)
        time.sleep(self.interval)
        GPIO.output(self.pin_D, False)
        GPIO.output(self.pin_C, False)

    def Step3(self):

        GPIO.output(self.pin_C, True)
        time.sleep(self.interval)
        GPIO.output(self.pin_C, False)

    def Step4(self):

        GPIO.output(self.pin_B, True)
        GPIO.output(self.pin_C, True)
        time.sleep(self.interval)
        GPIO.output(self.pin_B, False)
        GPIO.output(self.pin_C, False)

    def Step5(self):

        GPIO.output(self.pin_B, True)
        time.sleep(self.interval)
        GPIO.output(self.pin_B, False)

    def Step6(self):

        GPIO.output(self.pin_A, True)
        GPIO.output(self.pin_B, True)
        time.sleep(self.interval)
        GPIO.output(self.pin_A, False)
        GPIO.output(self.pin_B, False)

    def Step7(self):

        GPIO.output(self.pin_A, True)
        time.sleep(self.interval)
        GPIO.output(self.pin_A, False)

    def Step8(self):

        GPIO.output(self.pin_D, True)
        GPIO.output(self.pin_A, True)
        time.sleep(self.interval)
        GPIO.output(self.pin_D, False)
        GPIO.output(self.pin_A, False)

    def turn(self,count):
        for i in range (int(count)):
            self.Step1()
            self.Step2()
            self.Step3()
            self.Step4()
            self.Step5()
            self.Step6()
            self.Step7()
            self.Step8()

    def close(self):
        # cleanup the GPIO pin use
        GPIO.cleanup()

    def turnSteps(self, count):
        # Turn n steps
        # (supply with number of steps to turn)
        for i in range (count):
            self.turn(1)

    def turnDegrees(self, count):
        # Turn n degrees (small values can lead to inaccuracy)
        # (supply with degrees to turn)
        self.turn(round(count*512/360,0))

    def turnDistance(self, dist, rad):
        # Turn for translation of wheels or coil (inaccuracies involved e.g. due to thickness of rope)
        # (supply with distance to move and radius in same metric)
        self.turn(round(512*dist/(2*math.pi*rad),0))

def main():

    print("moving started")
    motor = Stepmotor()
    print("One Step")
    motor.turnSteps(1)
    time.sleep(0.5)
    print("20 Steps")
    motor.turnSteps(20)
    time.sleep(0.5)
    print("quarter turn")
    motor.turnDegrees(360)
    print("moving stopped")
    motor.close()

if __name__ == "__main__":
    main()
    
# Buzzer 3
# Represent the end of the milling process
time.sleep(2)
buzzer_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

# Make buzzer sound
GPIO.output(buzzer_pin, GPIO.HIGH)
time.sleep(.5)
# Stop buzzer sound
GPIO.output(buzzer_pin, GPIO.LOW)

GPIO.cleanup()

# LED Matrix 4
# Inform that the milling process is done
# Move to the mash tun
time.sleep(1)
def main(cascaded, block_orientation, rotate):
    
    # create matrix device
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=cascaded or 1, block_orientation=block_orientation, rotate=rotate or 0)
    # debugging purpose
    print("[-] Matrix initialized")

    # print Balrog Brewery on the matrix display
    msg4 = "Finished."
    
    time.sleep(3)
    # print Brewing process initializing...
    msg5 = "Moving to mash tun..."
    
    # for debugging purpose
    print("[-] Printing: %s" % msg4)
    show_message(device, msg4, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)

    # for debugging purpose
    print("[-] Printing: %s" % msg5)
    show_message(device, msg5, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)
        

if __name__ == "__main__":
    
    # cascaded = Number of cascaded MAX7219 LED matrices, default=1
    # block_orientation = choices 0, 90, -90, Corrects block orientation when wired vertically, default=0
    # rotate = choices 0, 1, 2, 3, Rotate display 0=0°, 1=90°, 2=180°, 3=270°, default=0
   
    try:
        main(cascaded=1, block_orientation=90, rotate=0)
    except KeyboardInterrupt:
        pass


# Servo
class sg90:

  def __init__( self, direction):

    self.pin = 25
    GPIO.setmode( GPIO.BCM )
    GPIO.setup( self.pin, GPIO.OUT )
    self.direction = int( direction )
    self.servo = GPIO.PWM( self.pin, 50 )
    self.servo.start(0.0)

  def cleanup( self ):

    self.servo.ChangeDutyCycle(self._henkan(0))
    time.sleep(0.3)
    self.servo.stop()
    GPIO.cleanup()

  def currentdirection( self ):

    return self.direction

  def _henkan( self, value ):

    return 0.05 * value + 7.0

  def setdirection( self, direction, speed ):

    for d in range( self.direction, direction, int(speed) ):
      self.servo.ChangeDutyCycle( self._henkan( d ) )
      self.direction = d
      time.sleep(0.1)
    self.servo.ChangeDutyCycle( self._henkan( direction ) )
    self.direction = direction

def main():

    s = sg90(0)

    try:
        while True:
            print("Turn left ...")
            s.setdirection( 100, 100 )
            time.sleep(0.5)
            print("Turn right ...")
            s.setdirection( -100, -100 )
            time.sleep(0.5)
    except KeyboardInterrupt:
        s.cleanup()

if __name__ == "__main__":
    main()



