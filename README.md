# RadSat Python Testing Files
### By Austin Rosenbaum

This repository contains a few python scripts for testing MFIB to RTC communications.

## Useful Files
[uart_logging.py](./uart_logging.py)
This script reads data from a serial line (usually over the appropriate FTDI cable) and then writes the data it receives to a text file. The script alternates between waiting for a TILE packet and a HEALTH packet, but could be modified to listen for anything. I wanted each individual packet to be on its own line of the text file, so when 0x0A is read, it writes a newline, but I set up most of the debugging UART statements from the MFIB to replace newline characters with something like 0xAA. Then, when each packet is done sending, it explicitly writes a newline character so the next packet will be on its own line.

This file also includes a small threaded section (commented out as of 5/3/18) that allows the user to write message back over the UART while the program continues listening for packets normally.

[uart_test_dynamic2.py](./uart_test_dynamic2.py)
This script is meant to emulate the packet sending behavior of the RTC. It communicates over UART and should be used with the RS422 FTDI cable connected to UART1 on the MFIB board.

#### Packet Data
The different components of the two primary RTC packets are enumerated at the beginning of this file. Some of the packet fields are 16 or 32 bits, but when creating the bytearray in python, 8 bits must be used at a time (I'm sure there is a better way to do this, perhaps an actual Enum and a loop while appending to the bytearray? I leave it as an exercise to the reader). The sync byte and packet type variables have specific and correct values, but the rest of the data is made up and can be changed as necessary. Following the enumerated packets parts, the two packets are created using bytearrays. The structure of the packets is defined in [this](./RadSat_RTC_Payload_Packet_Structure.docx) document.

## Files to Ignore
