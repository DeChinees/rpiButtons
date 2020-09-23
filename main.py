from gpiozero import Button

button1 = Button(12)


def button_pressed():
    while True:
        if (button1 == 0):
            print('button 1 pressed.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    button_pressed()

