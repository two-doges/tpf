import os
import sys
sys.path.append("..")
import dataoper
def initall():
    pat="devhost"
    fp = open("devdata.py","w+")
    fp.write('dir = '+'"'+pat+'"')
    dataoper.make_table(pat)


if __name__ == "__main__":
    dataoper.delete_table()
    initall()
