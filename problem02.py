from linked_list import first, rest, is_link, link

def linked_to_list(x):
  """
  linked list-> list
  takes in a linked list and returns a list with the same data order

  >>> linked_to_list([1,[2,[3,[4,'empty']]]])
  [1, 2, 3, 4]
  >>> linked_to_list([3,[5,[7,[9,'empty']]]])
  [3, 5, 7, 9]
  """
  result=[]
  while x != 'empty':
    result.append(first(x))
    x= rest(x)
  return result
