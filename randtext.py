import random
import sys
sys.path.append("..")
def get_randtext(len=50):
    ans = ""
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    for i in range(len):
        e = random.randint(0,61)
        ans += chars[e]
    return ans

if __name__=="__main__":
    print(get_randtext())
