import serial

timeout = 5

uart1 = serial.Serial(port = 'COM5', baudrate = 115200, timeout = timeout)
uart1.write(bytearray([0xC0, 0xAA]))
