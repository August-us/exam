# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
#  例如 \begin{bmatrix} a & b & c &e \\ s & f & c & s \\ a & d & e& e\\ \end{bmatrix}\quad
#   矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子

# 自己的代码，递归层数浅，但是代码长
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        matrix=list(map(lambda x:matrix[x*cols:x*cols+cols],range(0,rows)))
        visited=[[False]*cols for i in range(rows)]
        if not path:
            return False
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==path[0]:
                    visited[i][j]=True
                    flag=self.findPath(matrix,path,1,rows,cols,i,j,visited)
                    if flag:
                        return True
                    visited[i][j]=False
        return False

    def findPath(self, matrix, path,start, rows, cols, i, j, visited):
        if start==len(path):
            return True
        if i-1>=0  and not visited[i-1][j] and matrix[i-1][j]==path[start]:
            visited[i-1][j] = True
            flag = self.findPath(matrix, path,start+1, rows, cols, i-1, j, visited)
            if flag:
                return True
            visited[i-1][j] = False
        if i+1<rows and not visited[i+1][j] and matrix[i+1][j]==path[start]:
            visited[i+1][j] = True
            flag = self.findPath(matrix, path,start+1, rows, cols, i+1, j, visited)
            if flag:
                return True
            visited[i+1][j] = False

        if j-1>=0 and not visited[i][j-1] and matrix[i][j-1]==path[start]:
            visited[i][j-1] = True
            flag = self.findPath(matrix, path,start+1, rows, cols, i, j-1, visited)
            if flag:
                return True
            visited[i][j-1] = False
        if j+1<cols and not visited[i][j+1] and matrix[i][j+1]==path[start]:
            visited[i][j+1] = True
            flag = self.findPath(matrix, path,start+1, rows, cols, i, j+1, visited)
            if flag:
                return True
            visited[i][j+1] = False
        return False


class Solution1:
    def hasPath(self, matrix, rows, cols, path):
        visited=[False]*(cols*rows)
        print(len(visited))
        if not path:
            return False
        for i in range(rows):
            for j in range(cols):
                flag=self.findPath(matrix,path,1,rows,cols,i,j,visited)
                if flag:
                    return True
        return False

    def findPath(self, matrix, path,start, rows, cols, i, j, visited):
        if start==len(path):
            return True
        if(i>=0 and i<rows and j>=0 and j<=cols):
            visited[i * cols + j] = True
            if (self.findPath(matrix, path,start+1, rows, cols, i-1, j, visited) or
                    self.findPath(matrix, path,start+1, rows, cols, i+1, j, visited) or
                    self.findPath(matrix, path, start + 1, rows, cols, i, j - 1, visited) or
                    self.findPath(matrix, path, start + 1, rows, cols, i, j + 1, visited)
                ):
                return True
            else:
                visited[i * cols + j] = False
        return False

print(Solution1().hasPath("DFCBAB",2,3,"ABD"))