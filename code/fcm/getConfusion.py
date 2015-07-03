import sys

filein1 = open(sys.argv[1], 'r')
filein2 = open(sys.argv[2], 'r')

lines1 = filein1.readlines()
lines2 = filein2.readlines()

filein1.close()
filein2.close()

matrix = [[0, 0], [0, 0]]
for i, line1 in enumerate(lines1):
    line2 = lines2[i]
    array1 = line1.strip().split('\t')
    array2 = line2.strip().split('\t')
    if array1[2] != array2[2]:
        print line1 + line2
        sys.exit(-1)
    goldrel = array1[2]
    pred1 = array1[1]
    pred2 = array2[1]
    if goldrel == 'NA':
        continue
    if pred1 == goldrel and pred2 == goldrel:
        matrix[0][0] += 1
    elif pred1 == goldrel and pred2 != goldrel:
        matrix[0][1] += 1
    elif pred1 != goldrel and pred2 == goldrel:
        matrix[1][0] += 1
    else:
        matrix[1][1] += 1

print matrix
