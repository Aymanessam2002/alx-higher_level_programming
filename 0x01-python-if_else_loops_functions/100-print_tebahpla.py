#!/usr/bin/python3
print("".join('{}{}'.format(chr((char + 1) + 32), chr(char))
              for char in range(65, 91, 2)[::-1]), end='')
