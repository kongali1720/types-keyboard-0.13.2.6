# tests/test_typing.py

import keyboard

def test_keyboard_typing() -> None:
    keyboard.write("Test typing stub", delay=0.01)

def test_keyboard_key_press() -> None:
    keyboard.press("a")
    keyboard.release("a")
