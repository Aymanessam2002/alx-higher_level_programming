#!/usr/bin/python3
import sys
if __name__ == '__main__':
    calcul = 0
    for num in range(1, len(sys.argv)):
        calcul += int(sys.argv[num])
    print('{}'.format(calcul))
