import operator
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = {'+':lambda x,y:x+y, '-':lambda x,y:y-x,'*':lambda x,y:x*y,'/':lambda x,y:int(y/x)}

        nums =[]
        for i in tokens:
            if i.isnumeric() or i[1:].isnumeric():
                nums.append(int(i))
            else:
                x = nums.pop()
                y = nums.pop()
                nums.append(operation[i](x,y))
        return nums[-1]

# token = ["4", "13", "5", "/", "+"]
# token = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
token = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(token))
