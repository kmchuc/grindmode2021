def ONotation():

    ###############For O(1) Notation:

    lst = [1,2,3]

    # if we asked up to print one number from the list using the index like this:
    print(lst[0])
    #we'd only be asking for one thing back, making the runtime O(1)

    #but say we asked for it to print twice like this:
    print(lst[0])
    print(lst[0])
    #the runtime for this would be O(2) since we're asking twice

    ##############For O(n) Notation:

    lst = [1,2,3]

    #in this example, the number of items printed has a linear relationship with the number of items on the given list, so the runtime of this would be O(n)
    #n represents the size of the input
    #doesn't matter what type of loop used
    for i in range(len(lst)-1):
        print(lst[i])
    
    #what would happen if you had a print statement before the for loop and after the for loop
    print(lst) #O(1)
    for i in range(len(lst)-1): #O(n)
        print(lst[i])
    print(lst) #O(1)
    #what is the runtime?
    #runtime: O(1) + O(n) + O(1) = O(2) + O(n) = O(2+n)
    #not a significant impact so drop the constant number (2)
    #so final runtime is O(n)

    #what if we had 2 loop statements?
    for i in range(len(lst)-1): #O(n)
        print(lst[i])
    for i in range(len(lst)-1): #O(n)
        print(lst[i])
    #runtime: O(n) + O(n) = O(2n)
    #again, drop the constant because we only need approximation
    #final runtime is O(n)

    #what if we have 2 different arrays
    #1 array with numbers and another array with names
    for i in range(len(lst)-1): #O(n)
        print(lst[i])
    for j in range(len(names)-1): #O(m)
        print(names[i])
    #since there are 2 separate inputs we use n for the numbers input and m for the names input
    #runtime = O(n) + O(m) = O(n+m)
    #again, drop the constant m, so now:
    #final runtime is O(n)

    ##################### O(n^2)

    for first in lst: #O(n)
        for second in lst: #O(n)
            print(first + "," + second)
    #runtime = O(n) * O(n) = O(n^2)
    #run quadratically so it runs slower than O(n)
    #as input grows larger, algorithms with O(n^2) get slower and slower

    for i in lst: #O(n)
        print(i)
    
    for first in lst: #O(n)
        for second in lst: #O(n)
            print(first + "," + second)
    
    #runtime = O(n) + O(n) * O(n) = O(n) + O(n^2)
    #in this case, O(n^2) is always going to be the bigger number so we drop the n in the beginning
    #final runtime: O(n^2)

    for first in lst: #O(n)
        for second in lst: #O(n)
            for third in lst: #O(n)
                print(first + "," + second + "," + third)
    #runtime = O(n) * O(n) * O(n) = O(n^3)
    #this gets slower than O(n^2)


    ################# O(logn)

    #faster and efficient than linear O(n)
    #say we have a sorted array of numbers from 1 to 10 and we want to find the number 10
    #one way is to iterate over array using "for" loop -> LINEAR SEARCH
    #another way is to start from middle item -> BINARY SEARCH
        #we check to see if the number is > or < the number we're looking for. If smaller, then number must be on the right, meaning we get rid of the left partition
        #again look at the middle of the new half
        #if the new middle is smaller than the target value we want to focus only the on the left of the partition
        #every step we're narrowing down the search by half
        #THIS IS LOGARITHMIC TIME IN ACTION
    
    ################## O(2^n)

    #oppsite of logarithmic curve
    #this type of algorithm is very slow and not efficient

    ################## Other scenarios

    for i in range(len(names)-1):
        print("Hi" + names[i])
    #since we're only printing the names again and not searching it doesn't change the runtime as much
    #runtime = O(1) space

    #copy array also has a length of the names list
    #so depending on how many items are in the names list, this runtime will be O(n)
    copy = [len(names)]
    for i in range(len(names)-1):
        print("Hi" + names[i])