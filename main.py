import RPi.GPIO as GPIO
import time

# Pin configuration
PIN = 3

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(PIN, GPIO.OUT)  # Set GPIO 17 as an output

try:
    while True:
        # Turn on the GPIO pin
        time.sleep(10)  # Keep it off for 1 second
        
        GPIO.output(PIN, GPIO.HIGH)
        print("GPIO 17 ON")
        time.sleep(5)  # Keep it on for 1 second

        # Turn off the GPIO pin
    #    GPIO.output(PIN, GPIO.LOW)
        print("GPIO 17 OFF")
        time.sleep(20)  # Keep it off for 1 second

except KeyboardInterrupt:
    print("Script interrupted by user.")

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
    print("GPIO cleanup completed.")
