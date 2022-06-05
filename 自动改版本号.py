import time
import re
import os
import sys
import py7zr


def genTimeVersion():
    #十位
    #millis = int(time.time())
    #十三位
    millis = int(round(time.time() * 1000))
    return millis


if __name__ == '__main__':
    # currentPath  = os.path.dirname(sys.argv[0])
    currentPath  = os.getcwd()
    print(currentPath)
        
    # print(len(id))