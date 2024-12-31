def Linear_Search(DATA_ARRAY:list[int], KEY:int) -> int:
    index:int = 0
    for DATA in DATA_ARRAY:
        if DATA == KEY:
            return index
        index = index + 1
    return -1
    raise Exception("Value Not in Array")