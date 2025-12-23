#Assignment 2 - task 5
N = int(input())
C = 'ABCEHKMOPTXY'

for i in range(N):
    plate = input()
    if (
        len(plate) == 6 and
        plate[0] in C and plate[4] in C and plate[5] in C and
        plate[1].isdigit() and plate[2].isdigit() and plate[3].isdigit()
    ):
        print("Yes")
    else:
        print("No")