import pyscreenshot as ImageGrab
from time import sleep
# from pymouse import PyMouse
from pykeyboard import PyKeyboard

k = PyKeyboard()
ACTION_KEY = k.numpad_keys[6]

def pressAction(times = 1, delay = 1.0):
    for i in range(times):
        k.press_key(ACTION_KEY)
        sleep(0.25)
        k.release_key(ACTION_KEY)
        sleep(delay)

def main():
    print('Place window in top left corner of the screen')
    print('Place pokemon you want to train in slot 1 and stand in front of the trainer.')
    print('Starting training in 5 seconds...')
    sleep(5.0)
    talk()
    for i in range(10):
        print(f'Training round {i+1}')
        train()
    print('Done.')

def train():
    cont = True
    bbox = (405,680,941,764)
    # ckpos = (272,20)
    ckpos = (272,25)
    ckcolor = (0xe0,0x08,0x08)
    while cont:
        # continuously examine screen
        im = ImageGrab.grab(bbox)
        # check for red arrow in center
        pixel = im.getpixel(ckpos)
        if (pixel == ckcolor):
            cont = False
    # found good spot, hit the button
    pressAction(times = 1, delay = 1.0)


def talk():
    print('Talking to NPC...')
    pressAction(times=3, delay = 1.5)
    print('paying cash...')
    pressAction(times = 1, delay = 1.5)
    print('Choosing pokemon')
    pressAction(times=2, delay = 3)

if __name__ == '__main__':
    main();
