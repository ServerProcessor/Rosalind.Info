from bbio import *
ss = "ILFNNSDGIGYQWPAMSLQTWEEKKNTCWWAICRSD"

w = 0

for i in ss:
    if i == 'A':
        w = w + 71.03711
    if i == 'C':
        w = w + 103.00919
    if i == 'D':
        w = w + 115.02694
    if i == 'E':
        w = w + 129.04259
    if i == 'F':
        w = w + 147.06841
    if i == 'G':
        w = w + 57.02146
    if i == 'H':
        w = w + 137.05891
    if i == 'I':
        w = w + 113.08406
    if i == 'K':
        w = w + 128.09496
    if i == 'L':
        w = w + 113.08406
    if i == 'M':
        w = w + 131.04049
    if i == 'N':
        w = w + 114.04293
    if i == 'P':
        w = w + 97.05276
    if i == 'Q':
        w = w + 128.05858
    if i == 'R':
        w = w + 156.10111
    if i == 'S':
        w = w + 87.03203
    if i == 'T':
        w = w + 101.04768
    if i == 'V':
        w = w + 99.06841
    if i == 'W':
        w = w + 186.07931
    if i == 'Y':
        w = w + 163.06333
        
print w
