''' Write a short recursive Python function that finds the minimum and maximum
values in a sequence without using any loops. '''

# Decided to divide max and min into two seperate functions, but this function returns both

def findMinMaxRec(n):
    return findMax(n), findMin(n)

def findMax(n):
    # if the list has only one element, then return that element because that is the max
    if len(n) == 1:
        return n[0]
    # the list has multiple elements
    else:
        # max is set recursively while splicing the sequence. Once it reaches one element, goes to first if statement.
        max = findMax(n[1:])
        return max if max > n[0] else n[0]

def findMin(n):
    if len(n) == 1:
        return n[0]
    else:
        min = findMin(n[1:])
        return min if min < n[0] else n[0]

def main():
    n = [1, 3, 10, 0, 9]
    print(findMinMaxRec(n))

main()