from abc import ABC, abstractmethod
'''
get input form user
'''
class UserInput:

    @abstractmethod
    def getUserRowAndCol(self):
        pass

    @abstractmethod
    def getUserLists(self):
        pass
    
    def constructLists(self):

        self.getUserRowAndCol()
        self.__row = self.getUserRow()

        self.__column = self.getUserColumn()
    # rows
        lst = []
        lstCopy = []
        lstCopy2 = []
        self.__list = lst
        self.__list2 = lstCopy
        self.__list3 = lstCopy2

        for i in range(self.__row):
            self.getUserLists()
            items = self.getX().strip().split()

            coefs = [eval(x) for x in items]
            coefs2 = [eval(y) for y in items]
            coefs3 = [eval(z) for z in items]

            lst.append(coefs)
            lstCopy.append(coefs2)
            lstCopy2.append(coefs3)
        print("list", self.__list)
        print("r n c", self.__row, self.__column)
    def getLists(self):

        return self.__list, self.__list2, self.__list3

    def  getRowAndCol(self):

            return self.__row, self.__column

'''
get input from keyboard
'''
class KeyboardInput(UserInput):
    def __init__(self, row = 0, column = 0,  list = [], list2 = [], list3 = [],): 
        self.__row = row
        self.__column = column
        self.__list = list
        self.__list2 = list2
        self.__list3 = list3

    def getUserRowAndCol(self):
        self.row, self.column = eval(input("enter row and colomn: "))
        
        return self.row, self.column

    def getUserLists(self):
    
        print('enter row ', ':', end="")
        self.__x = input()
    
        return self.__x
'''
get input from File
'''
class FileInput(UserInput):

    def __init__(self, row = 0, column = 0,  list = [], list2 = [], list3 = [],): 
        self.__row = row
        self.__column = column
        self.__list = list
        self.__list2 = list2
        self.__list3 = list3

    def getUserRowAndCol(self):
        for i in range(1):
            self.__y = input().strip().split()
            self.__userRow = eval(self.__y[0])
            self.__userColumn = eval(self.__y[1])

        return self.__userRow, self.__userColumn
    def getUserLists(self):
        line = 1
        for i in range(1, line + 1):
            self.__x = input()
            line += 1 
        
        
        return self.__x
    def getX(self):
        return self.__x
    def getUserRow(self):
        return self.__userRow
    def getUserColumn(self):
        return self.__userColumn
