def quickSort(array):
    left = []
    equal = []
    right = []
    if len(array) > 1:
        for i in array:
            pivot = array[0]
            if i == pivot:
                equal.append(i)
            elif i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
        return qSort(left) + equal + qSort(right)
    else:
        return array
