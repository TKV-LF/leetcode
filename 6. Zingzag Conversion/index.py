import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rr = range(numRows)
        pattern = list(rr) + list(range(numRows-2, 0, -1))
        print(pattern)
        times = math.ceil(len(s)/len(pattern))
        patterns = pattern*times

        arr = ["" for _ in rr]

        for a, b in zip(patterns, s):
            arr[a] += b

        return "".join(arr)
