def Arrays():

    #just to review, what is the runtime of this list?
    nums = [10, 20, 30, 40, 50]
    #runtime is O(1) because the indexing address would be called one by one

    #we need to know ahead of time how many items that will be in the array
    #if we want to add another item to the array, we'd have to copy this entire array into a new array along with space for a new item
    nums = [10, 20, 30, 40, 50] #O(1)
    new_nums = [10, 20, 30, 40, 50, , , , ] #O(n)
    #what would the runtime be for this new list?
    #runtime = O(1) + O(n)
    #drop the constants O(1) 
    #final runtime = O(n)

    #runtimes for array editing:
    #lookup: O(1) because you're only looking for a single item using indexing
    #insert: O(n) because you don't know how long the length of the list is so it could displace items
    #deletion: O(n) because worst case scenario you have delete something from the beginning, causing all the other items to shift to the left

    numbers = []

    numbers.append(10)
    numbers.append(20)
    numbers.append(30)
    numbers.append(40)
    print(numbers)
    numbers.pop(3)
    print(numbers.index(10))