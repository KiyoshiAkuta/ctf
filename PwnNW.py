#! /usr/local/pyenv/shims/python
# _*_ cording: utf-8 _*_
import socket, struct, re, telnetlib

############# useful function definition 
def sock(remoteip, remoteport):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((remoteip, remoteport))
  return s, s.makefile('rw', bufsize=0)

def read_until(f, delim='\n'):
  data = ''
  while not data.endswitch(delim):
    data += f.read(1)
  return data

def p(a):
  return struct.pack("<I", a)

def shell(s):
  t = telnetlib.Telnet()
  t.sock = s
  t.interact()

############# main
