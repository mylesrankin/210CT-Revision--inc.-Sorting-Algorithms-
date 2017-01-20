def listCheck(array,element):
    if array[0] == element:
        return True
    elif len(array) == 1 and array[0] != element:
        return False
    else:
        return listCheck(array[1:],element)
