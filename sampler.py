#!/usr/bin/env python3

import csv
import serial
import time
import table

port = "COM9"
baud = 115200
s = serial.Serial(port)
s.baudrate = baud
threshold = 3

def main():
    """
    Starts reading from the given serial port
    Writes to a specific CSV file as opened, depending on the data transmitted by the microbit
    """
    light_sample_count = 0
    tempe_sample_count = 0

    with open('light_data.csv', 'w', newline='') as file:
        light_writer = csv.writer(file)
        light_writer.writerow(["Temperature Sample Count", "timeDate", "value"])
    with open('tempe_data.csv', 'w', newline='') as file:
        tempe_writer = csv.writer(file)
        tempe_writer.writerow(["Temperature Sample Count", "timeDate", "value"])
    # Opens individual CSV file for both sensor values
    while True:
        sensor = s.readline()
        sensor = str(sensor[0:5])[1:]
        # Reads the serial port & separates the sensor part
        timestamp = time.ctime()
        print(timestamp)
        data = s.readline()
        data = int(data[0:5])
        # Reads the serial port & separates the data part
        if sensor == "'light'":
            print(sensor)
            if data:
                light_sample_count += 1
                print(data)
            fields = [light_sample_count, timestamp, data]
            with open(r'light_data.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(fields)
        # Adds data & time stamp to CSV file
        elif sensor == "'tempe'":
            print(sensor)
            if data:
                tempe_sample_count += 1
                print(data)
            fields = [tempe_sample_count, timestamp, data]
            with open(r'tempe_data.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(fields)
        # Adds data & time stamp to CSV file
        time.sleep(3600)

        if (light_sample_count >= threshold) and (tempe_sample_count >= threshold):
            break;
        # Stops sampling when the amount of collected samples goes above the threshold
if __name__ == "__main__":
    main()





