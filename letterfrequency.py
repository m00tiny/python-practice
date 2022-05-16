#!/usr/bin/env python
string = input()
letter = input()
print(int((string.count(letter)/len(string) * 100) // 1))
