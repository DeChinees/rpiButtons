from gpiozero import Button

button1 = Button(18)
button2 = Button(23)
button3 = Button(24)

while True:
    if button1.is_pressed:
        print('button 1 pressed.')
    if button2.is_pressed:
        print('button 2 pressed.')
    if button3.is_pressed:
        print('button 3 pressed.')