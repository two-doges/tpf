import sqlite3 as sq
import os
import sys
sys.path.append("..")
import randtext
import devdata


def make_table(pat=""):
    con = sq.connect(pat)
    cu = con.cursor()
    cu.execute("create table tpf_data(idd varchar(20) UNIQUE,key varchar(52))")
    con.commit()
    con.close()
    print("make table success")


def delete_table(pat=devdata.dir,tab="tpf_data"):
    con = sq.connect(pat)
    cu = con.cursor()
    cu.execute("drop table %s" % tab)
    con.commit()
    con.close()
    print("delete table success")


def insert_table(idd,key):
    if len(idd) > 20 or len(key) !=50:
        return "insert fail!"
    con = sq.connect(devdata.dir)
    cu = con.cursor()
    cu.execute("select * from tpf_data where idd = '%s'" % idd)
    if cu.fetchall() != []:
        print("insert repeat element!")
        return "insert fail!"
    cu.execute("insert into tpf_data values('%s','%s')" % (idd,key) )
    con.commit()
    con.close()
    return "insert success"


def find_table(idd):
    con = sq.connect(devdata.dir)
    cu = con.cursor()
    cu.execute("select * from tpf_data where idd = '%s'" % idd)
    # print(str(cu.fetchall())+' '+idd)
    res = cu.fetchall()
    if res == []:
        return "None"
    else :
        return res[0][1]


def display_table():
    con = sq.connect(devdata.dir)
    cu = con.cursor()
    cu.execute("select * from tpf_data")
    print(cu.fetchall())


if __name__ == "__main__":
    insert_table("a",randtext.get_randtext())
    display_table()
