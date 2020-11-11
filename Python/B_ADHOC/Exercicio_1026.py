# -*- coding: utf-8 -*-
while True:
    try:
    	line = input().split(" ")
    	print(int(line[0]) ^ int(line[1]))
    except EOFError:
        break    