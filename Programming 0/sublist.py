def tail(items):
    result = []

    for index in range(1, len(items)):
        item = items[index]
        result += [item]

    return result


def take(n, items):
    result = []

    for index in range(0, min(n, len(items))):
        result += [items[index]]

    return result


def sublist(l1, l2):
  n = len(l1)

  while len(l2) is not 0:
    if take(n, l2) == l1:
      return True
    
    l2 = tail(l2)

  return False

print(sublist([1,2],[1, 0, 1, 2, 2]))
        
    
