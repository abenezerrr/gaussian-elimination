'''
perform elemenatery row reductions
'''
class ElemetaryRowReduction:

    def __init__(self, list, list2, list3, row, column):
        self.__list = list
        self.__list2 = list2
        self.__list3 = list3
        self.__row = row
        self.__column = column
    

    '''
    Put a zero at the leading entry positon
    '''
    def leadingEntry(self):

        if self.__list[0][0] == 0:
            if self.__list[len(self.__list) -1][0] != 0:
                x = self.__list[0]
                y = self.__list[len(self.__list) -1] #swap pos with last row if last row not 0
                self.__list[0] = y
                self.__list[len(self.__list) -1] = x
            else:
                for j in range(1, self.__row) :

                    if self.__list[j][0] != 0 :
                        x = self.__list[0]
                        y = self.__list[j]
                        self.__list[0] = y
                        self.__list[j] = x
                        break
        # arrange the leading entery for the copy list
        if self.__list2[0][0] == 0:
            if self.__list2[len(self.__list2) -1][0] != 0:
                x = self.__list2[0]
                y = self.__list2[len(self.__list2) -1] #swap pos with last row if last row not 0
                self.__list2[0] = y
                self.__list2[len(self.__list2) -1] = x
            else:
                for j in range(1, self.__row) :

                    if self.__list2[j][0] != 0 :
                        x = self.__list2[0]
                        y = self.__list2[j]
                        self.__list2[0] = y
                        self.__list2[j] = x
                        break
    '''
    Determine the next pivot position.
    '''
    def pivotCheck(self):
        
        for i in range(self.__checkedRows, self.__row): 
            for j in range(self.__column):
            
                if self.__list[i][j] != 0:
                    pos = [i,j]
                    self.__pivotrowlst.append(pos)
                    self.__pivotRow = i
                    self.__pivotColumn = j
                    self.pivot = self.__list[i][j]
                    break
            
            self.__checkedRows += 1
            if len(self.__pivotrowlst) >= 1:

                break
    ''' 
    Check the consistency of the system.
    '''         
    def checkConsistency(self):

        self.isConsistent = True
        for i in range(len(self.__pivotrowlst)):

            if self.__pivotrowlst[i][1] == (self.__column - 1) :
                self.isConsistent = False
                print('             System is inconsistent')       