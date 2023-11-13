class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for k in range(n//2):
            for i in range(k,n-k-1):
                tmp = matrix[i][n-k-1]
                matrix[i][n-k-1] = matrix[k][i]

                tmp1 = matrix[n-1-k][n-1-i]
                matrix[n-1-k][n-1-i] = tmp

                tmp2 = matrix[n-i-1][k]
                matrix[n-1-i][k]=tmp1
                
                matrix[k][i]=tmp2
            print(matrix)
        return matrix


#ANOTHER INTERSTING AND EASY WAY TO DO IT
# void rotate(vector<vector<int> > &matrix) {
#     reverse(matrix.begin(), matrix.end());
#     for (int i = 0; i < matrix.size(); ++i) {
#         for (int j = i + 1; j < matrix[i].size(); ++j)
#             swap(matrix[i][j], matrix[j][i]);
#     }
# }

# /*
#  * anticlockwise rotate
#  * first reverse left to right, then swap the symmetry
#  * 1 2 3     3 2 1     3 6 9
#  * 4 5 6  => 6 5 4  => 2 5 8
#  * 7 8 9     9 8 7     1 4 7
# */
# void anti_rotate(vector<vector<int> > &matrix) {
#     for (auto vi : matrix) reverse(vi.begin(), vi.end());
#     for (int i = 0; i < matrix.size(); ++i) {
#         for (int j = i + 1; j < matrix[i].size(); ++j)
#             swap(matrix[i][j], matrix[j][i]);
#     }
# }