def goodInsert(array):
    goodInsertHelper(array, 0, len(array))

def goodInsertHelper(array, left_bound, right_bound):
    size = right_bound - left_bound
    if (size < 1): return
    mid = (right_bound + left_bound) / 2
    print array[mid]
    goodInsertHelper(array, left_bound, mid)
    goodInsertHelper(array, mid + 1, right_bound)

array = [1,2,3,4,5,6,7,8,9]

goodInsert(array)
