Given an array of arrays, implement an iterator class to allow the client to
traverse and remove elements in the array list. This iterator should provide
three public class member functions:
def hasNext()
   return true or false if there is another element in the set
 def next()
   return the value of the next element in the array
def remove()
   remove the last element returned by the iterator.
   That is, remove the element that the previous next() returned
#
The code should be well structured, and robust enough to handle any access
pattern. Additionally, write code to demonstrate that the class can be used for
the following basic scenarios:
Print elements
  Given:  [[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]]
  Print:  1 2 3 4 5 6 7 8 9 10
Remove multiplies of 3
  Given:  [[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]]
  Should result in:  [[],[1,2],[4,5],[],[],[],[7,8],[],[],[10],[]]

arrayList = [[], [1, 2, 3], [4, 5], [], [], [6], [7, 8], [], [9], [10], []]
