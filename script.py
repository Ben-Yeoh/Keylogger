from pynput import keyboard

keys = []


def strip_apostrophe(key):
    return str(key).replace("'", "")


def format_key(key):
    key = strip_apostrophe(key)
    if (key == "Key.space"):
        return " "
    elif (key == "Key.esc"):
        return ""
    # If the input is a modifier key (e.g. Shift, Alt) surrond it with brackets.
    elif (len(key) > 1):
        return f"[{key}]"
    return key


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
        # Stop listener
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
