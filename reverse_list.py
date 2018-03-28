''' Write a recursive function to reverse a list. '''

def reverseListRec(n):
    if len(n) == 0:
        return n
    else:
        return n[-1:] + reverseListRec(n[:-1])
    
def main():
    n = [1, 3, 10, 7, 9]
    print(reverseListRec(n))

main()