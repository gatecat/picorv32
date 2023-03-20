import os

# obtain and parse ID
unique_id = int(os.environ["UNIQUE_ID"], 16)

lut_count = 0
for cell_name, cell in ctx.cells:
	if "unique_id_idx" in cell.attrs:
		index = int(cell.attrs["unique_id_idx"], 2)
		print(f"lut {index}: {cell_name}")
		# each LUT provides one bit per 32-bit word out of 128 bits total
		new_init = 0
		for i in range(4):
			if (unique_id >> (32 * i + index)) & 0x1:
				new_init |= (1 << i)
		# the LUT function is repeated 4 times, as the top two bits are don't cares
		new_init = new_init & 0xF
		new_init = (new_init << 12) | (new_init << 8) | (new_init << 4) | new_init 
		cell.setParam("LUT_INIT", f"{new_init:016b}")
		lut_count += 1
assert lut_count == 32, lut_count
write_bitstream(ctx, "icebreaker_patched.asc")
