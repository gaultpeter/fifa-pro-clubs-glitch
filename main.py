import sys
import time
import pydirectinput
import PIL
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

try:
    from PIL import ImageGrab

    use_grab = True
except Exception as ex:
    if sys.platform == 'windows':
        from Xlib import display, X

        use_grab = False
    else:
        raise ex


def start_script():
    while True:
        time.sleep(1)
        print("Checking if in a game....")
        if has_game_started():
            print("In a game")
            leave_game()
        else:
            pydirectinput.press('enter')


def leave_game():
    pydirectinput.press('esc')
    time.sleep(1)
    pydirectinput.press('right')
    pydirectinput.press('down')
    pydirectinput.press('right')
    pydirectinput.press('down')
    pydirectinput.press('enter')
    time.sleep(0.5)
    pydirectinput.press('down')
    pydirectinput.press('enter')


def has_game_started():
    time_on_screen_image = PIL.ImageGrab.grab(bbox=[957, 55, 995, 71])
    time_on_screen_text = pytesseract.image_to_string(time_on_screen_image, config='--psm 6')
    time_on_screen_image.save("screenshot-time.jpg")
    return "2" in time_on_screen_text


if __name__ == '__main__':
    time.sleep(3)
    start_script()
