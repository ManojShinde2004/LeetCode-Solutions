class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []

        for i in range(len(matrix)):
           
            minimum = min(matrix[i])

           
            col = matrix[i].index(minimum)

    
            is_lucky = True

            for j in range(len(matrix)):
                if matrix[j][col] > minimum:
                    is_lucky = False
                    break

            if is_lucky:
                result.append(minimum)

        return result
        