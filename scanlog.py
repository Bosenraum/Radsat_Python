from tkinter import ttk
import tkinter as tk

log = open("pktlog.txt")

width = 12

class Application(tk.Frame):
	tileRows = 27

	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.winfo_toplevel().title("Packet Decoder")
		self.create_widgets()

	def create_widgets(self):
		self.n = ttk.Notebook(self)
		self.tile_frame = ttk.Frame(self.n)
		self.health_frame = ttk.Frame(self.n)
		self.n.add(self.tile_frame, text="TILE")
		self.n.add(self.health_frame, text="HEALTH")
		self.n.pack()

		# TILE labels
		p1 = self.tile_frame
		self.pkt_type = tk.Label(p1, text="PACKET TYPE:", width=width)
		self.pkt_type.grid(column=0, row=0)

		self.s6_count = tk.Label(p1, text="S6 COUNT:", width=width)
		self.s6_count.grid(column=0, row=2)

		self.act_tiles = tk.Label(p1, text="ACT TILES:", width=width)
		self.act_tiles.grid(column=0, row=4)

		self.pkt_type_data = tk.Label(p1, text="TILE PACKET", width=width)
		self.pkt_type_data.grid(column=3, row=0)

		self.s6_count_data = tk.Label(p1, text="0x1234ABCD", width=width)
		self.s6_count_data.grid(column=3, row=2)

		self.act_tiles_data = tk.Label(p1, text="0x0003", width=width)
		self.act_tiles_data.grid(column=3, row=4)

		self.h1 = ttk.Separator(p1, orient="horizontal")
		self.h1.grid(column=0, columnspan=100, row=1, sticky="ew")

		self.h2 = ttk.Separator(p1, orient="horizontal")
		self.h2.grid(column=0, columnspan=100, row=3, sticky="ew")

		self.h3 = ttk.Separator(p1, orient="horizontal")
		self.h3.grid(column=0, columnspan=100, row=5, sticky="ew")

		self.v1 = ttk.Separator(p1, orient="vertical")
		self.v1.grid(column=1, row=0, rowspan=100, sticky="ns")

		self.pkt_type2 = tk.Label(self.health_frame, text="PACKET TYPE:", width=width)
		self.pkt_type2.pack()


# Split file into individual lines
# do something for each line
for line in log:
	# convert each character to a hex value
	vals = line.split(" ")
	#print(len(vals))
	if int(vals[0], 16) != 0xC0:
		print("NO SYNC BYTE FOUND!")
		quit()

	# next 50 bytes are tile packet



root = tk.Tk()
app = Application(master=root)
app.mainloop()

log.close()
