import os
import sys
sys.path.append("..")
import dataoper
def initall():
    pat = "devhost"
    fp = open("devdata.py","w+")
    s = str(os.getcwd())
    fp.write('dir = '+'"'+s+'/'+pat+'"'+'\n')
    fp.write('pos = '+'"'+s+'/'+"devdata"+'"')
    dataoper.make_table(pat)


if __name__ == "__main__":
    dataoper.delete_table()
    initall()
