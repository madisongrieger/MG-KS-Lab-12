import linked_list

def remove_duplicates(x):
  '''
  takes in a linked list and looks for any

  >>> remove_duplicates(link(63,link(67,(link(27,link(25,link(63,link(8,'empty'))))))))
  link(63,link(67,link(27,link(25,link(8,'empty')))))
  >>> remove_duplicates(link(1,link(1,link(1,link(1,'empty')))))
  link(1,'empty')
  '''
