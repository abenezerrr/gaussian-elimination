from UserLinearSystemInput import UserInput
from UserLinearSystemInput import KeyboardInput
from ElementaryRowReductions import ElemetaryRowReduction
from UserLinearSystemInput import FileInput

def main():
   a = FileInput()
   a.constructLists()
   list, list2, list3 = a.getLists()
   r,c = a.getRowAndCol()
   b = ElemetaryRowReduction(list, list2, list3, r, c)
   b.operations()
main()
