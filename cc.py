import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BCM)
YELLOW_PIN = 2
WHITE_PIN = 21
RED_PIN = 23
GREEN_PIN = 26

GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(WHITE_PIN, GPIO.OUT)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

def turn_off_all():
    GPIO.output(YELLOW_PIN, GPIO.LOW)
    GPIO.output(WHITE_PIN, GPIO.LOW)
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)

def turn_on_color(color):
    turn_off_all()
    if color == 'yellow':
        GPIO.output(YELLOW_PIN, GPIO.HIGH)
    elif color == 'white':
        GPIO.output(WHITE_PIN, GPIO.HIGH)
    elif color == 'red':
        GPIO.output(RED_PIN, GPIO.HIGH)
    elif color == 'green':
        GPIO.output(GREEN_PIN, GPIO.HIGH)

def wave_effect(duration=10):
    """Lights turn on one by one then off one by one"""
    print("🌊 Wave effect starting...")
    pins = [YELLOW_PIN, WHITE_PIN, RED_PIN, GREEN_PIN]
    end_time = time.time() + duration
    
    while time.time() < end_time:
        # Turn on one by one
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.2)
        # Turn off one by one
        for pin in pins:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.2)

def alternating_blink(duration=10):
    """Two colors alternate"""
    print("🔄 Alternating blink starting...")
    end_time = time.time() + duration
    
    while time.time() < end_time:
        GPIO.output(YELLOW_PIN, GPIO.HIGH)
        GPIO.output(RED_PIN, GPIO.HIGH)
        GPIO.output(WHITE_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        time.sleep(0.5)
        
        GPIO.output(YELLOW_PIN, GPIO.LOW)
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(WHITE_PIN, GPIO.HIGH)
        GPIO.output(GREEN_PIN, GPIO.HIGH)
        time.sleep(0.5)
    turn_off_all()

def disco_mode(duration=10):
    """Random combinations of lights"""
    print("🕺 DISCO MODE starting...")
    pins = [YELLOW_PIN, WHITE_PIN, RED_PIN, GREEN_PIN]
    end_time = time.time() + duration
    
    while time.time() < end_time:
        turn_off_all()
        # Randomly turn on 1-3 lights
        num_lights = random.randint(1, 3)
        selected_pins = random.sample(pins, num_lights)
        for pin in selected_pins:
            GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.2)
    turn_off_all()

def breathing_effect(duration=10):
    """All lights fade in and out (on/off simulation)"""
    print("💨 Breathing effect starting...")
    end_time = time.time() + duration
    
    while time.time() < end_time:
        turn_on_all()
        time.sleep(1)
        turn_off_all()
        time.sleep(1)

# Menu
print("Light Controller")
print("1 - Yellow")
print("2 - White")
print("3 - Red")
print("4 - Green")
print("5 - All Off")
print("6 - Exit")

try:
    while True:
        choice = input("\nEnter choice: ")
        
        if choice == '1':
            turn_on_color('yellow')
            print("Yellow ON")
        elif choice == '2':
            turn_on_color('white')
            print("White ON")
        elif choice == '3':
            turn_on_color('red')
            print("Red ON")
        elif choice == '4':
            turn_on_color('green')
            print("Green ON")
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
    print("\nGoodby
