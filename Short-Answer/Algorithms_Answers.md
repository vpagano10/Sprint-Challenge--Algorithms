#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    - Setting a = 0 is of constant time
    - The while loop sets a to the value of a=a+n*n (which is constant) continuously until a is >= n which in this case will take 'n' time.
    
    The result of this first example is O(n)

b)
    - Function contnues to run until the end of the assignment n -> O(1)
    - For each i in n -> O(n)
        - j doubles for each i until j >= n
        - sum += 1 each time j doubles
            - sum counts the number of times j has to double before its >= n for each i in range(n)
        - for each doubled i in range(n) (for ex: i=1, 2, 4, 8, 16, 32...) it only increases the sum count of j by 1 -> O(log(n))

    The result of this second example is O(nlog(n))

c)
    - A function that takes in an input is of constant time -> O(1)
    - If input == 0, return 0 is of constant time -> O(1)
    - Return 2 + recursion_of_current_function at a new input of (input - 1) will result in 'n' the function recursing 'n' times -> O(n)

    The result of this third example is O(n)


## Exercise II

- make a list (height) = [range(len(height of building) + 1)]
    - height represents height of a building in floors

- make function that takes 2 inputs of (height) and target floor (target)
    - target represents the floor at which the egg does/doesn't break

- since we know our height array is in order because it represents a range from 0 to the height of the building. We can use a binary search to find the target floor faster than a linear search.

in the function...
- make variable to find the middle floor = len(height) // 2
- make variables left and right = height[:mid] and height[mid:]
- if the target = middle floor variable, return our answer
- else, if the target is > the middle floor, re-set our low floors section (left) to start at the middle variable +1 and find the new middle.
- else, our target is < the middle floor, and you must re-set our high floors section (right) to end at the middle floor and find our new middle
- these steps continue until we find our target floor

Time:
- since each double of the height of the building will only result in 1 extra split of the height arr, time complexity = O(log(n))