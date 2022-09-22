#!/usr/bin/env python3

import time
flag = "gopher{it's_about_time}"

def check(s):
    if len(s) != len(flag):
        print("wrong length", flush=True)
        return

    for c in range(min(len(s), len(flag))):
        if c < 3 and flag[c] == s[c]:
            time.sleep(1)
        if flag[c] == s[c]:
            time.sleep(0.3)
        else:
            print("wrong flag", flush=True)
            return

    print("correct", flush=True)
    return

print("enter the flag: ", end="", flush=True)
a = input()
check(a)

import sys
sys.exit(0)
