import tkinter as tk
import serial
import random

# TILE PACKET DATA
# Packet bytes, must be added to array in single bytes
SYNC 				= 0xC0			# 1 byte
TILE_PKT_TYPE 		= 0x88			# 1 byte
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
CRC					= 0x00
CRC_1				= 0x00			# 2 bytes


# HEALTH PACKET DATA
HEALTH_PKT_TYPE			= 0x33		# 1 byte
VOLTAGE_INS_BATT	    = 0
VOLTAGE_INS_BATT_1      = 1
VOLTAGE_AVE_BATT        = random.randint(0, 191)
VOLTAGE_AVE_BATT_1      = random.randint(0, 191)
VOLTAGE_MAX_BATT        = random.randint(0, 191)
VOLTAGE_MAX_BATT_1      = random.randint(0, 191)
VOLTAGE_MIN_BATT        = random.randint(0, 191)
VOLTAGE_MIN_BATT_1      = random.randint(0, 191)
VOLTAGE_INS_15V0A       = random.randint(0, 191)
VOLTAGE_INS_15V0A_1     = random.randint(0, 191)
VOLTAGE_AVE_15V0A       = random.randint(0, 191)
VOLTAGE_AVE_15V0A_1     = random.randint(0, 191)
VOLTAGE_MAX_15V0A       = random.randint(0, 191)
VOLTAGE_MAX_15V0A_1     = random.randint(0, 191)
VOLTAGE_MIN_15V0A       = random.randint(0, 191)
VOLTAGE_MIN_15V0A_1     = random.randint(0, 191)
VOLTAGE_INS_N3V0A       = random.randint(0, 191)
VOLTAGE_INS_N3V0A_1     = random.randint(0, 191)
VOLTAGE_AVE_N3V0A       = random.randint(0, 191)
VOLTAGE_AVE_N3V0A_1     = random.randint(0, 191)
VOLTAGE_MAX_N3V0A       = random.randint(0, 191)
VOLTAGE_MAX_N3V0A_1     = random.randint(0, 191)
VOLTAGE_MIN_N3V0A       = random.randint(0, 191)
VOLTAGE_MIN_N3V0A_1     = random.randint(0, 191)
VOLTAGE_INS_3V3D        = random.randint(0, 191)
VOLTAGE_AVE_3V3D        = random.randint(0, 191)
VOLTAGE_MAX_3V3D        = random.randint(0, 191)
VOLTAGE_MIN_3V3D        = random.randint(0, 191)
VOLTAGE_INS_3V3D_1      = random.randint(0, 191)
VOLTAGE_AVE_3V3D_1      = random.randint(0, 191)
VOLTAGE_MAX_3V3D_1      = random.randint(0, 191)
VOLTAGE_MIN_3V3D_1      = random.randint(0, 191)
VOLTAGE_INS__3V0A       = random.randint(0, 191)
VOLTAGE_AVE__3V0A       = random.randint(0, 191)
VOLTAGE_MAX__3V0A       = random.randint(0, 191)
VOLTAGE_MIN__3V0A       = random.randint(0, 191)
VOLTAGE_INS__3V0A_1     = random.randint(0, 191)
VOLTAGE_AVE__3V0A_1     = random.randint(0, 191)
VOLTAGE_MAX__3V0A_1     = random.randint(0, 191)
VOLTAGE_MIN__3V0A_1     = random.randint(0, 191)
VOLTAGE_INS_2V5D        = random.randint(0, 191)
VOLTAGE_AVE_2V5D        = random.randint(0, 191)
VOLTAGE_MAX_2V5D        = random.randint(0, 191)
VOLTAGE_MIN_2V5D        = random.randint(0, 191)
VOLTAGE_INS_2V5D_1      = random.randint(0, 191)
VOLTAGE_AVE_2V5D_1      = random.randint(0, 191)
VOLTAGE_MAX_2V5D_1      = random.randint(0, 191)		# Byte 46
VOLTAGE_MIN_2V5D_1      = random.randint(0, 191)
VOLTAGE_INS_2V5FA       = random.randint(0, 191)
VOLTAGE_AVE_2V5FA       = random.randint(0, 191)
VOLTAGE_MAX_2V5FA       = random.randint(0, 191)
VOLTAGE_MIN_2V5FA       = random.randint(0, 191)
VOLTAGE_INS_2V5FA_1     = random.randint(0, 191)
VOLTAGE_AVE_2V5FA_1     = random.randint(0, 191)
VOLTAGE_MAX_2V5FA_1     = random.randint(0, 191)
VOLTAGE_MIN_2V5FA_1     = random.randint(0, 191)                                            
VOLTAGE_INS_2V5RA       = random.randint(0, 191)
VOLTAGE_AVE_2V5RA       = random.randint(0, 191)
VOLTAGE_MAX_2V5RA       = random.randint(0, 191)
VOLTAGE_MIN_2V5RA       = random.randint(0, 191)
VOLTAGE_INS_2V5RA_1     = random.randint(0, 191)
VOLTAGE_AVE_2V5RA_1     = random.randint(0, 191)
VOLTAGE_MAX_2V5RA_1     = random.randint(0, 191)
VOLTAGE_MIN_2V5RA_1     = random.randint(0, 191)
VOLTAGE_INS_1V8D        = random.randint(0, 191)
VOLTAGE_AVE_1V8D        = random.randint(0, 191)
VOLTAGE_MAX_1V8D        = random.randint(0, 191)
VOLTAGE_MIN_1V8D        = random.randint(0, 191)
VOLTAGE_INS_1V8D_1      = random.randint(0, 191)
VOLTAGE_AVE_1V8D_1      = random.randint(0, 191)
VOLTAGE_MAX_1V8D_1      = random.randint(0, 191)
VOLTAGE_MIN_1V8D_1      = random.randint(0, 191)
VOLTAGE_INS_1V0SD       = random.randint(0, 191)
VOLTAGE_AVE_1V0SD       = random.randint(0, 191)
VOLTAGE_MAX_1V0SD       = random.randint(0, 191)
VOLTAGE_MIN_1V0SD       = random.randint(0, 191)
VOLTAGE_INS_1V0SD_1     = random.randint(0, 191)
VOLTAGE_AVE_1V0SD_1     = random.randint(0, 191)
VOLTAGE_MAX_1V0SD_1     = random.randint(0, 191)
VOLTAGE_MIN_1V0SD_1     = random.randint(0, 191)
VOLTAGE_INS_1V0VD       = random.randint(0, 191)
VOLTAGE_AVE_1V0VD       = random.randint(0, 191)
VOLTAGE_MAX_1V0VD       = random.randint(0, 191)
VOLTAGE_MIN_1V0VD       = random.randint(0, 191)
VOLTAGE_INS_1V0VD_1     = random.randint(0, 191)
VOLTAGE_AVE_1V0VD_1     = random.randint(0, 191)
VOLTAGE_MAX_1V0VD_1     = random.randint(0, 191)
VOLTAGE_MIN_1V0VD_1     = random.randint(0, 191)                                            
CURRENT_INS_BATT        = random.randint(0, 191)
CURRENT_AVE_BATT        = random.randint(0, 191)
CURRENT_MAX_BATT        = random.randint(0, 191)
CURRENT_MIN_BATT        = random.randint(0, 191)
CURRENT_INS_BATT_1      = random.randint(0, 191)
CURRENT_AVE_BATT_1      = random.randint(0, 191)
CURRENT_MAX_BATT_1      = random.randint(0, 191)
CURRENT_MIN_BATT_1      = random.randint(0, 191)
CURRENT_INS_15V0A       = random.randint(0, 191)
CURRENT_AVE_15V0A       = random.randint(0, 191)
CURRENT_MAX_15V0A       = random.randint(0, 191)
CURRENT_MIN_15V0A       = random.randint(0, 191)
CURRENT_INS_15V0A_1     = random.randint(0, 191)
CURRENT_AVE_15V0A_1     = random.randint(0, 191)
CURRENT_MAX_15V0A_1     = random.randint(0, 191)
CURRENT_MIN_15V0A_1     = random.randint(0, 191)
CURRENT_INS_N3V0A       = random.randint(0, 191)
CURRENT_AVE_N3V0A       = random.randint(0, 191)
CURRENT_MAX_N3V0A       = random.randint(0, 191)
CURRENT_MIN_N3V0A       = random.randint(0, 191)
CURRENT_INS_N3V0A_1     = random.randint(0, 191)
CURRENT_AVE_N3V0A_1     = random.randint(0, 191)
CURRENT_MAX_N3V0A_1     = random.randint(0, 191)
CURRENT_MIN_N3V0A_1     = random.randint(0, 191)
CURRENT_INS_3V3D        = random.randint(0, 191)
CURRENT_AVE_3V3D        = random.randint(0, 191)
CURRENT_MAX_3V3D        = random.randint(0, 191)
CURRENT_MIN_3V3D        = random.randint(0, 191)
CURRENT_INS_3V3D_1      = random.randint(0, 191)
CURRENT_AVE_3V3D_1      = random.randint(0, 191)
CURRENT_MAX_3V3D_1      = random.randint(0, 191)
CURRENT_MIN_3V3D_1      = random.randint(0, 191)
CURRENT_INS_3V0A        = random.randint(0, 191)
CURRENT_AVE_3V0A        = random.randint(0, 191)
CURRENT_MAX_3V0A        = random.randint(0, 191)
CURRENT_MIN_3V0A        = random.randint(0, 191)
CURRENT_INS_3V0A_1      = random.randint(0, 191)
CURRENT_AVE_3V0A_1      = random.randint(0, 191)
CURRENT_MAX_3V0A_1      = random.randint(0, 191)
CURRENT_MIN_3V0A_1      = random.randint(0, 191)                                            
CURRENT_INS_2V5D        = random.randint(0, 191)
CURRENT_AVE_2V5D        = random.randint(0, 191)
CURRENT_MAX_2V5D        = random.randint(0, 191)
CURRENT_MIN_2V5D        = random.randint(0, 191)
CURRENT_INS_2V5D_1      = random.randint(0, 191)
CURRENT_AVE_2V5D_1      = random.randint(0, 191)
CURRENT_MAX_2V5D_1      = random.randint(0, 191)
CURRENT_MIN_2V5D_1      = random.randint(0, 191)
CURRENT_INS_2V5FA       = random.randint(0, 191)
CURRENT_AVE_2V5FA       = random.randint(0, 191)
CURRENT_MAX_2V5FA       = random.randint(0, 191)
CURRENT_MIN_2V5FA       = random.randint(0, 191)
CURRENT_INS_2V5FA_1     = random.randint(0, 191)
CURRENT_AVE_2V5FA_1     = random.randint(0, 191)
CURRENT_MAX_2V5FA_1     = random.randint(0, 191)
CURRENT_MIN_2V5FA_1     = random.randint(0, 191)
CURRENT_INS_2V5RA       = random.randint(0, 191)
CURRENT_AVE_2V5RA       = random.randint(0, 191)
CURRENT_MAX_2V5RA       = random.randint(0, 191)
CURRENT_MIN_2V5RA       = random.randint(0, 191)
CURRENT_INS_2V5RA_1     = random.randint(0, 191)
CURRENT_AVE_2V5RA_1     = random.randint(0, 191)
CURRENT_MAX_2V5RA_1     = random.randint(0, 191)
CURRENT_MIN_2V5RA_1     = random.randint(0, 191)
CURRENT_INS_1V8D        = random.randint(0, 191)
CURRENT_AVE_1V8D        = random.randint(0, 191)
CURRENT_MAX_1V8D        = random.randint(0, 191)
CURRENT_MIN_1V8D        = random.randint(0, 191)
CURRENT_INS_1V8D_1      = random.randint(0, 191)
CURRENT_AVE_1V8D_1      = random.randint(0, 191)
CURRENT_MAX_1V8D_1      = random.randint(0, 191)
CURRENT_MIN_1V8D_1      = random.randint(0, 191)
CURRENT_INS_1V0SD       = random.randint(0, 191)
CURRENT_AVE_1V0SD       = random.randint(0, 191)
CURRENT_MAX_1V0SD       = random.randint(0, 191)
CURRENT_MIN_1V0SD       = random.randint(0, 191)
CURRENT_INS_1V0SD_1     = random.randint(0, 191)
CURRENT_AVE_1V0SD_1     = random.randint(0, 191)
CURRENT_MAX_1V0SD_1     = random.randint(0, 191)
CURRENT_MIN_1V0SD_1     = random.randint(0, 191)
CURRENT_INS_1V0VD       = random.randint(0, 191)
CURRENT_AVE_1V0VD       = random.randint(0, 191)
CURRENT_MAX_1V0VD       = random.randint(0, 191)
CURRENT_MIN_1V0VD       = random.randint(0, 191)
CURRENT_INS_1V0VD_1     = random.randint(0, 191)
CURRENT_AVE_1V0VD_1     = random.randint(0, 191)
CURRENT_MAX_1V0VD_1     = random.randint(0, 191)
CURRENT_MIN_1V0VD_1     = random.randint(0, 191)
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
#CRC                     = 0xAA



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
						  VOTER_CNTS_1, CRC, CRC_1, SYNC])
						  
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
							CURRENT_INS_3V3D_1, CURRENT_AVE_3V3D_1, CURRENT_MAX_3V3D_1, CURRENT_MIN_3V3D_1, 
							CURRENT_INS_3V0A, CURRENT_AVE_3V0A, CURRENT_MAX_3V0A, CURRENT_MIN_3V0A,
							CURRENT_INS_3V0A_1, CURRENT_AVE_3V0A_1, CURRENT_MAX_3V0A_1, CURRENT_MIN_3V0A_1, 
							CURRENT_INS_2V5D, CURRENT_AVE_2V5D, CURRENT_MAX_2V5D, CURRENT_MIN_2V5D, 
							CURRENT_INS_2V5D_1, CURRENT_AVE_2V5D_1, CURRENT_MAX_2V5D_1, CURRENT_MIN_2V5D_1, 
							CURRENT_INS_2V5FA, CURRENT_AVE_2V5FA, CURRENT_MAX_2V5FA, CURRENT_MIN_2V5FA, 
							CURRENT_INS_2V5FA_1, CURRENT_AVE_2V5FA_1, CURRENT_MAX_2V5FA_1, CURRENT_MIN_2V5FA_1, 
							CURRENT_INS_2V5RA, CURRENT_AVE_2V5RA, CURRENT_MAX_2V5RA, CURRENT_MIN_2V5RA, 
							CURRENT_INS_2V5RA_1, CURRENT_AVE_2V5RA_1, CURRENT_MAX_2V5RA_1, CURRENT_MIN_2V5RA_1, 
							CURRENT_INS_1V8D, CURRENT_AVE_1V8D, CURRENT_MAX_1V8D, CURRENT_MIN_1V8D, 
							CURRENT_INS_1V8D_1, CURRENT_AVE_1V8D_1, CURRENT_MAX_1V8D_1, CURRENT_MIN_1V8D_1, 
							CURRENT_INS_1V0SD, CURRENT_AVE_1V0SD, CURRENT_MAX_1V0SD, CURRENT_MIN_1V0SD, 
							CURRENT_INS_1V0SD_1, CURRENT_AVE_1V0SD_1, CURRENT_MAX_1V0SD_1, CURRENT_MIN_1V0SD_1, 
							CURRENT_INS_1V0VD, CURRENT_AVE_1V0VD, CURRENT_MAX_1V0VD, CURRENT_MIN_1V0VD, 
							CURRENT_INS_1V0VD_1, CURRENT_AVE_1V0VD_1, CURRENT_MAX_1V0VD_1, CURRENT_MIN_1V0VD_1, 
							V6_TEMPERATURE, PC1_TEMPERATURE, PC1_EXT_TEMPERATURE, PC2_TEMPERATURE, 
							PC2_EXT_TEMPERATURE, SYSTEM_RUNTIME_DAYS, SYSTEM_RUNTIME_DAYS_1, SYSTEM_RUNTIME_MS, 
							SYSTEM_RUNTIME_MS_1, SYSTEM_STATUS_FLAG, SYSTEM_STATUS_FLAG_1, CRC, CRC_1, SYNC])
							
TEST_PKT = bytearray("Hello World!", "utf8")

timeout = 60 # port timeout; None = wait forever

# Setup and open serial port
uart1 = serial.Serial(port = 'COM5', baudrate = 115200, timeout = timeout)

xPad = 3
yPad = 5

pktLen = "Pkt Length:   "

# Add things here

class Application(tk.Frame):

	syncWrapVar = None

	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.winfo_toplevel().title("UART Testing")
		self.create_widgets()
		
	def create_widgets(self):
		# Create necessary buttons
		self.send_tile = tk.Button(self)
		self.send_tile["text"] = "Send Tile"
		self.send_tile["command"] = self.sendTile
		self.send_tile.grid(column=0, columnspan=2, padx=xPad, pady=yPad, row=0)
		
		self.send_health = tk.Button(self)
		self.send_health["text"] = "Send Health"
		self.send_health["command"] = self.sendHealth
		self.send_health.grid(column=2, columnspan=2, padx=xPad, pady=yPad, row=0)
		
		self.hello_world = tk.Button(self)
		self.hello_world["text"] = "Hello World!"
		self.hello_world["command"] = self.sendHello
		self.hello_world.grid(column=4, columnspan=2, padx=xPad, pady=yPad, row=0)
		
		self.send_custom = tk.Button(self)
		self.send_custom["text"] = "Send Custom Pkt"
		self.send_custom["command"] = self.sendCustom
		self.send_custom.grid(column=3, columnspan=2, padx=xPad, pady=yPad, row=2, sticky="W")
				
		self.quit = tk.Button(self)
		self.quit["text"] = "Quit"
		self.quit["command"] = root.destroy
		self.quit.grid(column=2, padx=xPad, pady=yPad, row = 3, sticky="E")
		
		# Create label and text entry box
		self.custom_label = tk.Label(self)
		self.custom_label["text"] = "Custom Pkt: "
		self.custom_label.grid(column=0, columnspan=2, padx=xPad, pady=yPad, row=1, sticky="W")
		
		self.enter_pkt = tk.Entry(self)
		self.enter_pkt.grid(column=2, columnspan=2, padx=xPad, pady=yPad, row=1, sticky="W")
		
		# Create length label
		self.pkt_length = tk.Label(self)
		self.pkt_length["text"] = pktLen
		self.pkt_length.grid(column=0, columnspan=3, padx=xPad, pady=yPad, row=2, sticky="W")
				
		# Create check box
		self.syncWrap = tk.Checkbutton(self)
		self.syncWrap["text"] = "SyncWrap"
		self.syncWrap["offvalue"] = False
		self.syncWrap["onvalue"] = True
		
		self.syncWrapVar = tk.IntVar()
		self.syncWrap["variable"] = self.syncWrapVar
		self.syncWrap.grid(column=4, padx=xPad, pady=yPad, row=1)
		
		
	def sendTile(self):
		# Update packet length field
		self.pkt_length["text"] = pktLen + str(len(TLM_TILE_PKT))
		
		tile_out = ''
		for i in range(0, len(TLM_TILE_PKT)):
			tile_out += str(TLM_TILE_PKT[i]) + ' '
			
		print("TILE_PKT: " + tile_out)
		
		# Send tile packet over uart1
		uart1.write(TLM_TILE_PKT)
	
	def sendHealth(self):
		# Update packet length field
		self.pkt_length["text"] = pktLen + str(len(TLM_HEALTH_PKT))
		
		output = ''
		for i in range(len(TLM_HEALTH_PKT)):
			output += str(TLM_HEALTH_PKT[i]) + ' '
	
		print("HEALTH_PKT: " + output)
		# Send health packet over uart1
		uart1.write(TLM_HEALTH_PKT)
		return
	
	def sendHello(self):
		# Update packet length field
		self.pkt_length["text"] = pktLen + str(len(TEST_PKT))
		# Send test packet over uart1
		uart1.write(TEST_PKT)
		return
	
	def sendCustom(self):
		entry = self.enter_pkt.get()
		temp = ""
		#print(str(self.syncWrapVar.get()))		
		CUST_PKT = bytearray()
		
		if(self.syncWrapVar.get() == 1):
			temp = str(SYNC) + entry + str(SYNC)
			CUST_PKT.append(SYNC)
		else:
			temp = entry
		#print(temp)
		# Clear entry field
		#self.enter_pkt.delete(0, len(self.enter_pkt.get()))		
		
		# Convert entry text into bytearray for sending
		
		i = 0
		for i in range(0, len(entry)):
			CUST_PKT.append(ord(entry[i]))
			#print(str(ord(entry[i])))
		
		if(self.syncWrapVar.get() == 1):
			CUST_PKT.append(SYNC)
		self.pkt_length["text"] = pktLen + str(len(CUST_PKT))
		
		# Send custom packet over uart1
		uart1.write(CUST_PKT)
		
		
		
root = tk.Tk()
app = Application(master=root)
app.mainloop()