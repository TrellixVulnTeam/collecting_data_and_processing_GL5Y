import serial, time, csv
import numpy as np

tof = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
arduino = serial.Serial('COM4',115200,timeout=1)

print("Starting Conversation with Arduino")
print(len(tof))
SayingTo = input()

SayingToArduino = SayingTo.encode("utf-8")
arduino.write(SayingToArduino)
print(SayingToArduino)
time.sleep(1)

while True:

    while (arduino.inWaiting()==0):
        pass
    SdataPacket = arduino.readline()
    SdataPacket = str(SdataPacket, "utf-8")
    SsplitPacket = SdataPacket.split(" ")

    file_path = "C:/Users/Lab/Desktop/LYS/Coding/Python/210805_50ms_Data.csv"
    if len(SsplitPacket) >= len(tof):
        file = open(file_path, 'a',encoding = "utf-8", newline='')
        csv_writer = csv.writer(file)
        csv_writer.writerow(SsplitPacket)
        for i in range(0,17):
            tof[i] = float(SsplitPacket[i])
            print(tof[i],end=' ')
    print("")