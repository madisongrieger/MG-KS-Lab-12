from linked_list import first, rest, is_link, link

def list_to_linked(x):
  """
  list -> linked list
  takes in a list and returns a linked list with the same data in the same order
  
  >>> list_to_linked([1,2,3,4])
  [1, [2, [3, [4, 'empty']]]]
  >>> list_to_linked([4,5,7,9])
  [4, [5, [7, [9, 'empty']]]]
  """
  result = 'empty'
  i= len(x) -1
  while i>=0:
    result= link(x[i], result)
    i-= 1
  return result 
