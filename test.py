# https://gpiozero.readthedocs.io/en/stable/api_pins.html#mock-pins
from gpiozero.pins.mock import MockFactory
from gpiozero import Device, Button
from time import sleep

# Set the default pin factory to a mock factory
Device.pin_factory = MockFactory()

button1 = Button(18)
button2 = Button(23)
button3 = Button(24)

reboot_statement = "sudo shutdown -r -f now"
shutdown_statement = "sudo shutdown -h"

held_for = 0.0

btn_pin = Device.pin_factory.pin(18)

btn_pin.drive_low()

if button1.is_pressed:
    sleep(0.1)
    print('button 1 pressed.')
if button2.is_pressed:
    sleep(0.1)
    print(f'button 2 pressed for ', held_for, ' seconds.')
if button3.is_pressed:
    sleep(0.1)
    print('button 3 pressed.')
