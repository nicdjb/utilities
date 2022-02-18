#!/usr/bin/python3

# join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

with open('/Users/nicbox/Projects/ctf/picoctf/enc', 'r') as myfile:
   flag = myfile.read()

   for i in range(len(flag)):
       print(chr(ord(flag[i]) >> 8), end ="")
       print(chr(ord(flag[i]) - ((ord(flag[i]) >> 8) <<8 )), end ="")

