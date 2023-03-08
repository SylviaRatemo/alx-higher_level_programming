#!/usr/bin/python3i
index = 0
for character in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(character - index)), end="")
    index = 32 if index == 0 else 0
