import RPi.GPIO as GPIO
import time

# Pin configuration
PIN = 26

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(PIN, GPIO.OUT)  # Set GPIO 26 as an output

try:
    while True:
        # Turn on the GPIO pin
        GPIO.output(PIN, GPIO.HIGH)
        print("GPIO 26 ON")
        time.sleep(1)  # Keep it on for 1 second

        # Turn off the GPIO pin
        GPIO.output(PIN, GPIO.LOW)
        print("GPIO 26 OFF")
        time.sleep(1)  # Keep it off for 1 second

except KeyboardInterrupt:
    print("Script interrupted by user.")

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
    print("GPIO cleanup completed.")
