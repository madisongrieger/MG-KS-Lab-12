from linked_list import first, rest, is_link, link

def rotate_by_n(x,n):
  '''
  linked list, int-> linked list
  takes in a linked list and a number, n, and returns a linked list with each value shifted n positions to the right

  >>> rotate_by_n(link(1,link(2,link(3,link(4,'empty')))),3)
  link(2,link(3,link(4,link(1,'empty'))))
  >>> rotate_by_n(link(1,link(2,link(3,link(4,'empty')))),1)
  link(4,link(1,link(2,link(3,'empty'))))
  >>> rotate_by_n('empty', 2)
  'empty'
  >>> rotate_by_n(link(1,link(2,link(3,'empty'))), 5) 
  link(2,link(3,link(1,'empty')))
  '''
  if x == 'empty':
    return 'empty'
  i=[]
  while x != 'empty':
    i.append(first(x))
    x=rest(x)
  n= n% len(i)
  rotated= i[-n:] + i[:-n]
  result='empty'
  i = len(rotated)-1
  while i>=0:
    result = link(rotated[i], result)
    i=i-1
  return result
