import sys
sys.path.append('..')
import dataoper
import randtext
import re
import hashlib


helpstr='''
    This is a program which can product random password.
    Please input 'a,b(,c)(,d)'
    a means website.
    b means username.
    c means format.
    d means length.
'''


def has_dev(str):
    hashh = hashlib.md5()
    hashh.update(bytes(str,encoding='utf-8'))
    return hashh.hexdigest()


def form_dev(str,fo):
    ans = ""
    cha = ""
    must = ""
    char = ""
    if fo[0]>'0' and fo[0] <= '9':
        if fo == '1':
            for i in range(10):
                cha += chr(ord('0')+i)
        elif fo == '2':
            for i in range(10):
                cha += chr(ord('0')+i)
            for i in range(26):
                cha += chr(ord('a')+i)
            must = "a0"
        elif fo == '3':
            for i in range(10):
                cha += chr(ord('0')+i)
            for i in range(26):
                cha += chr(ord('a')+i)
            must = "a0.A"
            char = "!@#$%^&*(),.[]"
            cha += char
        else:
            for i in range(10):
                cha += chr(ord('0')+i)
            for i in range(26):
                cha += chr(ord('a')+i)
    else:
        for i in range(len(fo)):
            if fo[i] == '0':
                for j in range(10):
                    cha += chr(ord('0')+j)
            elif fo[i] == 'a':
                for j in range(26):
                    cha += chr(ord('a')+j)
            elif fo[i] == 'A':
                for j in range(26):
                    cha += chr(ord('A')+j)
            else:
                cha += fo[i]
                char += fo[i]
    str = int(str,16)
    for i in range(len(must)):
        if must[i] == '0':
            ans += chr(ord('0')+(str%256)%10)
        elif must[i] == 'a':
            ans += chr(ord('a')+(str%256)%10)
        elif must[i] == 'A':
            ans += chr(ord('A')+(str%256)%10)
        else:
            ans+= char[(str%256)%len(char)]
        str //= 256
    while str > 0:
        ans += cha[(str%256)%len(cha)]
        str //= 256
    return ans


def pan(str):
    if len(str) == 1:
        if str[0]>='0' and str[0]<='9':
            return True
        else :
            return False
    else:
        se = set()
        for i in range(len(str)):
            if str[i] in se:
                return False
            if((str[i]>'0' and str[i]<='9') or (str[i]>'A' and str[i]<='Z') or
                (str[i]>'a' and str[i]<='z')):
                return False
            se.add(str[i])
        return True


def solve(chaid,str='help'):
    if str=="help":
        return helpstr
    res=dataoper.find_table(chaid)
    if res=="None":
        dataoper.insert_table(chaid,randtext.get_randtext())
        res=res=dataoper.find_table(chaid)
    lis = re.split(r',',str)
    if len(lis) < 2:
        return "invalid input!"
    has = has_dev(lis[0]+lis[1]+res)
    if len(lis) < 3:
        lis.append('2')
    if len(lis) < 4:
        lis.append(12)
    try:
        lis[3] = int(lis[3])
    except:
        return "invalid input!"
    if pan(lis[2]) == False:
        return "invalid input!"
    return form_dev(has,lis[2])[:lis[3]]


if __name__ == "__main__":
    a = solve('a','a,bdddd,3')
    print(a)
