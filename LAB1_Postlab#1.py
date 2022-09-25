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
    ctr = 0
    most = numlist[0]

    for i in numlist:
        freq = numlist.count(i)
        if(freq>ctr):
            ctr = freq
            most = i
        if(len(set(numlist))==len(numlist)):
            return 'There is no mode for the input number list.'
    return most

def main():
    numbers = [5,6,72,10,7,7]
    print(mean(numbers))
    print(median(numbers))
    print(mode(numbers))

if __name__=='__main__':
    main()
