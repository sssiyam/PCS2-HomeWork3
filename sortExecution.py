import random
from timeit import Timer
from collections import OrderedDict
import matplotlib.pyplot as plt

L = [10,100,1000,10000]
dquick= OrderedDict()
dbubble= OrderedDict()

for x in L:
    randoms = random.sample(range(x),x)

    s1 = 'bubbleSort(' + str(randoms) + ')'
    t1 = Timer(s1, 'from sorting import bubbleSort')
    time1 = t1.timeit(10)/10
    dquick[x] = time1

    s2 = 'quickSort(' + str(randoms) + ')'
    t2 = Timer(s2, 'from sorting import quickSort')
    time2 = t2.timeit(10)/10
    dbubble[x] = time2


plt.plot(dquick.keys(),dquick.values(), label = 'quick sort')
plt.plot(dbubble.keys(),dbubble.values(), label = 'bubble sort')
plt.xlabel('length of the list')
plt.ylabel('time')
plt.title('Sorting execution time')
plt.legend(bbox_to_anchor=(1,0.2))
plt.show()
