#!/usr/bin/env python3
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        scores = sum(scores)
        scores = scores // n
        student_marks[name] = scores
    query_name = input()
    print (query_name
    var = {name}
    )