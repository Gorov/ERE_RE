
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
        sys.stdout.write(array[2] + ' ')

sys.stdout.write('\n')



