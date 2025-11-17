import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BCM)
BLUE_PIN = 17
GREEN_PIN = 27
YELLOW_PIN = 22
RED_PIN = 23

GPIO.setup(BLUE_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(RED_PIN, GPIO.OUT)

def turn_off_all():
    GPIO.output(BLUE_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(YELLOW_PIN, GPIO.LOW)
    GPIO.output(RED_PIN, GPIO.LOW)

def turn_on_color(color):
    turn_off_all()
    if color == 'blue':
        GPIO.output(BLUE_PIN, GPIO.HIGH)
    elif color == 'green':
        GPIO.output(GREEN_PIN, GPIO.HIGH)
    elif color == 'yellow':
        GPIO.output(YELLOW_PIN, GPIO.HIGH)
    elif color == 'red':
        GPIO.output(RED_PIN, GPIO.HIGH)

# Menu
print("Light Controller")
print("1 - Blue")
print("2 - Green")
print("3 - Yellow")
print("4 - Red")
print("5 - All Off")
print("6 - Exit")

try:
    while True:
        choice = input("\nEnter choice: ")
        
        if choice == '1':
            turn_on_color('blue')
            print("Blue ON")
        elif choice == '2':
            turn_on_color('green')
            print("Green ON")
        elif choice == '3':
            turn_on_color('yellow')
            print("Yellow ON")
        elif choice == '4':
            turn_on_color('red')
            print("Red ON")
        elif choice == '5':
            turn_off_all()
            print("All OFF")
        elif choice == '6':
            break
        else:
            print("Invalid choice")
            
except KeyboardInterrupt:
    pass

finally:
    turn_off_all()
    GPIO.cleanup()
    print("\nGoodbye!")
