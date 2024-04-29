def find_x(list1):
    for i in range (len(list1)):
        if list1[i] == 22:
            return i
        
print(find_x([1,8,3,22,5]))


def find_x(list1):
    for item in list1:
        if item == 22:
            return list1.index(item)

print(find_x([1, 8, 3, 22, 5]))

def find_x(list1):
    i = 0
    for a in list1:
        if a == 6:
            return i
        i += 1

print(find_x([4,4,3,4,22,6]))