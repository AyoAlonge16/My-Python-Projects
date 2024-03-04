def mergeList(first, second):
    combined = first + second
    combined.sort()
    return combined


# call the function    
group1 = [11,13,18,17,56]
group2 = [12,15,19,43,66]
merged = mergeList(group1, group2)
print(merged)

#This code defines a function called `mergeList` that takes two lists, `first` and `second`, as arguments. Inside the function, it combines the two lists using the `+` operator, sorts the combined list using the `sort()` method, and then returns the sorted list.

#After defining the function, it calls the `mergeList` function with two lists: `group1` and `group2`. These lists contain integer values. The merged and sorted list is stored in the `merged` variable.

#Finally, the code prints the `merged` list, which contains all the elements from `group1` and `group2`, sorted in ascending order.
