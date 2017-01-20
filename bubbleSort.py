def bubbleSort(list):
    sorted = False
    length = len(list)-1
    while not sorted:
        sorted = True
        for i in range(length):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1],list[i]
                print(i)
                print(list)
    return list
                

'''
In English/Pseudocode:

BUBBLESORT(LIST)
    LIST_SORTED <- FALSE
    LIST_LENGTH <- LEN(LIST)-1
    WHILE LIST_SORTED IS FALSE
          LIST_SORTED <- TRUE
          FOR I IN 0 TO LIST_LENGTH
               IF LIST[I] MORE THAN LIST[I+1]
                   SORTED <- FALSE
                   SWAP(LIST[I], LIST[I+1])
    RETURN LIST

'''
    
