#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Simple template for Google CodeJam to enable reading
# the input files that are provided.

if __name__ == "__main__":
    testSetSize = int(input())

    for caseNr in range(1, testSetSize+1):
        test = input()
        print("Case #{}: {}".format(caseNr, test))
