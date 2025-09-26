import serial
import csv

arduinoComPort = "COM12"
baudRate = 9600
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)

with open('readings.csv', 'w', newline='') as csvfile:
  csv_writer = csv.writer(csvfile)
  data = []
  while True:
    lineOfData = serialPort.readline().decode()

    if len(lineOfData) > 0:
      a = int(lineOfData.strip())
      data.append(a)
    if len(data) == 610:
      csv_writer.writerow(data)
      break