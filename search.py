#!/usr/bin/python
import fileinput
query = ' '.join(fileinput.input()).lower() # can take a commandline argument or a piped text stream
print "Searching for '",query,"'"
with open('equation-database.txt','r') as f:
    for line in f:
        if '%%' in line:
             pass # Go to the next line
        if query in line.lower():
             print line,
             while '%%' not in line:
                 try:
                     line = f.next()
                     print line,
                 except StopIteration:
                     break # If we hit the end of the file, exit the loop.
