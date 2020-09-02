from collections import deque
from typing import List

'''
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

 

示例 1:

输入: 2, [[1,0]] 
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
 

提示：

输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5
'''
class Solution207:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        rely = [[] for j in range(numCourses)]
        zeroDegree = []
        indgree = [0 for i in range(numCourses)]
        for i,j in prerequisites:
            indgree[i]+=1
            rely[j].append(i)
        for i in range(numCourses):
            if indgree[i] == 0:
                zeroDegree.append(i)

        while zeroDegree:
            a = zeroDegree.pop()
            for i in rely[a]:
                indgree[i] -= 1
                if indgree[i]==0:
                    zeroDegree.append(i)
            numCourses -= 1
        return 0==numCourses

    def canFinish_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            if visit_flag[i]==1:
                return True
            elif visit_flag[i] == -1:
                return False
            else:
                visit_flag[i] = -1
                for j in rely[i]:
                    if not dfs(j):
                        return False
                visit_flag[i] = 1
                return True


        visit_flag = [0 for i in range(numCourses)]
        rely = [[] for j in range(numCourses)]
        for i, j in prerequisites:
            rely[j].append(i)
        for i in range(numCourses):
            if  not dfs(i):
                return False
        return True


'''输出课程的顺序'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        rely = [[] for j in range(numCourses)]
        zeroDegree = []
        indgree = [0 for i in range(numCourses)]
        for i, j in prerequisites:
            indgree[i] += 1
            rely[j].append(i)
        for i in range(numCourses):
            if indgree[i] == 0:
                zeroDegree.append(i)

        cur = 0
        while cur<len(zeroDegree):
            a = zeroDegree[cur]
            cur +=1
            for i in rely[a]:
                indgree[i] -= 1
                if indgree[i] == 0:
                    zeroDegree.append(i)
        return zeroDegree if cur == numCourses else []

    def canFinish_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            if visit_flag[i] == 1:
                return True
            elif visit_flag[i] == -1:
                return False
            else:
                visit_flag[i] = -1
                for j in rely[i]:
                    if not dfs(j):
                        return False
                visit_flag[i] = 1
                return True

        visit_flag = [0 for i in range(numCourses)]
        rely = [[] for j in range(numCourses)]
        for i, j in prerequisites:
            rely[j].append(i)
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


print(Solution().findOrder( 3,
[[2,0],[2,1]]))