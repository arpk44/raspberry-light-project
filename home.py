import streamlit as st
import RPi.GPIO as GPIO
import time

# GPIO Setup - do this once when the app loads
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for each color (adjust these to your actual pin connections)
BLUE_PIN = 17
GREEN_PIN = 27
YELLOW_PIN = 22
RED_PIN = 23

# Setup all pins as outputs
GPIO.setup(BLUE_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(RED_PIN, GPIO.OUT)

# Turn all off initially
GPIO.output(BLUE_PIN, GPIO.LOW)
GPIO.output(GREEN_PIN, GPIO.LOW)
GPIO.output(YELLOW_PIN, GPIO.LOW)
GPIO.output(RED_PIN, GPIO.LOW)

# Functions to control each light
def turn_on_light(pin, color_name):
    """Turn on a specific light"""
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)  # Small delay for stability

def turn_off_light(pin):
    """Turn off a specific light"""
    GPIO.output(pin, GPIO.LOW)

def turn_off_all():
    """Turn off all lights"""
    GPIO.output(BLUE_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(YELLOW_PIN, GPIO.LOW)
    GPIO.output(RED_PIN, GPIO.LOW)

# Page config
st.set_page_config(page_title="Light Controller", layout="centered")

# Title
st.title("💡 Light Controller")
st.write("Click a button to control the lights")

# Create 2 columns for buttons
col1, col2 = st.columns(2)

with col1:
    # Blue button
    if st.button("Blue", use_container_width=True, type="primary"):
        turn_off_all()  # Turn off other lights first
        turn_on_light(BLUE_PIN, "Blue")
        st.success("Blue light is ON!")
        
    # Green button
    if st.button("Green", use_container_width=True, type="secondary"):
        turn_off_all()
        turn_on_light(GREEN_PIN, "Green")
        st.success("Green light is ON!")

with col2:
    # Yellow button
    if st.button("Yellow", use_container_width=True, type="primary"):
        turn_off_all()
        turn_on_light(YELLOW_PIN, "Yellow")
        st.success("Yellow light is ON!")
        
    # Red button
    if st.button("Red", use_container_width=True, type="secondary"):
        turn_off_all()
        turn_on_light(RED_PIN, "Red")
        st.success("Red light is ON!")

# Turn all off button
st.divider()
if st.button("🔴 Turn All OFF", use_container_width=True):
    turn_off_all()
    st.info("All lights turned OFF")

# Status display
st.divider()
st.write("**Status:** Ready")

# Instructions
with st.expander("ℹ️ Instructions"):
    st.write("""
    - Click any color button to turn that light ON
    - Other lights will automatically turn OFF
    - Use "Turn All OFF" to switch everything off
    - Make sure your Raspberry Pi GPIO pins match the pin numbers in the code:
        - Blue: GPIO 17
        - Green: GPIO 27
        - Yellow: GPIO 22
        - Red: GPIO 23
    """)

# Cleanup when app closes (optional, but good practice)
# Note: Streamlit keeps running, so GPIO.cleanup() should only be called on shutdown
