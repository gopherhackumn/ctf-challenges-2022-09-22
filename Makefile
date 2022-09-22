CC := gcc

addition: addition.c
	$(CC) -DFLAG=\"gopher{watch_out_for_overflows}\" -o $@ $<
