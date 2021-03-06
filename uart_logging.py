import serial
import threading
import datetime


timeout = 0
newline = 0xA

TILE_PKT_SIZE = 52
HEALTH_PKT_SIZE = 123
port = 'COM3'

uart2 = serial.Serial(port=port, baudrate=115200, timeout=timeout)

log = open("pktlog.txt", 'w')


# Simple threaded solution to allow user input while also waiting for packets
# def get_input():
#     while True:
#         cmd = input()
#         if cmd == 'q':
#             quit()
#         #print(cmd)
#         uart2.write(cmd.encode('utf-8'))
#
# inThread = threading.Thread(target=get_input)
# inThread.start()

while True:

    now = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    log.write("-----------------------------------")
    log.write("        " + now "        ")
    log.write("-----------------------------------")

    for b in uart2.read(TILE_PKT_SIZE + 1):
        out = format(int(b), '02X') + " "
        if(int(b) == 0xA):
            log.write('\n')
            #print('\n')
        else:
            log.write(out)
            #print(out, end="")

    for b in uart2.read(HEALTH_PKT_SIZE + 1):
        out = format(int(b), '02X') + " "
        if(int(b) == 0xA):
            log.write('\n')
            #print('\n')
        else:
            log.write(out)
            #print(out, end="")

	# b = 0
	# while int(b) != 0xA:
	# 	b = uart2.read(1)
	# 	out = format(int(b), '02X') + " "
	# 	log.write(out)
	# log.write('\n')



log.close()
