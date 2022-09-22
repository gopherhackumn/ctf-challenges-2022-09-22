#!/usr/bin/env python3

import time
flag = "gopher{it's_about_time}"

def check(s):
    if len(s) != len(flag):
        print("wrong", flush=True)
        return

    time.sleep(0.5)

    for c in range(min(len(s), len(flag))):
        if flag[c] == s[c]:
            time.sleep(0.5)
        else:
            print("wrong", flush=True)
            return

    print("correct", flush=True)
    return

print("enter the flag: ", end="", flush=True)
a = input()
check(a)

import sys
sys.exit(0)
