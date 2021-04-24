"""
    This script convert vasp file to a file that contain
    desired informations
"""

import sys

_, filename = sys.argv

with open(filename, 'r+') as f :
    fin = f.readlines()
    
results = filename[:-5] + "m.txt"
fresults = filename[:-5] + "final.txt"

fout = open(results, 'w')
fr = open(fresults, 'w')

file = fin[8:]
for i in range(len(file)):
    file[i] = file[i].strip('- ')
    
for j in range(len(file)):
    a = float(file[j][:12])
    b = float(file[j][21:32])
    c = float(file[j][39:])
    s = f"{a:.16f}  {b:.16f}  {c:.16f} \n"
    fout.write(s)   
    
fout.close()
with open(results, 'r+') as f2 :
    mfile = f2.readlines()
    
for i in range(len(mfile)):
    mfile[i] = mfile[i].strip()
    
lfr = []
lfr += 'H'
lfr += mfile[96:102]
lfr += 'C'
lfr += mfile[45: 52]
lfr += 'O'
lfr += mfile[157:158]
lfr += mfile[193:]
lfr

lfr=map(lambda x:x+'\n', lfr)
fr.writelines(lfr)
fr.close()