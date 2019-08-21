import sys
class Maze():
    def __init__(self):
        size=sys.stdin.readline()
        link=sys.stdin.readline()
        if size.split(' ').__len__() != 2:
            raise RuntimeError("Incorrect command format.")
        row,col=size.split(' ')
        self.row, self.col=int(row),int(col)
        self.link=link
        self.grid=[['[W]'for i in range(2 * self.col + 1)] for i in range (2 * self.row+1)]

    def checkRange(self,limit,*args):
        for i in args:
            if i<0 or i>=limit:
                raise RuntimeError("Number out of range.")

    def render(self):
        for i in range(self.row):
            for j in range(self.col):
                self.grid[2 * i + 1][2 * j + 1]='[R]'
        for cell_link in self.link.split(';'):
            tmpList=cell_link.split(' ')
            if tmpList.__len__()!=2:
                raise RuntimeError("Incorrect command format.")
            foreCell=(tmpList[0]).split(',')
            if foreCell.__len__()!=2:
                raise RuntimeError("Incorrect command format.")
            backCell=(tmpList[1]).split(',')
            if backCell.__len__()!=2:
                raise RuntimeError("Incorrect command format.")
            foreCellRow,foreCellCol=int(foreCell[0]),int(foreCell[1])
            backCellRow, backCellCol = int(backCell[0]), int(backCell[1])
            self.checkRange(self.row,foreCellRow,backCellRow)
            self.checkRange(self.col,foreCellCol,backCellCol)

            if foreCellRow==backCellRow :
                if foreCellCol==backCellCol+1 or foreCellCol==backCellCol-1:
                    self.grid[foreCellRow*2+1][foreCellCol+backCellCol+1]='[R]'
                else:
                    raise RuntimeError("Maze format error.")
            elif foreCellRow==backCellRow+1 or foreCellRow==backCellRow-1:
                if foreCellCol==backCellCol:
                    self.grid[foreCellRow+backCellRow+1][foreCellCol*2+1]='[R]'
                else:
                    raise RuntimeError("Maze format error.")
            else:
                raise RuntimeError("Maze format error.")
        return self

    def printMaze(self):
        for i in range(2*self.row+1):
           for j in range(2*self.col+1):
               print (self.grid[i][j],end=' ')
           print ()

if __name__=="__main__":
    maze = Maze()
    maze.render().printMaze()
    try:
        maze = Maze()
        maze.render().printMaze()
    except ValueError:
        print ("Invalid number format.")
        exit(1)
    except RuntimeError as e:
        print (e)
        exit(2)

'''
3 3
0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1



运行python程序，然后在命令行中输入测试用例，程序开始运行，主要功能如下:
	1.接受命令行的输入，并对输入进行判断，判断用户输入的第一行内容是否由两个数据和空格间隔的样式，如果不是则报错：Incorrect command format. 如果用户只输入一个数据和空格，则报错：Invalid number format.
	2.解析用户的第一行的数据，如果不能成功转为cell的行数和列数，则报错：Invalid number format.
	3.判断第二行的输入是否是由分号间隔的四元组形式，如果不是则报错：Incorrect command format.用户输入的四元组中间又以空格间隔开，如果不符合格式则报错Incorrect command format.
	4.判断用户的输入能否构成两个cell的行号和列号，如果输入数据不能转换为该格式，报错Invalid number format.
	5.通过cell行号和列号的关系（行号相等，列号相差一，或者列号相等，行号相差一为合法输入）判断序号能否构成连通关系，如果不能则报错Maze format error.
	6.判断cell的序号是否符合范围，如果不符合，报错Number out of range.
	7.对合法的输入进行渲染，将连通的cell之间的[W]改写为[R]

'''













