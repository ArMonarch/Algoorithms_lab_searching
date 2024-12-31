def Binary_Search(DATA_ARRAY:list[int], KEY:int, start:int=0, end:int=-1) -> int:
    if end == -1:
        end = (DATA_ARRAY.__len__() - 1)
    
    middle:int = (start + end) // 2

    if DATA_ARRAY[middle] == KEY:
        return middle
    
    elif KEY < DATA_ARRAY[middle]:
        return Binary_Search(DATA_ARRAY, KEY, start=start, end=(middle-1)) # search the left half
    
    elif KEY > DATA_ARRAY[middle]:
        return Binary_Search(DATA_ARRAY, KEY, start=(middle+1), end=end) # search the right half
    else:
        raise Exception("Value Not found")
