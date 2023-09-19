def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    bigList = nums1
    smallList = nums2
    lenSmall = len(nums2)
    totalLen = 0
    if len(bigList) < len(smallList):
        bigList = nums2
        smallList = nums1
        lenSmall = len(smallList)
        totalLen = len(bigList) + lenSmall
    for i, value in enumerate(bigList):
        if lenSmall != 0:
            if value > smallList[0]:
                bigList.insert(i, smallList[0])
                smallList.pop(0)
                lenSmall -= 1

    if lenSmall > 0:
        bigList = bigList + smallList
    temp = totalLen % 2
    return statistics.median(bigList)
