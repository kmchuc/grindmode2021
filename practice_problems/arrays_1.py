def array():
    items = [1,2,3]

    items.pop(1)

    for i in range(len(items)):
        print(items[i])
    
    print(items)
    print(items.index(3))

array()
