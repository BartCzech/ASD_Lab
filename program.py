import time
import random

list = []
small_list = [] # special small list for insertion, my PC too slow
for i in range(200000):
    list.append(random.randint(0, 100000))

for i in range(5000):
    small_list.append(random.randint(0, 5000))

#print(list)

#insertion sort
def insertionsort(array):
    
    for i in range(1, len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0:
            temporal = array[j - 1]
            array[j - 1] = array[j]
            array[j] = temporal
            j -= 1
    return array

#merge sort
def mergesort(array):
    if len(array) == 1:
        return array

    arrayOne = array[:len(array)//2]
    arrayTwo = array[len(array)//2:]

    arrayOne = mergesort(arrayOne)
    arrayTwo = mergesort(arrayTwo)

    return merge(arrayOne, arrayTwo)


def merge(arrayA, arrayB):
    arrayC = []

    while len(arrayA) > 0 and len(arrayB) > 0:
        if arrayA[0] > arrayB[0]:
            arrayC.append(arrayB[0])
            arrayB.pop(0)
        else:
            arrayC.append(arrayA[0])
            arrayA.pop(0)

    #now either A or B is empty

    while len(arrayA) > 0:
        arrayC.append(arrayA[0])
        arrayA.pop(0)

    while len(arrayB) > 0:
        arrayC.append(arrayB[0])
        arrayB.pop(0)

    return arrayC

ins_start_time = time.time()
list_by_insertion = insertionsort(small_list)
insertion_time = time.time() - ins_start_time
print(insertion_time)

mer_start_time = time.time()
list_by_merge = mergesort(list)
merge_time = time.time() - mer_start_time
print(merge_time)

def_sort_start_time = time.time()
list_by_default = list.sort()
def_sort_time = time.time() - def_sort_start_time
print(def_sort_time)