from linked_list import first, rest, is_link, link

def merge(x,y):
  '''
  linked list, linked list-> linked list
  takes in two sorted linked lists and returns a new linked list that contains all elements in the two lists in sorted order

  >>> merge(link(1,link(2,link(3,link(4,'empty')))),link(5,link(6,'empty')))
  link(1,link(2,link(3,link(4,link(5,link(6,'empty'))))))
  >>> merge(link(3,link(6,link(7, link(8, 'empty')))), link(9,link(10,'empty')))
  link(3,link(6,link(7,link(8,link(9,link(10,'empty'))))))
  >>>merge (link(2,link(4,link(6,'empty'))),link(7,link(8,'empty')))
  link(2,link(4,link(6,link(7,link(8,'empty')))))
  '''
  
