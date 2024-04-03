import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode (GPIO.BOARD)

#Assign GPIO pins for both motors

lm_ena = 33 
lm_pos = 35
lm_neg = 37

rm_ena = 36
rm_pos = 38
rm_neg = 40

# Set pins in the output mode 
GPIO.setup(lm_ena,GPIO.OUT)
GPIO.setup(lm_pos,GPIO.OUT)
GPIO.setup(lm_neg,GPIO.OUT)

GPIO.setup(rm_ena,GPIO.OUT)
GPIO.setup(rm_pos,GPIO.OUT)
GPIO.setup(rm_neg,GPIO.OUT)

def moveRobot(direction):
    if(direction == "f"): 
        print ("Forward")
        #Left Motor Forward
        GPIO.output (lm_ena,GPIO.HIGH)
        GPIO.output (lm_pos,GPIO.HIGH)
        GPIO.output (lm_neg,GPIO.LOW)  
        #Right Motor Forward.
        GPIO.output (rm_ena,GPIO.HIGH) 
        GPIO.output (rm_pos,GPIO.HIGH)
        GPIO.output (rm_neg,GPIO.LOW)
        
        if (direction == "b"):
            print ("Backward")
            #Left Motor Backward
            GPIO.output(lm ena, GPIO.HIGH)
            GPIO.output(lm_pos, GPIO.LOW)
            GPIO.output(lm_neg, GPIO.HIGH)
            #Right Motor Backward
            GPIO.output(rm_ena,GPIO.HIGH)
            GPIO.output(rm_pos,GPIO.LOW)
            GPIO.output(rm_neg,GPIO.HIGH)
            
        if(direction == "r"):
            print ("Right")
            #Left Motor Forward
            GPIO.output(lm_ena,GPIO.HIGH)
            GPIO.output(lm_pos,GPIO.HIGH)
            GPIO.output (lm_neg,GPIO.LOW)
            #Right Motor Backward
            GPIO.output(rm_ena,GPIO.HIGH) 
            GPIO.output(rm_pos,GPIO.LOW)
            GPIO.output(rm_neg,GPIO.HIGH)
        
        if (direction == "l"):
            print ("Left")
            #Left Motor Backward
            GPIO.output(lm_ena,GPIO.HIGH)
            GPIO.output(lm_pos,GPIO.LOW)
            GPIO.output(lm_neg,GPIO.HIGH)
            #Right Motor Forward 
            GPIO.output(rm_ena,GPIO.HIGH) 
            GPIO.output(rm_pos,GPIO.HIGH)
            GPIO.output(rm_neg,GPIO.LOW)

        if (direction == "s"):
            print ("Stop")
            #Left Motor Stop
            GPIO.output(lm_ena,GPIO.HIGH)
            GPIO.output(lm_pos,GPIO.LOW)
            GPIO.output(lm_neg,GPIO.LOW)
            #Right Motor Stop 
            GPIO.output(rm_ena,GPIO.HIGH) 
            GPIO.output(rm_pos,GPIO.LOW)
            GPIO.output(rm_neg,GPIO.LOW)

for i in range(0,5): 
    moveRobot("f")
    sleep(1)
    moveRobot("b")
    sleep(1)
    moveRobot("r")
    sleep(1)
    moveRobot("l")
    sleep(1)
    moveRobot("s")
    sleep(1)

GPIO.cleanup()

        