class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """
            CONTAINT LAST ELEMENT OF ARRAY AND ADD TO THE END OF ARRAY
            biggest number will be at the end of array first
        """
        a, b, write_index = m-1, n-1, m + n - 1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                nums1[write_index] = nums2[b]
                b -= 1

            write_index -= 1
        """
            loop decrement m 
            after that loop decrement n
            O(m+n)
        """
        # if m == 0:
        #     for i in range(n):
        #         nums1[i] = nums2[i]
        # else:
        #     while m > 0:
        #         if n == 0:
        #             break
        #         if nums1[m - 1] < nums2[n-1]:
        #             nums1.insert(m, nums2[n-1])
        #             nums1.pop()
        #             n -= 1
        #         else: 
        #             m -= 1

        #     if n > 0:
        #         for i in range(n):
        #             nums1.insert(i, nums2[i])
        #             nums1.pop()


