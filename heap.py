import random
import timeit
from collections import OrderedDict
import matplotlib.pyplot as plt
import heapq


insDict = OrderedDict()
getMinDict = OrderedDict()
deleteMinDict = OrderedDict()


#insertion

size = [10, 50, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000]

for x in size:
    total = 0
    for rep in range(10):
        heap = []
        randoms = random.sample(range(x), x)
        time1 = 0
        for i in range(len(randoms)):
            t1 = timeit.timeit('heapq.heappush(heap,randoms[i])',  number=1, globals=globals())
            time1 += t1
        total += time1
    xAxis1 = x
    insDict[xAxis1] = total/10



####

size = [10, 100, 1000, 10000, 10000]

for x in size:
    randoms = random.sample(range(x), x)
    heapq.heapify(randoms)
    heap = randoms

#get min element
    tot_time2 = 0

    for i in range(100):
        t2 = timeit.timeit('heap[0]', number=1, globals=globals())
        tot_time2 += t2

    xAxis2 = x
    getMinDict[xAxis2] = tot_time2/100


#delete max element
    tot_time3 = 0
    min = heap[0]

    for i in range(100):
        t3 = timeit.timeit('heapq.heappop(heap)', number=1, globals=globals())
        tot_time3 += t3
        heapq.heappush(heap, min)

    xAxis3 = x
    deleteMinDict[xAxis3] = tot_time3/100


plt.figure(1)

plt.plot(list(insDict.keys()), list(insDict.values()), label='insertion')
plt.scatter(list(insDict.keys()), list(insDict.values()))
plt.title('construction of a min heap of size x')
plt.legend(bbox_to_anchor=(1,0.2))
plt.grid(True)
plt.ylabel('time')
plt.xlabel('size')

plt.figure(2)
plt.subplot(221)
plt.plot(list(getMinDict.keys()), list(getMinDict.values()), color='r')
plt.scatter(list(getMinDict.keys()), list(getMinDict.values()), color='r')
plt.title('get minimum execution time', color='r')
plt.grid(True)
plt.ylabel('time')
plt.xlabel('size')


plt.subplot(222)
plt.plot(list(deleteMinDict.keys()), list(deleteMinDict.values()), color='b')
plt.scatter(list(deleteMinDict.keys()), list(deleteMinDict.values()), color='b')
plt.title('delete minimum execution time', color='b')
plt.grid(True)
plt.ylabel('time')
plt.xlabel('size')


plt.subplot(223)
plt.plot(list(getMinDict.keys()), list(getMinDict.values()), color='r', label= 'get minimum')
plt.scatter(list(getMinDict.keys()), list(getMinDict.values()), color='r')
plt.plot(list(deleteMinDict.keys()), list(deleteMinDict.values()), color='b', label='delete minimum')
plt.scatter(list(deleteMinDict.keys()), list(deleteMinDict.values()), color='b')
plt.grid(True)
plt.ylabel('time')
plt.xlabel('size')
plt.title('comparison')


plt.show()
