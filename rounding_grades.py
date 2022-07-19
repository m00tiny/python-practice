#!/usr/bin/env python3
# grading students
# hackerrank solution

def gradingStudents(grades):
    for i in range(len(grades)):       
        if grades[i] < 38:
            continue
        else:
            var = grades[i]
            val = var % 5
            if val == 3:
                var = var + 2
                grades[i] = var
            elif val == 4:
                var = var + 1
                grades[i] = var
            else:
                continue
    return grades

    
# some bullshit offline testing
dumb_kids = int(7)
bad_grades = [28, 39, 42, 57, 71, 88, 64]
print("Before: ", end='')
print(bad_grades)
print("After: ", end='')
print(gradingStudents(bad_grades))

