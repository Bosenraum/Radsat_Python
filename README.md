# RadSat Python Testing Files
### By Austin Rosenbaum

This repository contains a few python scripts for testing MFIB to RTC communications.

## Useful Files
[uart_logging](./uart_logging.py) --
This script reads data from a serial line (usually over the appropriate FTDI cable) and then writes the data it receives to a text file. The script alternates between waiting for a TILE packet and a HEALTH packet, but could be modified to listen for anything. I wanted each individual packet to be on its own line of the text file, so when 0x0A is read, it writes a newline, but I set up most of the debugging UART statements from the MFIB to replace newline characters with something like 0xAA. Then, when each packet is done sending, it explicitly writes a newline character so the next packet will be on its own line.

This file also includes a small threaded section (commented out as of 5/3/18) that allows the user to write message back over the UART while the program continues listening for packets normally.

[uart_test_dynamic2](./uart_test_dynamic2.py) --
This script is meant to emulate the packet sending behavior of the RTC. It communicates over UART and should be used with the RS422 FTDI cable connected to UART1 on the MFIB board.

#### Packet Data
The different components of the two primary RTC packets are enumerated at the beginning of this file. Some of the packet fields are 16 or 32 bits, but when creating the bytearray in python, 8 bits must be used at a time (I'm sure there is a better way to do this, perhaps an actual Enum and a loop while appending to the bytearray? I leave it as an exercise to the reader). The sync byte and packet type variables have specific and correct values, but the rest of the data is made up and can be changed as necessary. Following the enumerated packets parts, the two packets are created using bytearrays. The structure of the packets is defined in [this document](./RadSat_RTC_Payload_Packet_Structure.docx). These packets are completed by the CRC and ending SYNC byte discussed in the next section.

#### CRC Data
Starting around line 314, the CRC functionality of the RTC communication was attempted to be mimicked. The majority of this did not work at least through Python and may need to be done from the RTC itself. About line 352, the CRC values are overridden and the 16-bit CRC used becomes 0xCCCC. This is the same value that the MFIB looks for when it receives a packet. Normally this would be replaced by an actual CRC calculation, but this was not accomplished before the launch of RadSat-g. The CRC data is appended onto both packets and each is followed by the end SYNC byte.

#### Setup and Connection
After the packets are created, they are printed out along with their lengths. Before communication begins, the UART serial connection must be established. Currently, the port used is dependent upon the host machine being used to run the script and this must be changed as necessary to use the correct COM port. The baudrate of the MFIB's UART is 115200 so this should be set as the baudrate for serial communication. I've set the timeout variable to be None meaning the connection will never timeout and will constantly try and receive data. This may make the program unresponsive if no data is expected to be received and the terminal may need to be closed (this should probably be handled more gracefully, but having a long timeout you can get practically the same result).

#### Command Loop
The script enters an infinite loop where it blocks and waits for a single byte command from the MFIB. This command is then deciphered and the correct packet is sent in response. If the script receives an unknown command, it will alert the user and print the command it did receive for debugging. The else condition can also be used to exit the loop when a bad command is received, however this is not the behavior of the RTC and would generally be undesirable.

## Files to Ignore
[gui_test.py](./gui_test.py) -- An early version of the dynamic response, allows the user to send packets at will from a simple GUI. Not fully featured and didn't really work all that well. Could be made to use the packets created in uart_test_dynamic2.py to keep everything in sync, but would only be useful for testing UART functionality which should already work.

[scanlog](./scanlog.py) -- Script for parsing pktlog.txt and giving a more user-friendly output. Never fully finished and Skylar's GUI for the final flight is much better. Could use the same idea as that file and adapt it to this specific file.

[uart_test](./uart_test.py) -- First attempt script at communicating to MFIB. Does not respond to commands, instead sends a single packet of each type after receiving any single byte. Packet structures are not up to date.

[uart_test_dynamic](./uart_test_dynamic.py) -- First dynamic response to commands. Packet structures not current and no CRC considerations. The file uart_test_dynamic2.py was created off of this and is more current.

[write_test](./write_test.py) -- A simple serial write to verify things are working.
