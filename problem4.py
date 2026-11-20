from linked_list import first,rest, is_link, link

def maximum_value(x):
  """
  linked list-> value
  takes in a linked list and returns the max value

  >>> maximum_value (link(1, link(2, link(3, link(4,'empty')))))
  4
  >>> maximum_value (link(6, link(7, link(8, link(9,'empty')))))
  9
  """
  highest_value = first(x)
  while x != 'empty':
    if first(x) > highest_value:
      highest_value = first(x)
    x = rest(x)
  return highest_value
