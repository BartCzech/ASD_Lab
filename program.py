import time
import random

def create_list():
    list = []
    for i in range(5000):
        list.append(random.randint(0, 50000))
    return list

#print(list)

#insertion sort
def insertionsort(array):
    for i in range(1, len(array)):
        x = array[i]
        j = i - 1
        while j >= 0 and array[j] > x:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = x
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

def check_insertion(list):
    ins_start_time = time.time()
    list_by_insertion = insertionsort(list)
    insertion_time = time.time() - ins_start_time
    return insertion_time

def check_merge(list):
    mer_start_time = time.time()
    list_by_merge = mergesort(list)
    merge_time = time.time() - mer_start_time
    return merge_time

def check_default(list):
    def_sort_start_time = time.time()
    list_by_default = list.sort()
    def_sort_time = time.time() - def_sort_start_time
    return def_sort_time

def print_average(insertion_times, merge_times, default_times):
    print('\nAverage insertion time: ' + str(sum(insertion_times)/len(insertion_times)))
    print('Average merge time: ' + str(sum(merge_times)/len(merge_times)))
    print('Average default sort time: ' + str(sum(default_times)/len(default_times)))

def print_fastest(insertion_times, merge_times, default_times):
    print('\nFastest insertion time: ' + str(min(insertion_times)))
    print('Fastest merge time: ' + str(min(merge_times)))
    print('Fastest default sort time: ' + str(min(default_times)))

def print_slowest(insertion_times, merge_times, default_times):
    print('\nSlowest insertion time: ' + str(max(insertion_times)))
    print('Slowest merge time: ' + str(max(merge_times)))
    print('Slowest default sort time: ' + str(max(default_times)))


def check_time():
    insertion_times = []
    merge_times = []
    default_times = []
    for i in range(1, 101):
        list = create_list()

        ins = check_insertion(list)
        mer = check_merge(list)
        default = check_default(list)

        insertion_times.append(ins)
        merge_times.append(mer)
        default_times.append(default)

    print_average(insertion_times, merge_times, default_times)
    print_fastest(insertion_times, merge_times, default_times)
    print_slowest(insertion_times, merge_times, default_times)

check_time()