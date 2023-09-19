class Solution:
    def sortPeople(names, heights):
        temp = {}
        for i in range(len(names)):
            temp[heights[i]] = names[i]
        sortedDict = {k: temp[k] for k in sorted(temp, reverse=True)}
        return sortedDict.values()
# Time complexity: O(NlogN)
# Space complexity: O(N)
# Sort by Tim Sort (Python)
# Key is height, value is name
# Sort by height in descending order