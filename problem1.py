from linked_list import first, rest, is_link, link

def remove_duplicates(x):
  '''
  linked list -> linked list
  takes in a linked list and looks repeating elements and returns a new linked list only containing unique elements
  
  >>> remove_duplicates(link(63,link(67,(link(27,link(25,link(63,link(8,'empty'))))))))
  link(63,link(67,link(27,link(25,link(8,'empty')))))
  >>> remove_duplicates(link(1,link(1,link(1,link(1,'empty')))))
  link(1,'empty')
  >>> remove_duplicates(link(10, link(20, link(10, link(30, link(20, link(40, 'empty')))))))
  [10, [20, [30, [40, 'empty']]]]
  >>> remove_duplicates('empty')
  'empty'
  '''
  unqiue=[]
  while x != 'empty':
    if first(x) not in unique:
      unqiue.append(first(x))
    x= rest(x)
  result= 'empty'
  i=len(unqiue)-1
  while i>= 0:
    result = link(unqiue[i], result)
    i = i-1
  return result
