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
                    