
import sys

score_dict = {}

while True:
    line = sys.stdin.readline()
    if not line:
        break
    if line.startswith('Iter '):
        array = line.strip().split(' ')
        iter_id = array[1]
        for i in range(15):
            line = sys.stdin.readline()
        line = sys.stdin.readline()
        #print line
        array = line.strip().split('\t')
        if(len(array) != 3):
            break
        score_dict[iter_id] = float(array[2])

sort_scores = sorted(score_dict.items(), key=lambda x:x[1], reverse=True)

for k,v in sort_scores:
    print k + '\t' + str(v)



