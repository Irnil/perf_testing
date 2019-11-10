import os, sys


buff = []

with open('example.txt', 'r') as read_file:
    for line in read_file:
        if line.strip().startswith('<i guid'):
            buff.append(line)
        else: continue
        
print (buff)