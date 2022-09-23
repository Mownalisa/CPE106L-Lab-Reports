#Starting out
enterfile = input("Enter the textfile name: ")
file = open(enterfile, 'r')
linecount = 0

#Line count in text file
for line in file:
    linecount = linecount + 1

print("There are", linecount, "lines in this text file")

#Loop for reading file
while True:
    linenum = 0

    num = int(input("Please enter a line number to show the content or press 0 to quit: "))
    if num >=1 and num <= linecount:
        file = open(enterfile, 'r')
        for lines in file:
            linenum = linenum + 1
            if linenum == num:
                print(lines)
    else:
        if num == 0:
            print("Thanks you and have a nice day!")
            break
#End of program