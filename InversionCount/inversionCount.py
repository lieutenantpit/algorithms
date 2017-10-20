import time

def merge(array, temp, left, mid, right):
    result = 0
    i = left
    j = mid
    k = left

    while (i <= mid-1) and (j <= right):
        if array[i] < array[j]:
            temp[k] = array[i]
            k += 1
            i += 1
        else:
            temp[k] = array[j]
            k += 1
            j += 1
            result += mid-i

    while i <= mid-1:
        temp[k] = array[i]
        k += 1
        i += 1

    while j <= right:
        temp[k] = array[j]
        k += 1
        j += 1

    i = left
    while i <= right:
        array[i] = temp[i]
        i += 1

    return result

def mergeSort(array, temp, left, right):
    result = 0
    if right > left:
        mid = (right + left)//2
        result += mergeSort(array,temp,left, mid)
        result += mergeSort(array, temp, mid+1, right)
        result += merge(array, temp, left, mid+1, right)
    return result

def getInvCount(array, n):
    temp = [0 for x in range(len(array))]
    return mergeSort(array, temp, 0, len(array)-1)

# POINT OF THE START PROGRAMM

array = []
file = open("IntegerArray.txt")
for line in file:
    array.append(int(line))

t1 = time.clock()
result = getInvCount(array, len(array))
t2 = time.clock()
delta = (t2 - t1)
# delta = (t2 - t1) * 1000000
print('Count of Inversions is {}, running time is {:.3f}s.'.format(result, delta))
print('Count of Inversions is 2407905288, running time is 880.864s.')
