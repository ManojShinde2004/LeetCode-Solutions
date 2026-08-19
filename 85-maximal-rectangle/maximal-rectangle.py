class Solution(object):
    def maximalRectangle(self, matrix):

        if not matrix or not matrix[0]:
            return 0

        l = [0] * len(matrix[0])
        max_size = 0

        def maxi(l1):
            curr_max = 0

            for i in range(len(l1)):
                minimum = float('inf')

                for j in range(i, len(l1)):
                    minimum = min(minimum, l1[j])

                    area = minimum * (j - i + 1)

                    curr_max = max(curr_max, area)

            return curr_max

        for i in range(len(matrix)):

            for j in range(len(matrix[0])):

                if matrix[i][j] == "1":
                    l[j] += 1
                else:
                    l[j] = 0

            max_size = max(max_size, maxi(l))

        return max_size