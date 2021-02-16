# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:

# Use binary search.
a =[7,1,2,3,4,5]

def elementSearch(list, number):
    output=False
    list = sorted(list)
    for i in list:
        if i == number:
            output=True
        else:
            output==False
    return output

# print(elementSearch(a,2))
# print(elementSearch(a,5))
# print(elementSearch(a,7))
# print(elementSearch(a,9))

def binary_search_recursive(array, element, start, end, number):
    array = sorted(array)
    output=False

    for i in array:
        if i == number:
            output=True
            return output

    if start > end:
        return output

    mid = (start + end) // 2
    if element == array[mid]:
        return output

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1, number)
    else:
        return binary_search_recursive(array, element, mid+1, end, number)

print(binary_search_recursive(a,1,0,5,0))
print(binary_search_recursive(a,1,0,5,1))
print(binary_search_recursive(a,1,0,5,7))
print(binary_search_recursive(a,1,0,5,9))