def link(first,rest):
  assert is_link(rest)
  return [first, rest]

def first(s):
  assert is_link(s)
  assert s[0]!='empty'
  return s[0]

def rest(s):
  assert is_link(s)
  assert s[0]!='empty'
  return s[1]

def is_link(s):
  return s=='empty' or (len(s)==2 and is_link(s[1]))
