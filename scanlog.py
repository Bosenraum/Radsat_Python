
log = open("pktlog.txt")
newline = 0x0A

# Split file into individual lines
# do something for each line
for line in log:
    # convert each character to a hex value
    output = ''
    for char in line:

        output += format(ord(char), '02X') + ' '
    print(output)
