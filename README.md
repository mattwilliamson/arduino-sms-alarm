Arduino SMS Alarm
=================

An Arduino based burglar alarm that sends an SMS when motion is detected. 
It will send an SMS to you every 30 minutes while motion is detected (configurable).

![SMS Screenshot](https://raw.github.com/mattwilliamson/arduino-sms-alarm/master/action_shots/sms.png)


## Requirements

* Python
* Python library *pyserial* installed
* Python library *requests* installed
* A [TelAPI](http://goo.gl/A36VN) account
* An [Arduino](http://arduino.cc)
* A [Parallax PIR sensor](http://www.parallax.com/tabid/768/ProductID/83/Default.aspx)
* Some [female-female jumper wires](http://adafruit.com/products/266)
* Some [break-away headers](http://www.adafruit.com/products/400) (to convert female to male)

![PIR Sensor](https://raw.github.com/mattwilliamson/arduino-sms-alarm/master/action_shots/pir_sensor.png)


# Set up


## Wire it up!

1. Attach **+** on the PIR sensor to **5v** on the Arduino
1. Attach **-** on the PIR sensor to **GND** on the Arduino
1. Attach **OUT** on the PIR sensor to **DIGITAL 2** on the Arduino

![Schematic](https://raw.github.com/mattwilliamson/arduino-sms-alarm/master/action_shots/Schematic_bb.png)
![Wired Up](https://raw.github.com/mattwilliamson/arduino-sms-alarm/master/action_shots/wired_up.png)


## Upload the sketch

1. Plug your Arduino into your computer
1. Open the `arduino_pir/arduino_pit.ino` sketch with the Arduino IDE
1. Select your serial port (Tools>Serial Port) and click Upload

Your arduino LED will now be blnking. This means the PIR sensor is calibrating.


## Setup the server

1. Open server.py with a text editor
1. Change the value of `SERIAL_PORT` to the serial port you set in the Arduino IDE. For Windows it might look like *COM2*, for Posix systems, it might look like */dev/tty.usbserial-AH00PP05*
1. Change the value of `SMS_FROM` to the number in your [TelAPI account numbers](http://www.telapi.com/numbers/) (You can set this to another number, such as your own phone and it will cost a little extra. This is what I do.)
1. Change the value `SMS_TO` to your cell phone
1. Change the value of `TELAPI_ACCOUNT_SID` to your `Account SID` as found at [your TelAPI dashboard](http://www.telapi.com/dashboard)
1. Change the value of `TELAPI_TOKEN` to your `Account Token` as found at [your TelAPI dashboard](http://www.telapi.com/dashboard)

## Run it!

1. Open up your terminal and run `python server.py` (assuming the terminal is CD'd to the directory where server.py is)
1. The Arduino will blink it's LED for 60 seconds. Get out of the sensor's sight while it calibrates.


Now, whevever motion is detected in the infra-red spectrum (think body heat), `server.py` will send you an SMS up to once every 30 minutes.


## Put it in a case (Optional)

1. Get some plastic case, like one from a hummus & pretzel snack
1. Cut a hole in the top for the sensor to be exposed (like R2D2 in an X-Wing)
1. Cut a hole for the USB cable to stick out
1. Tape or screw the sensor to the top
1. Finit!

![Cut a hole](https://raw.github.com/mattwilliamson/arduino-sms-alarm/master/action_shots/case.png)
![Cut a hole](https://raw.github.com/mattwilliamson/arduino-sms-alarm/master/action_shots/complete.png)



**BEEP BEEP WHISTLE**

![X-Wing Car](https://raw.github.com/mattwilliamson/arduino-sms-alarm/master/action_shots/xwingcar.jpg)

**YUM** (Makes a nice case)

![Sabra Hummus Single Serve](https://raw.github.com/mattwilliamson/arduino-sms-alarm/master/action_shots/sabra.jpg)


Free $25 credit when you sign up for a [TelAPI](http://goo.gl/A36VN) account!


