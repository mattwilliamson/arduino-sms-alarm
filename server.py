#!/usr/bin/env python

import serial
import requests
from datetime import datetime, timedelta

# Set the serial port to the same serial port you uploaded the arduino sketch to
# In the Arduino IDE, click "Tools > Serial Port"
# SERIAL_PORT = "/dev/tty.usbserial-A70064Mh"
SERIAL_PORT = "/dev/tty.usbserial-AH00PP05"
SERIAL_BAUD = 115200

# Don"t send more than one message every 30 minutes
SENSOR_INTERVAL = timedelta(minutes=30)

SMS_FROM = "YOUR TELAPI NUMBER" # Make sure this is a number on telapi.com or you'll get charged extra for spoofing
SMS_TO = "YOUR CELL PHONE NUMBER"
SMS_BODY = "ALERT! Your Arduino just detected motion!"
TELAPI_ACCOUNT_SID = "YOUR TELAPI ACCOUNT SID"
TELAPI_TOKEN = "YOUR TELAPI ACCOUNT TOKEN"

# Try to import TELAPI_ACCOUNT_SID and such from settings_local.py, if it exists
try:
    from settings_local import *
except ImportError:
    pass

TELAPI_SMS_URL = "https://api.telapi.com/2011-07-01/Accounts/%s/SMS/Messages" % TELAPI_ACCOUNT_SID

# Start the server
if __name__ == "__main__":
    print "Starting SMS motion detector server at", datetime.now()
    last_sent_time = None

    # Open a serial connection to the Arduino
    with serial.Serial(SERIAL_PORT, SERIAL_BAUD) as arduino:
        while True:
            print "Polling Arduino..."

            # Listen for the Arduino to send a byte
            byte_received = arduino.read()

            print "Received byte:", byte_received

            # Motion was detected
            if byte_received == "1":
                print "Motion detected at", datetime.now()

                # If we haven"t sent an SMS in the last 30 minutes, send one now
                if not last_sent_time or (datetime.now() - last_sent_time) > SENSOR_INTERVAL:
                    last_sent_time = datetime.now()
                    print "Sending SMS..."

                    # Send request to TelAPI to send SMS
                    try:
                        data = {
                            "From": SMS_FROM,
                            "To": SMS_TO,
                            "Body": SMS_BODY,
                        }
                        requests.post(TELAPI_SMS_URL, data=data, auth=(TELAPI_ACCOUNT_SID, TELAPI_TOKEN))

                        print "** SMS Sent! **"

                    except Exception as e:
                        print "Some error occurred while sending SMS:", e
