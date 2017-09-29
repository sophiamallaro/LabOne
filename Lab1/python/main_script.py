# pip install pyserial
import serial

# pip install pyrebase
import pyrebase

import time
import random
from smtpEmail import create_message, send_message

# JSON object used to configure the firebase object
config = {
  "apiKey": "AIzaSyD4Px2vgieA7bKPnjjI1CEPW5AbBg_lbXY",
  "authDomain": "peed-0xdeadbeef-lab-1.firebaseapp.com",
  "databaseURL": "https://peed-0xdeadbeef-lab-1.firebaseio.com/",
  "storageBucket": "peed-0xdeadbeef-lab-1.appspot.com"
}

# Initialize firebase and the firebase database objects
firebase = pyrebase.initialize_app(config)
database = firebase.database()

# Remove all data currently under the "Temperatures" heading on the database
database.child("Temperatures").remove()

# Reset the 'Button' entry in the data base. (might remove this, will talk to Jason....)
database.child().update({'Button': 0})

# Initialize serial connection. May need to change COM #
ser = serial.Serial('COM6', baudrate=9600, timeout=1)

ser.write(b't')
response = ser.readline().decode('ascii')
count = 0
while count < 10:
    ser.write(b't')
    arduino_junk = ser.readline().decode('ascii')
    count += 1


# Initial sleep of 1 second before collecting data just to be safe
time.sleep(3)

# This function is used to retrieve a temperature value from the arduino
def get_temperature_value():
    ser.write(b't')
    arduino_data = ser.readline().decode('ascii')
    if arduino_data == '':
        return 40.0
    else:
        arduino_data = float(arduino_data)
        if arduino_data > max_temp:
            message = create_message(phone_number, 'Too Hot', 'The temperature is too high!')
            send_message(message)        
        elif arduino_data < min_temp:
            message = create_message(phone_number, 'Too Cold', 'The temperature is too low!')
            send_message(message)
      
    print(arduino_data)
    return float(arduino_data)
    
show_data = True


def check_switch(current_value):
    ser.write(b's')
    switch_data = ser.readline().decode('ascii')
    print(switch_data)
    if switch_data == 'y':
        if not current_value:
            database.child().update({'ShowData': True})
            current_value = True
    else:
        if current_value:
            database.child().update({'ShowData': False})
            current_value = False
    return current_value
    

# This function is called when the arduino should turn on its LEDs
def arduino_led_on():
    # one line functions, now that's pythonic!
    ser.write(b'o')
    

# This function is called when the arduino should turn off its LEDs
def arduino_led_off():
    ser.wrte(b'f')
    


# i is used to keep track of the current index in the database
i = 0

# Every time tick == 10, we send a new data point to the database
tick = 0
inner_tick = 0
database.child().update({'ShowData': True})
# boolean to keep track of transitions from 0->1 and 1->0 in the database
button_toggled = False


database_initial_state = database.child().get()

print(database_initial_state.val())

database_dict = database_initial_state.val()
max_temp = database_dict['MaxTemp']
min_temp = database_dict['MinTemp']
phone_number = database_dict['PhoneNumber']




# ------------------------------------------------ Main loop ----------------------------------------------------------#
# 10 times per second check if the button is pressed, 1 time per second send temperature data
while 1:
    # If tick == 9, then 1 second has passed since the last temperature was pulled from the arduino (10 loop iterations)
    if tick == 9:
        # Create simple JSON object to store temperature, and send it off to the database
        data_point = {
            str(i): get_temperature_value()
            # str(i): random.uniform(-50, 100) # This line was used for debugging when I didn't have the arduino
        }
        result = database.child("Temperatures").update(data_point)


        # Increment i, reset tick
        
        if inner_tick == 5:
            database_initial_state = database.child().get()

            print(database_initial_state.val())
        
            database_dict = database_initial_state.val()
            max_temp = database_dict['MaxTemp']
            min_temp = database_dict['MinTemp']
            phone_number = database_dict['PhoneNumber']
            inner_tick = 0
            
        i += 1
        tick = 0
        inner_tick += 1

    if tick == 4:
        # Every time through the loop we also want to check that the switch hasn't been flipped
        show_data = check_switch(show_data)
    # Every time through the loop we want to make sure that the button hasn't been pressed on the web app
    # With sleep set to 0.1, this will happen 10 times per second. We can reduce the sleep time to reduce latency
    result = database.child().get()

    # In this case, database.child().get returns an ordered dictionary. The key 'Button' corresponds to the
    # value in the database that is used to control button toggles.
    if result.val()['Button'] == 1:
        if not button_toggled: # LEDs currently off
            button_toggled = True
            arduino_led_on() # Turn on LEDs

        #print("Button on") # Print statement for debugging.

    else:  # Button set to 0. If button was previously on, we need to tell the arduino to turn off the LED
        if button_toggled: # LED's currently on
            button_toggled = False
            arduino_led_off() # Turn off LEDs

        #print("Button off") # Print statement for debugging.

  
    
    print('tick')
    # Increment tick, and sleep for 0.08 seconds
    tick += 1
    time.sleep(0.08)

