def head(list): #първи елемент от списък
    return(list[0])

def last(list): #последен елемент от списък
    return(list[len(list) - 1])

def equal_lists(list1, list2): # проверка за еднакви списъци
    if len(list1) is not len(list2):
        return False
    else:
        for index in range(0, len(list1)):
            if list1[index] is not list2[index]:
                return False
    return True

def tail(list1):
    result = []

    for index in range(1, len(list1)):
        result += [list1[index]]
    return result
        


def count_item(n, list1):
    counter = 0

    for count in list1:
        if count == n:
            counter += 1

    return counter

def take(n, list1):
    n = round(n)
    result = []

    for index in range(0, n):
        result += [list1[index]]

    return result

def drop(n, list1):
    n = round(n)
    result = []
    
    if n > len(list1):
        return False
    for index in range(n, len(list1)):
        result += [list1[index]]
    return result


def reverse(items):
    result = []

    last_index = len(items) - 1

    while last_index >= 0:
        result += [items[last_index]]
        last_index -= 1

    return result



print(head([1,2,3]))
print(last([1, 2, 3]))
print(tail([1, 2, 3]))
print(equal_lists([1, 2], [1, 2]))
print(count_item(5, [1, 2, 3, 4, 5]))
print(take(2, [1, 2, 3, 4, 5]))
print( drop(1, [1, 2, 3]))
print(reverse(["Speak", "in", "reverse", "you", "must!"]))
        
