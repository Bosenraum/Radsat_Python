import serial
import random

timeout 			= 20			# port timeout
RTC_TLM_TILE_SIZE	= 46			# Tile packet size in bytes
RTC_TLM_HEALTH_SIZE = 191			# Health packet size in bytes

HEALTH_PKT_TYPE		= 0x33			# type command for health packets

# Packet bytes, must be added to array in single bytes
SYNC 				= 0xC0			# 1 byte
TILE_PKT_TYPE 		= 0x88			# 1 byte, type command for tile packets
S6_COUNT 			= 0x00
S6_COUNT_1			= 0x00
S6_COUNT_2			= 0xFF
S6_COUNT_3			= 0xFF			# 4 bytes
ACT_TILES 			= 0x00
ACT_TILES_1			= 0x03			# 2 bytes
FAULTED_TILES		= 0x00
FAULTED_TILES_1		= 0x01			# 2 bytes
FAULT_COUNT_TILE0	= 0x00
FAULT_COUNT_TILE0_1 = 0x00			# 2 bytes
FAULT_COUNT_TILE1	= 0x00
FAULT_COUNT_TILE1_1 = 0x01			# 2 bytes
FAULT_COUNT_TILE2	= 0x00
FAULT_COUNT_TILE2_1 = 0x02			# 2 bytes
FAULT_COUNT_TILE3	= 0x00
FAULT_COUNT_TILE3_1 = 0x03			# 2 bytes
FAULT_COUNT_TILE4	= 0x00
FAULT_COUNT_TILE4_1 = 0x04			# 2 bytes
FAULT_COUNT_TILE5	= 0x00
FAULT_COUNT_TILE5_1 = 0x05			# 2 bytes
FAULT_COUNT_TILE6	= 0x00
FAULT_COUNT_TILE6_1 = 0x06			# 2 bytes
FAULT_COUNT_TILE7	= 0x00
FAULT_COUNT_TILE7_1 = 0x07			# 2 bytes
FAULT_COUNT_TILE8	= 0x00
FAULT_COUNT_TILE8_1 = 0x08			# 2 bytes
READBACK_FAULTS		= 0x00
READBACK_FAULTS_1	= 0x0C			# 2 bytes
WATCHDOG			= 0x00
WATCHDOG_1			= 0x0C			# 2 bytes
ACT_PROC1    		= 0x01			# 1 bytes
ACT_PROC2    		= 0x02			# 1 bytes
ACT_PROC3    		= 0x03			# 1 bytes
ACT_PROC1_CNT		= 0x00
ACT_PROC1_CNT_1		= 0xAA			# 2 bytes
ACT_PROC2_CNT		= 0x00
ACT_PROC2_CNT_1		= 0xBB			# 2 bytes
ACT_PROC3_CNT		= 0x00
ACT_PROC3_CNT_1		= 0xCC			# 2 bytes
VOTER_CNTS			= 0xFF
VOTER_CNTS_1		= 0xFF			# 2 bytes
CRC					= 0xAA
CRC_1				= 0xAA			# 2 bytes

def printOutput(pkt_type, output):
	print(pkt_type + ": " + output)

# Create packet structure
TLM_TILE_PKT = bytearray([SYNC, TILE_PKT_TYPE, S6_COUNT, S6_COUNT_1, S6_COUNT_2, S6_COUNT_3, ACT_TILES, 
						  ACT_TILES_1, FAULTED_TILES, FAULTED_TILES_1, FAULT_COUNT_TILE0,
						  FAULT_COUNT_TILE0_1, FAULT_COUNT_TILE1, FAULT_COUNT_TILE1_1, FAULT_COUNT_TILE2, 
						  FAULT_COUNT_TILE2_1, FAULT_COUNT_TILE3, FAULT_COUNT_TILE3_1, FAULT_COUNT_TILE4,
						  FAULT_COUNT_TILE4_1, FAULT_COUNT_TILE5, FAULT_COUNT_TILE5_1, FAULT_COUNT_TILE6, 
						  FAULT_COUNT_TILE6_1, FAULT_COUNT_TILE7, FAULT_COUNT_TILE7_1, FAULT_COUNT_TILE8,
						  FAULT_COUNT_TILE8_1, READBACK_FAULTS, READBACK_FAULTS_1, WATCHDOG, WATCHDOG_1,
						  ACT_PROC1, ACT_PROC2, ACT_PROC3, ACT_PROC1_CNT, ACT_PROC1_CNT_1,
						  ACT_PROC2_CNT, ACT_PROC2_CNT_1, ACT_PROC3_CNT, ACT_PROC3_CNT_1, VOTER_CNTS, 
						  VOTER_CNTS_1, CRC, CRC_1, SYNC])\
						  
TLM_HEALTH_PKT_L = [SYNC, HEALTH_PKT_TYPE]
for i in range(RTC_TLM_HEALTH_SIZE - 3):
	TLM_HEALTH_PKT_L.append(random.randint(0,255))
	
TLM_HEALTH_PKT_L.append(SYNC)
	
TLM_HEALTH_PKT = bytearray(TLM_HEALTH_PKT_L)

# Setup and open serial port
uart1 = serial.Serial(port = 'COM5', baudrate = 115200, timeout = timeout)
print('TILE PKT LENGTH: ' + str(len(TLM_TILE_PKT)))
output = ''

for i in range(0, len(TLM_TILE_PKT)):
	output += str(TLM_TILE_PKT[i]) + ' '
	
#printOutput('TILE PKT LENGTH', output)

print('UART Command ' + str(uart1.read(1)))

uart1.write(TLM_TILE_PKT)
print('PKT SENT')

printOutput('TILE PKT LENGTH', output)

print('Next Command: ' + str(uart1.read(1)))

#print()
print('HEALTH PKT LENGTH: ' + str(len(TLM_HEALTH_PKT)))

output = ''
for i in range(0, len(TLM_HEALTH_PKT)):
	output += str(TLM_HEALTH_PKT[i]) + ' '

uart1.write(TLM_HEALTH_PKT)

printOutput('HEALTH PKT LENGTH', output)


## send data as a byte array to avoid encoding issues
#hello_world = bytearray([SYNC, PKT_TYPE, 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x57, 0x6f, 0x72, 0x6c, 0x64, 0x21, 0x0a, SYNC])
#
#print('Sync byte: ' + str(SYNC))
#
#

#
#print('Serial port name: ' + str(uart1.name))
#
#print('UART Command ' + str(uart1.read(1)))
#
## Send desired data
#uart1.write(hello_world)
#print('Sending "└êHello World!└"')
#
#print('Next Command: ' + str(uart1.read(1)))



# receive data?