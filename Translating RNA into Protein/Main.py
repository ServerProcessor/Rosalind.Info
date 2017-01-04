from bbio import *
ss = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA" # Sample

g = len(ss)
p = g / 3
c1 = 0
c2 = 3

w = []

for i in range(p):
  gr = ss[c1:c2]
  if (gr == 'UUU') | (gr == 'UUC'):
    w.append('F')
  if (gr == 'UUA') | (gr == 'UUG'):
    w.append('L')
  if (gr == 'UCU') | (gr == 'UCC'):
    w.append('S')
  if (gr == 'UCA') | (gr == 'UCG'):
    w.append('S')
  if (gr == 'UAU') | (gr == 'UAC'):
    w.append('Y')
  if (gr == 'UGU') | (gr == 'UGC'):
    w.append('C')
  if (gr == 'UGG'):
    w.append('W')
  if (gr == 'CUU') | (gr == 'CUC'):
    w.append('L')
  if (gr == 'CUA') | (gr == 'CUG'):
    w.append('L')
  if (gr == 'CCC') | (gr == 'CCU'):
    w.append('P')
  if (gr == 'CCA') | (gr == 'CCG'):
    w.append('P')
  if (gr == 'CAU') | (gr == 'CAC'):
    w.append('H')
  if (gr == 'CAA') | (gr == 'CAG'):
    w.append('Q')
  if (gr == 'CGU') | (gr == 'CGC'):
    w.append('R')
  if (gr == 'CGA') | (gr == 'CGG'):
    w.append('R')
  if (gr == 'AUU') | (gr == 'AUC'):
    w.append('I')
  if (gr == 'AUA'):
    w.append('I')    
  if (gr == 'AUG'):
    w.append('M')
  if (gr == 'ACU') | (gr == 'ACC'):
    w.append('T')
  if (gr == 'ACA') | (gr == 'ACG'):
    w.append('T')
  if (gr == 'AAC') | (gr == 'AAU'):
    w.append('N')
  if (gr == 'AAG') | (gr == 'AAA'):
    w.append('K')
  if (gr == 'AGU') | (gr == 'AGC'):
    w.append('S')
  if (gr == 'AGA') | (gr == 'AGG'):
    w.append('R')
  if (gr == 'GUU') | (gr == 'GUC'):
    w.append('V')
  if (gr == 'GUA') | (gr == 'GUG'):
    w.append('V')
  if (gr == 'GCU') | (gr == 'GCC'):
    w.append('A')
  if (gr == 'GCA') | (gr == 'GCG'):
    w.append('A')
  if (gr == 'GAU') | (gr == 'GAC'):
    w.append('D')
  if (gr == 'GAA') | (gr == 'GAG'):
    w.append('E')
  if (gr == 'GGU') | (gr == 'GGC'):
    w.append('G')
  if (gr == 'GGA') | (gr == 'GGG'):
    w.append('G')  
  c1 = c2
  c2 = c2 + 3
  
print "".join(w)
