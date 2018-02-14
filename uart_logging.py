import serial

timeout = 60

uart2 = serial.Serial(port = 'COM3', baudrate = 115200, timeout = timeout)

log = open("pktlog.txt", 'wb')
