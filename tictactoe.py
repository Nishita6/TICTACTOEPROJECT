grid = [
    ["_","_","_"], ["_", "_", "_"],["_", "_", "_"],
]

#computer 1  #computer 2
# let computer 1 enters 0 and computer 2 enter *
#1st chance of computer 1 and second of computer 2
count=0
while count!=9:
    row1=int(input("which row you want your move"))
    col1=int(input("which column you want your move"))
    if count%2==0:
        grid[row1][col1]="0"
    else:
        grid[row1][col1] = "*"
    count+=1
    if grid[0][0] == grid[0][1] == grid[0][2] == "0" or grid[1][0] == grid[1][1] == grid[1][2] == "0" or grid[2][0] == \
            grid[2][1] == grid[2][2] == "0" or grid[0][0] == grid[1][0] == grid[2][0] == "0" or grid[0][1] == grid[1][
        1] == grid[2][1] == "0" or grid[0][2] == grid[1][2] == grid[2][2] == "0" or grid[1][1] == grid[0][0] == grid[2][
        2] == "0" or grid[0][2] == grid[1][1] == grid[2][0] == "0":
       break

    elif grid[0][0] == grid[0][1] == grid[0][2] == "*" or grid[1][0] == grid[1][1] == grid[1][2] == "*" or grid[2][0] == \
            grid[2][1] == grid[2][2] == "*" or grid[0][0] == grid[1][0] == grid[2][0] == "*" or grid[0][1] == grid[1][
        1] == \
            grid[2][1] == "*" or grid[0][2] == grid[1][2] == grid[2][2] == "*" or grid[1][1] == grid[0][0] == grid[2][
        2] == "*" or grid[0][2] == grid[1][1] == grid[2][0] == "*":
        break

    for row in grid:
        for col in row:
            print(col, end="")
        print("\n")  # this end is to use if we do not want to print in a new line

if (grid[0][0]==grid[0][1]==grid[0][2]=="0" or grid[1][0]==grid[1][1]==grid[1][2]=="0"
        or grid[2][0]==grid[2][1]==grid[2][2]=="0" or grid[0][0]==grid[1][0]==grid[2][0]=="0" or grid[0][1]==grid[1][1]==grid[2][1]=="0"
        or grid[0][2]==grid[1][2]==grid[2][2]=="0" or grid[1][1]==grid[0][0]==grid[2][2]=="0" or grid[0][2]==grid[1][1]==grid[2][0]=="0"):
    print("computer 1 wins")

elif grid[0][0] == grid[0][1] == grid[0][2] == "*" or grid[1][0] == grid[1][1] == grid[1][2] == "*" or grid[2][0] == \
        grid[2][1] == grid[2][2] == "*" or grid[0][0] == grid[1][0] == grid[2][0] == "*" or grid[0][1] == grid[1][1] == \
        grid[2][1] == "*" or grid[0][2] == grid[1][2] == grid[2][2] == "*" or grid[1][1] == grid[0][0] == grid[2][
    2] == "*" or grid[0][2] == grid[1][1] == grid[2][0] == "*":
    print("computer 2 wins")
else:
    print("match draws")

