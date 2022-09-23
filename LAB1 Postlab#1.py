"""
Author:
Program Description:

"""

def mean(numlist):
    sum = 0 
    for num in numlist:
        sum = sum + num
    return sum / len(numlist)

def median(numlist):
    numlist.sort()
    median = 0
    if len(numlist) % 2 == 1:
        median = numlist[len(numlist)/2]
    if len(numlist) % 2 == 0:
        median = (numlist[int(len(numlist)/2)] + numlist[int(len(numlist)/2-1)])/2
    return median

def mode(numlist):
    return 0

def main():
    numbers = [5,6,72,10,7,8]
    print(mean(numbers))
    print(median(numbers))
    print(mode(numbers))

if __name__=='__main__':
    main()
