def quicksort(list):
    less=[]
    equal=[]
    greater=[]
    if len(list)>1:
        pivot=list[0]
        for x in list:
            if x<pivot:
                less.append(x)
            if x==pivot:
                equal.append(x)
            if x>pivot:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)
    else:
        return list
