import serial

timeout = 0

TILE_PKT_SIZE = 52
HEALTH_PKT_SIZE = 111

uart2 = serial.Serial(port = 'COM3', baudrate = 115200, timeout = timeout)

log = open("pktlog.txt", 'wb')


while True:
    log.write(format(int(uart2.read(TILE_PKT_SIZE + 1)), '02X'))
    log.write(format(int(uart2.read(HEALTH_PKT_SIZE + 1)), '02X'))

log.close()
