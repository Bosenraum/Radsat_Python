import serial
import random
import socket
import crcmod
import time

host = socket.gethostname()

timeout 			= None			# port timeout; None = wait forever

# TILE PACKET DATA (52 bytes)
# Packet bytes, must be added to array in single bytes
SYNC 				= 0xC0			# 1 byte
TILE_PKT_TYPE 		= 0x88			# 1 byte
S6_COUNT 			= 0x00
S6_COUNT_1			= 0x00
S6_COUNT_2			= 0xBB
S6_COUNT_3			= 0xAA			# 4 bytes
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
FAULTS_INJECTED		= 0x00
FAULTS_INJECTED_1	= 0x09			# 2 bytes
TOTAL_FAULTS		= 0x00
TOTAL_FAULTS_1		= 0x0B			# 2 bytes
MOVE_TILE_COUNT		= 0x00
MOVE_TILE_COUNT_1	= 0x0A			# 2 bytes
NEXT_SPARE			= 0x01			# 1 byte
READBACK_FAULTS		= 0x00
READBACK_FAULTS_1	= 0x0C			# 2 bytes
WATCHDOG			= 0x00			# 1 byte
ACT_PROC1    		= 0x01			# 1 bytes
ACT_PROC2    		= 0x02			# 1 bytes
ACT_PROC3    		= 0x03			# 1 bytes
ACT_PROC1_CNT		= 0x00
ACT_PROC1_CNT_1		= 0xAA			# 2 bytes
ACT_PROC2_CNT		= 0x00
ACT_PROC2_CNT_1		= 0xBB			# 2 bytes
ACT_PROC3_CNT		= 0x00
ACT_PROC3_CNT_1		= 0xCC			# 2 bytes
VOTER_CNTS			= 0x55
VOTER_CNTS_1		= 0x66			# 2 bytes


# HEALTH PACKET DATA
HEALTH_PKT_TYPE			= 0x33		# 1 byte
VOLTAGE_INS_BATT	    = 0
VOLTAGE_INS_BATT_1      = 1
VOLTAGE_AVE_BATT        = random.randint(0, 255)
VOLTAGE_AVE_BATT_1      = random.randint(0, 255)
VOLTAGE_MAX_BATT        = random.randint(0, 255)
VOLTAGE_MAX_BATT_1      = random.randint(0, 255)
VOLTAGE_MIN_BATT        = random.randint(0, 255)
VOLTAGE_MIN_BATT_1      = random.randint(0, 255)
VOLTAGE_INS_15V0A       = random.randint(0, 255)
VOLTAGE_INS_15V0A_1     = random.randint(0, 255)
VOLTAGE_AVE_15V0A       = random.randint(0, 255)
VOLTAGE_AVE_15V0A_1     = random.randint(0, 255)
VOLTAGE_MAX_15V0A       = random.randint(0, 255)
VOLTAGE_MAX_15V0A_1     = random.randint(0, 255)
VOLTAGE_MIN_15V0A       = random.randint(0, 255)
VOLTAGE_MIN_15V0A_1     = random.randint(0, 255)
VOLTAGE_INS_N3V0A       = random.randint(0, 255)
VOLTAGE_INS_N3V0A_1     = random.randint(0, 255)
VOLTAGE_AVE_N3V0A       = random.randint(0, 255)
VOLTAGE_AVE_N3V0A_1     = random.randint(0, 255)
VOLTAGE_MAX_N3V0A       = random.randint(0, 255)
VOLTAGE_MAX_N3V0A_1     = random.randint(0, 255)
VOLTAGE_MIN_N3V0A       = random.randint(0, 255)
VOLTAGE_MIN_N3V0A_1     = random.randint(0, 255)
VOLTAGE_INS_3V3D        = random.randint(0, 255)
VOLTAGE_AVE_3V3D        = random.randint(0, 255)
VOLTAGE_MAX_3V3D        = random.randint(0, 255)
VOLTAGE_MIN_3V3D        = random.randint(0, 255)
VOLTAGE_INS_3V3D_1      = random.randint(0, 255)
VOLTAGE_AVE_3V3D_1      = random.randint(0, 255)
VOLTAGE_MAX_3V3D_1      = random.randint(0, 255)
VOLTAGE_MIN_3V3D_1      = random.randint(0, 255)
VOLTAGE_INS__3V0A       = random.randint(0, 255)
VOLTAGE_AVE__3V0A       = random.randint(0, 255)
VOLTAGE_MAX__3V0A       = random.randint(0, 255)
VOLTAGE_MIN__3V0A       = random.randint(0, 255)
VOLTAGE_INS__3V0A_1     = random.randint(0, 255)
VOLTAGE_AVE__3V0A_1     = random.randint(0, 255)
VOLTAGE_MAX__3V0A_1     = random.randint(0, 255)
VOLTAGE_MIN__3V0A_1     = random.randint(0, 255)
VOLTAGE_INS_2V5D        = random.randint(0, 255)
VOLTAGE_AVE_2V5D        = random.randint(0, 255)
VOLTAGE_MAX_2V5D        = random.randint(0, 255)
VOLTAGE_MIN_2V5D        = random.randint(0, 255)
VOLTAGE_INS_2V5D_1      = random.randint(0, 255)
VOLTAGE_AVE_2V5D_1      = random.randint(0, 255)
VOLTAGE_MAX_2V5D_1      = random.randint(0, 255)		# Byte 46, does not break if equal to 0xC0
VOLTAGE_MIN_2V5D_1      = random.randint(0, 255)
VOLTAGE_INS_2V5FA       = random.randint(0, 255)
VOLTAGE_AVE_2V5FA       = random.randint(0, 255)
VOLTAGE_MAX_2V5FA       = random.randint(0, 255)
VOLTAGE_MIN_2V5FA       = random.randint(0, 255)
VOLTAGE_INS_2V5FA_1     = random.randint(0, 255)
VOLTAGE_AVE_2V5FA_1     = random.randint(0, 255)
VOLTAGE_MAX_2V5FA_1     = random.randint(0, 255)
VOLTAGE_MIN_2V5FA_1     = random.randint(0, 255)

VOLTAGE_INS_2V5RA       = random.randint(0, 255)
VOLTAGE_AVE_2V5RA       = random.randint(0, 255)
VOLTAGE_MAX_2V5RA       = random.randint(0, 255)
VOLTAGE_MIN_2V5RA       = random.randint(0, 255)
VOLTAGE_INS_2V5RA_1     = random.randint(0, 255)
VOLTAGE_AVE_2V5RA_1     = random.randint(0, 255)
VOLTAGE_MAX_2V5RA_1     = random.randint(0, 255)
VOLTAGE_MIN_2V5RA_1     = random.randint(0, 255)
VOLTAGE_INS_1V8D        = random.randint(0, 255)
VOLTAGE_AVE_1V8D        = random.randint(0, 255)
VOLTAGE_MAX_1V8D        = random.randint(0, 255)
VOLTAGE_MIN_1V8D        = random.randint(0, 255)
VOLTAGE_INS_1V8D_1      = random.randint(0, 255)
VOLTAGE_AVE_1V8D_1      = random.randint(0, 255)
VOLTAGE_MAX_1V8D_1      = random.randint(0, 255)
VOLTAGE_MIN_1V8D_1      = random.randint(0, 255)
VOLTAGE_INS_1V0SD       = random.randint(0, 255)
VOLTAGE_AVE_1V0SD       = random.randint(0, 255)
VOLTAGE_MAX_1V0SD       = random.randint(0, 255)
VOLTAGE_MIN_1V0SD       = random.randint(0, 255)
VOLTAGE_INS_1V0SD_1     = random.randint(0, 255)
VOLTAGE_AVE_1V0SD_1     = random.randint(0, 255)
VOLTAGE_MAX_1V0SD_1     = random.randint(0, 255)
VOLTAGE_MIN_1V0SD_1     = random.randint(0, 255)
VOLTAGE_INS_1V0VD       = random.randint(0, 255)
VOLTAGE_AVE_1V0VD       = random.randint(0, 255)
VOLTAGE_MAX_1V0VD       = random.randint(0, 255)
VOLTAGE_MIN_1V0VD       = random.randint(0, 255)
VOLTAGE_INS_1V0VD_1     = random.randint(0, 255)
VOLTAGE_AVE_1V0VD_1     = random.randint(0, 255)
VOLTAGE_MAX_1V0VD_1     = random.randint(0, 255)
VOLTAGE_MIN_1V0VD_1     = random.randint(0, 255)

CURRENT_INS_BATT        = random.randint(0, 255)
CURRENT_AVE_BATT        = random.randint(0, 255)
CURRENT_MAX_BATT        = random.randint(0, 255)
CURRENT_MIN_BATT        = random.randint(0, 255)
CURRENT_INS_BATT_1      = random.randint(0, 255)
CURRENT_AVE_BATT_1      = random.randint(0, 255)
CURRENT_MAX_BATT_1      = random.randint(0, 255)
CURRENT_MIN_BATT_1      = random.randint(0, 255)
CURRENT_INS_15V0A       = random.randint(0, 255)
CURRENT_AVE_15V0A       = random.randint(0, 255)
CURRENT_MAX_15V0A       = random.randint(0, 255)
CURRENT_MIN_15V0A       = random.randint(0, 255)
CURRENT_INS_15V0A_1     = random.randint(0, 255)
CURRENT_AVE_15V0A_1     = random.randint(0, 255)
CURRENT_MAX_15V0A_1     = random.randint(0, 255)
CURRENT_MIN_15V0A_1     = random.randint(0, 255)
CURRENT_INS_N3V0A       = random.randint(0, 255)
CURRENT_AVE_N3V0A       = random.randint(0, 255)
CURRENT_MAX_N3V0A       = random.randint(0, 255)
CURRENT_MIN_N3V0A       = random.randint(0, 255)
CURRENT_INS_N3V0A_1     = random.randint(0, 255)
CURRENT_AVE_N3V0A_1     = random.randint(0, 255)
CURRENT_MAX_N3V0A_1     = random.randint(0, 255)
CURRENT_MIN_N3V0A_1     = random.randint(0, 255)
CURRENT_INS_3V3D        = random.randint(0, 255)
CURRENT_AVE_3V3D        = random.randint(0, 255)
CURRENT_MAX_3V3D        = random.randint(0, 255)
CURRENT_MIN_3V3D        = random.randint(0, 255)
CURRENT_INS_3V3D_1      = random.randint(0, 255)
CURRENT_AVE_3V3D_1      = random.randint(0, 255)
CURRENT_MAX_3V3D_1      = random.randint(0, 255)
CURRENT_MIN_3V3D_1      = random.randint(0, 255)
CURRENT_INS_3V0A        = random.randint(0, 255)
CURRENT_AVE_3V0A        = random.randint(0, 255)
CURRENT_MAX_3V0A        = random.randint(0, 255)
CURRENT_MIN_3V0A        = random.randint(0, 255)
CURRENT_INS_3V0A_1      = random.randint(0, 255)
CURRENT_AVE_3V0A_1      = random.randint(0, 255)
CURRENT_MAX_3V0A_1      = random.randint(0, 255)
CURRENT_MIN_3V0A_1      = random.randint(0, 255)

CURRENT_INS_2V5D        = random.randint(0, 255)
CURRENT_AVE_2V5D        = random.randint(0, 255)
CURRENT_MAX_2V5D        = random.randint(0, 255)
CURRENT_MIN_2V5D        = random.randint(0, 255)
CURRENT_INS_2V5D_1      = random.randint(0, 255)
CURRENT_AVE_2V5D_1      = random.randint(0, 255)
CURRENT_MAX_2V5D_1      = random.randint(0, 255)
CURRENT_MIN_2V5D_1      = random.randint(0, 255)
CURRENT_INS_2V5FA       = random.randint(0, 255)
CURRENT_AVE_2V5FA       = random.randint(0, 255)
CURRENT_MAX_2V5FA       = random.randint(0, 255)
CURRENT_MIN_2V5FA       = random.randint(0, 255)
CURRENT_INS_2V5FA_1     = random.randint(0, 255)
CURRENT_AVE_2V5FA_1     = random.randint(0, 255)
CURRENT_MAX_2V5FA_1     = random.randint(0, 255)
CURRENT_MIN_2V5FA_1     = random.randint(0, 255)
CURRENT_INS_2V5RA       = random.randint(0, 255)
CURRENT_AVE_2V5RA       = random.randint(0, 255)
CURRENT_MAX_2V5RA       = random.randint(0, 255)
CURRENT_MIN_2V5RA       = random.randint(0, 255)
CURRENT_INS_2V5RA_1     = random.randint(0, 255)
CURRENT_AVE_2V5RA_1     = random.randint(0, 255)
CURRENT_MAX_2V5RA_1     = random.randint(0, 255)
CURRENT_MIN_2V5RA_1     = random.randint(0, 255)
CURRENT_INS_1V8D        = random.randint(0, 255)
CURRENT_AVE_1V8D        = random.randint(0, 255)
CURRENT_MAX_1V8D        = random.randint(0, 255)
CURRENT_MIN_1V8D        = random.randint(0, 255)
CURRENT_INS_1V8D_1      = random.randint(0, 255)
CURRENT_AVE_1V8D_1      = random.randint(0, 255)
CURRENT_MAX_1V8D_1      = random.randint(0, 255)
CURRENT_MIN_1V8D_1      = random.randint(0, 255)
CURRENT_INS_1V0SD       = random.randint(0, 255)
CURRENT_AVE_1V0SD       = random.randint(0, 255)
CURRENT_MAX_1V0SD       = random.randint(0, 255)
CURRENT_MIN_1V0SD       = random.randint(0, 255)
CURRENT_INS_1V0SD_1     = random.randint(0, 255)
CURRENT_AVE_1V0SD_1     = random.randint(0, 255)
CURRENT_MAX_1V0SD_1     = random.randint(0, 255)
CURRENT_MIN_1V0SD_1     = random.randint(0, 255)
CURRENT_INS_1V0VD       = random.randint(0, 255)
CURRENT_AVE_1V0VD       = random.randint(0, 255)
CURRENT_MAX_1V0VD       = random.randint(0, 255)
CURRENT_MIN_1V0VD       = random.randint(0, 255)
CURRENT_INS_1V0VD_1     = random.randint(0, 255)
CURRENT_AVE_1V0VD_1     = random.randint(0, 255)
CURRENT_MAX_1V0VD_1     = random.randint(0, 255)
CURRENT_MIN_1V0VD_1     = random.randint(0, 255)

V6_TEMPERATURE          = 0x80
PC1_TEMPERATURE         = 0x81
PC1_EXT_TEMPERATURE     = 0x81
PC2_TEMPERATURE         = 0x82
PC2_EXT_TEMPERATURE     = 0x82
SYSTEM_RUNTIME_DAYS     = 0x00
SYSTEM_RUNTIME_DAYS_1   = 0x07
SYSTEM_RUNTIME_MS       = 0xFF
SYSTEM_RUNTIME_MS_1     = 0xB5
SYSTEM_STATUS_FLAG      = 0x00
SYSTEM_STATUS_FLAG_1    = 0x01



# Create packet structure
TLM_TILE_PKT = bytearray([SYNC, TILE_PKT_TYPE, S6_COUNT, S6_COUNT_1, S6_COUNT_2, S6_COUNT_3, ACT_TILES,
						  ACT_TILES_1, FAULTED_TILES, FAULTED_TILES_1, FAULT_COUNT_TILE0,
						  FAULT_COUNT_TILE0_1, FAULT_COUNT_TILE1, FAULT_COUNT_TILE1_1, FAULT_COUNT_TILE2,
						  FAULT_COUNT_TILE2_1, FAULT_COUNT_TILE3, FAULT_COUNT_TILE3_1, FAULT_COUNT_TILE4,
						  FAULT_COUNT_TILE4_1, FAULT_COUNT_TILE5, FAULT_COUNT_TILE5_1, FAULT_COUNT_TILE6,
						  FAULT_COUNT_TILE6_1, FAULT_COUNT_TILE7, FAULT_COUNT_TILE7_1, FAULT_COUNT_TILE8,
						  FAULT_COUNT_TILE8_1, FAULTS_INJECTED, FAULTED_TILES_1, TOTAL_FAULTS,
						  TOTAL_FAULTS_1, MOVE_TILE_COUNT, MOVE_TILE_COUNT_1, NEXT_SPARE, READBACK_FAULTS,
						  READBACK_FAULTS_1, WATCHDOG, ACT_PROC1, ACT_PROC2, ACT_PROC3, ACT_PROC1_CNT,
						  ACT_PROC1_CNT_1, ACT_PROC2_CNT, ACT_PROC2_CNT_1, ACT_PROC3_CNT, ACT_PROC3_CNT_1,
						  VOTER_CNTS, VOTER_CNTS_1])

TLM_HEALTH_PKT = bytearray([SYNC, HEALTH_PKT_TYPE,
							VOLTAGE_INS_BATT, VOLTAGE_INS_BATT_1, VOLTAGE_AVE_BATT, VOLTAGE_AVE_BATT_1,
							VOLTAGE_MAX_BATT, VOLTAGE_MAX_BATT_1, VOLTAGE_MIN_BATT, VOLTAGE_MIN_BATT_1,
							VOLTAGE_INS_15V0A, VOLTAGE_INS_15V0A_1, VOLTAGE_AVE_15V0A, VOLTAGE_AVE_15V0A_1,
							VOLTAGE_MAX_15V0A, VOLTAGE_MAX_15V0A_1, VOLTAGE_MIN_15V0A, VOLTAGE_MIN_15V0A_1,
							VOLTAGE_INS_N3V0A, VOLTAGE_INS_N3V0A_1, VOLTAGE_AVE_N3V0A, VOLTAGE_AVE_N3V0A_1,
							VOLTAGE_MAX_N3V0A, VOLTAGE_MAX_N3V0A_1, VOLTAGE_MIN_N3V0A, VOLTAGE_MIN_N3V0A_1,
							VOLTAGE_INS_3V3D, VOLTAGE_AVE_3V3D, VOLTAGE_MAX_3V3D, VOLTAGE_MIN_3V3D,
							VOLTAGE_INS_3V3D_1, VOLTAGE_AVE_3V3D_1, VOLTAGE_MAX_3V3D_1, VOLTAGE_MIN_3V3D_1,
							VOLTAGE_INS__3V0A, VOLTAGE_AVE__3V0A, VOLTAGE_MAX__3V0A, VOLTAGE_MIN__3V0A,
							VOLTAGE_INS__3V0A_1, VOLTAGE_AVE__3V0A_1, VOLTAGE_MAX__3V0A_1, VOLTAGE_MIN__3V0A_1,
							VOLTAGE_INS_2V5D, VOLTAGE_AVE_2V5D, VOLTAGE_MAX_2V5D, VOLTAGE_MIN_2V5D,
							VOLTAGE_INS_2V5D_1, VOLTAGE_AVE_2V5D_1, VOLTAGE_MAX_2V5D_1, VOLTAGE_MIN_2V5D_1,
							VOLTAGE_INS_2V5FA, VOLTAGE_AVE_2V5FA, VOLTAGE_MAX_2V5FA, VOLTAGE_MIN_2V5FA,
							VOLTAGE_INS_2V5FA_1, VOLTAGE_AVE_2V5FA_1, VOLTAGE_MAX_2V5FA_1, VOLTAGE_MIN_2V5FA_1,
							VOLTAGE_INS_2V5RA, VOLTAGE_AVE_2V5RA, VOLTAGE_MAX_2V5RA, VOLTAGE_MIN_2V5RA,
							VOLTAGE_INS_2V5RA_1, VOLTAGE_AVE_2V5RA_1, VOLTAGE_MAX_2V5RA_1, VOLTAGE_MIN_2V5RA_1,
							VOLTAGE_INS_1V8D, VOLTAGE_AVE_1V8D, VOLTAGE_MAX_1V8D, VOLTAGE_MIN_1V8D,
							VOLTAGE_INS_1V8D_1, VOLTAGE_AVE_1V8D_1, VOLTAGE_MAX_1V8D_1, VOLTAGE_MIN_1V8D_1,
							VOLTAGE_INS_1V0SD, VOLTAGE_AVE_1V0SD, VOLTAGE_MAX_1V0SD, VOLTAGE_MIN_1V0SD,
							VOLTAGE_INS_1V0SD_1, VOLTAGE_AVE_1V0SD_1, VOLTAGE_MAX_1V0SD_1, VOLTAGE_MIN_1V0SD_1,
							VOLTAGE_INS_1V0VD, VOLTAGE_AVE_1V0VD, VOLTAGE_MAX_1V0VD, VOLTAGE_MIN_1V0VD,
							VOLTAGE_INS_1V0VD_1, VOLTAGE_AVE_1V0VD_1, VOLTAGE_MAX_1V0VD_1, VOLTAGE_MIN_1V0VD_1,
							CURRENT_INS_BATT, CURRENT_AVE_BATT, CURRENT_MAX_BATT, CURRENT_MIN_BATT,
							CURRENT_INS_BATT_1, CURRENT_AVE_BATT_1, CURRENT_MAX_BATT_1, CURRENT_MIN_BATT_1,
							CURRENT_INS_15V0A, CURRENT_AVE_15V0A, CURRENT_MAX_15V0A, CURRENT_MIN_15V0A,
							CURRENT_INS_15V0A_1, CURRENT_AVE_15V0A_1, CURRENT_MAX_15V0A_1, CURRENT_MIN_15V0A_1,
							CURRENT_INS_N3V0A, CURRENT_AVE_N3V0A, CURRENT_MAX_N3V0A, CURRENT_MIN_N3V0A,
							CURRENT_INS_N3V0A_1, CURRENT_AVE_N3V0A_1, CURRENT_MAX_N3V0A_1, CURRENT_MIN_N3V0A_1,
							CURRENT_INS_3V3D, CURRENT_AVE_3V3D, CURRENT_MAX_3V3D, CURRENT_MIN_3V3D,
							CURRENT_INS_3V3D_1, CURRENT_AVE_3V3D_1])


#TEST_PKT = bytearray("Hello World!", "utf8")

def split_crc(crc16):
	crc16_int = int(crc16, 16)
	a = (crc16_int >> 8) & 0xFF
	b = crc16_int & 0xFF
	return {'CRC':a, 'CRC_1':b}

# Create the crc function
#CRC16 = crcmod.predefined.Crc('xmodem')
CRC16_fun = crcmod.mkCrcFun(0x11021, initCrc=0xFFFF, rev=False)

# crc_L = []
# # CRC testing
# for i in range(49):
# 	crc_L.append(i)

# TLM_TEST_PKT = bytearray(crc_L)
#
# TEST_CRC = CRC16_fun(TLM_TEST_PKT)
# print("TEST_CRC: " + format(TEST_CRC, '04X'))
# FULL_CRC = split_crc(format(TEST_CRC, '04X'))
# #print(format(FULL_CRC['CRC'], '02X') + " " + format(FULL_CRC['CRC_1'], '02X'))
# CRC = FULL_CRC['CRC']
# CRC_1 = FULL_CRC['CRC_1']
#
# TLM_TEST_PKT.append(CRC)
# TLM_TEST_PKT.append(CRC_1)
# # add the final sync byte
# TLM_TEST_PKT.append(SYNC)
#
# test_out = ''
# for i in range(0, len(TLM_TEST_PKT)):
# 	test_out += format(TLM_TEST_PKT[i],'02X') + ' '
#
# print("TEST_PKT is " + str(len(TLM_TEST_PKT)) + " bytes long.")
# print("TEST_PKT: " + test_out)
# print()


# Create CRC for TILE packet
#CRC16.update(TLM_TILE_PKT)
TILE_CRC = CRC16_fun(TLM_TILE_PKT)
print("TILE_CRC: " + format(TILE_CRC, '04X'))
FULL_CRC = split_crc(format(TILE_CRC, '04X'))
#print(format(FULL_CRC['CRC'], '02X') + " " + format(FULL_CRC['CRC_1'], '02X'))
CRC = 0xCC #FULL_CRC['CRC']
CRC_1 = 0xCC #FULL_CRC['CRC_1']

# append crc bytes to the packet
TLM_TILE_PKT.append(CRC)
TLM_TILE_PKT.append(CRC_1)
# add the final sync byte
TLM_TILE_PKT.append(SYNC)

# Create CRC for HEALTH packet
HEALTH_CRC = CRC16_fun(TLM_HEALTH_PKT)
print("HEALTH_CRC: " + format(HEALTH_CRC, '04X'))
FULL_CRC = split_crc(format(HEALTH_CRC, '04X'))
#print(format(FULL_CRC['CRC'], '02X') + " " + format(FULL_CRC['CRC_1'], '02X'))
CRC = 0xCC #FULL_CRC['CRC']
CRC_1 = 0xCC #FULL_CRC['CRC_1']

# append crc bytes to the packet
TLM_HEALTH_PKT.append(CRC)
TLM_HEALTH_PKT.append(CRC_1)
# add the final sync byte
TLM_HEALTH_PKT.append(SYNC)

# Print out the packets
tile_out = ''
for i in range(0, len(TLM_TILE_PKT)):
	tile_out += format(TLM_TILE_PKT[i],'02X') + ' '

print("TILE_PKT is " + str(len(TLM_TILE_PKT)) + " bytes long.")
print("TILE_PKT: " + tile_out)
print()

output = ''
for i in range(len(TLM_HEALTH_PKT)):
	output += format(TLM_HEALTH_PKT[i], '02X') + ' '

print("TILE_PKT is " + str(len(TLM_HEALTH_PKT)) + " bytes long.")
print("HEALTH_PKT: " + output)
print()

# Setup and open serial port
if host == 'bz-ece-hsddl03':
    uart1 = serial.Serial(port = 'COM5', baudrate = 115200)
elif host == 'bz-ece-hsddl05':
    uart1 = serial.Serial(port = 'COM3', baudrate = 115200, timeout = timeout)
elif host == 'bz-ece-hsddl07':
	print("TEST COMPLETE")
	quit()

# Loop forever waiting for commands
# Will send the correct packet (TILE or HEALTH) depending on the command received
while(True):
	print("WAITING FOR COMMAND...")
	cmd = uart1.read(1)
	#time.sleep(2)

	print()
	#print("WAITING FOR COMMAND...")
	print("RECEIVED COMMAND: " + str(cmd))
	print()

	if(int.from_bytes(cmd, byteorder='big') == 136):
		print("TILE COMMAND RECEIVED")
		print("SENDING TILE PACKET")
		# Send TILE PACKET
		uart1.write(TLM_TILE_PKT)
		print("SENT TILE PKT")

	elif(int.from_bytes(cmd, byteorder='big') == 51):
		print("HEALTH COMMAND RECEIVED")
		print("SENDING HEALTH PACKET")

		# Send HEALTH PACKET
		uart1.write(TLM_HEALTH_PKT)
		print("SENT HEALTH PKT")

	elif(int.from_bytes(cmd, byteorder='big') == 61):
		print("TEST COMMAND RECEIVED")
		print("SENDING TEST PACKET")

		uart1.write("HELLO WORLD")
		print("SENT TEST PKT")

	else:
		# Print the incorrect packet and stop execution, also catches timeout
		if(int.from_bytes(cmd, byteorder='big') == 0):
			print("TIMEOUT")
		else:
			print("COMMAND NOT RECOGNIZED")
			print("CMD: " + str(cmd))
		#print("EXITING")
		#break;
