def uniqueOccurrences(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    arrSet = set(arr)
    if len(arrSet) == len(arr):
        return False
    else:
        arrOcc = [arr.count(i) for i in arrSet]
        if len(arrSet) == len(set(arrOcc)):
            return True
        else:
            return False