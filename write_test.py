import serial

timeout = 5
port = 'COM5'

uart1 = serial.Serial(port=port, baudrate=115200, timeout=timeout)

# Write a sync byte (0xC0) and then a random data value (0xAA)
uart1.write(bytearray([0xC0, 0xAA]))
