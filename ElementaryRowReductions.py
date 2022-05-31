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
    Make enrties below a pivot zeros.
    '''
    def rowReduction(self):
        
        for i in range((self.__checkedRows), self.__row):

            self.__pivotRowElements = self.__list[self.__pivotRow]
            tobeZero = self.__list[i][self.__pivotColumn]

            # only one row reduced at a time
            if  tobeZero != 0:
                
                for j in range(self.__column):
                    #multiply the the pivot row in the copy list
                    self.__list2[self.__pivotRow][j] = self.__list[self.__pivotRow][j] * ((-1) * \
                        (tobeZero / self.pivot ))

                    # add it to the rows below a pivot row
                    self.__list[i][j] += self.__list2[self.__pivotRow][j]
                    self.__list3[i][j] += self.__list2[self.__pivotRow][j]

    ''' 
    Check the consistency of the system.
    '''         
    def checkConsistency(self):

        self.isConsistent = True
        for i in range(len(self.__pivotrowlst)):

            if self.__pivotrowlst[i][1] == (self.__column - 1) :
                self.isConsistent = False
                print('             System is inconsistent')  

    '''
    Make pivots zeros and entries above the pivots and below it zeros
    '''    
    def backwardPhase(self):

       for k in range(len(self.__pivotrowlst)):

           # back pivot columns and rows
           self.backPivotRow = self.__pivotrowlst[((len(self.__pivotrowlst) - 1) - k)][0]
           self.backPivotColumn = self.__pivotrowlst[((len(self.__pivotrowlst) - 1) - k)][1]
          
           #back pivot
           self.backPivot = self.__list[self.backPivotRow][self.backPivotColumn]
           
           #scale pivots to 1 if not 1
           if self.backPivot != 1 :
            
               # divide the back pivot row by the back pivot
               for l in range(self.__column):
                   self.__list[self.backPivotRow][l] = (self.__list[self.backPivotRow][l]) / \
                       (self.backPivot)
                   self.__list3[self.backPivotRow][l] =(self.__list3[self.backPivotRow][l]) / \
                       (self.backPivot)
               self.backPivot = self.__list[self.backPivotRow][self.backPivotColumn]
               
           for i in range(1, self.__row):
               backPhaseTobemadeZero = self.__list[(self.backPivotRow - i)][self.backPivotColumn] 
               
               if backPhaseTobemadeZero != 0:
                   for j in range(self.__column):
                       #multiply the the back pivot row
                       self.__list3[self.backPivotRow][j] = self.__list[self.backPivotRow][j] * ((-1) * \
                           backPhaseTobemadeZero / self.backPivot )
                      
                       # add it to the rows above a back pivot row
                       self.__list[(self.backPivotRow - i)][j] += self.__list3[self.backPivotRow][j]