
import sys

score_dict = {}

filein = open(sys.argv[1], 'r')

while True:
    line = filein.readline()
    if not line:
        break
    if line.startswith('Iter '):
        array = line.strip().split(' ')
        iter_id = array[1]
        for i in range(15):
            line = filein.readline()
        line = filein.readline()
        #print line
        array = line.strip().split('\t')
        if(len(array) != 3):
            break
        score_dict[iter_id] = float(array[2])

sort_scores = sorted(score_dict.items(), key=lambda x:x[1], reverse=True)

#for k,v in sort_scores:
#    print k + '\t' + str(v)

filein.close()

print sort_scores[0][0]
print sort_scores[0][1]

filein = open(sys.argv[2], 'r')
while True:
    line = filein.readline()
    if not line:
        break
    if line.startswith('Iter '):
        array = line.strip().split(' ')
        iter_id = array[1]
        if iter_id != sort_scores[0][0]:
            continue
        for i in range(15):
            line = filein.readline()
        line = filein.readline()
        array = line.strip().split('\t')
        print 'Test F1 at Iter ' + iter_id + ' ' + array[2]
        break

filein.close()
