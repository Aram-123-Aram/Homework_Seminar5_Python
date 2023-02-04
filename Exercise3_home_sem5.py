'''
Создайте программу для игры в ""Крестики-нолики"".
'''

matrix=[[0 for i in range(3)] for j in range(3)]
print("__________")
m=1
for i in range(3):
    for j in range(3):
        matrix[i][j]=m
        print(matrix[i][j], end=" ")
        m=m+1
    print()
print("-----------")

def winner():
    for i in range(3):
        for j in range(3):
            if matrix[i][0]==matrix[i][1]==matrix[i][2] or matrix[0][j]==matrix[1][j]==matrix[2][j]:
                print("You WIN!!! Cogretulations!!!")
                break
            if matrix[0][0]==matrix[1][1]==matrix[2][2] or matrix[0][2]==matrix[1][1]==matrix[2][0]:
                print("You WIN!!! Cogretulations!!!")
                break
        break
for k in range(9):
    n1=int(input("Player1, Enter the simvol X in number: "))
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == n1:
                matrix[i][j]='X'
            print(matrix[i][j], end=" ")
        print()
    winner()
    n2=int(input("Player2, Enter the simvol O in number: "))
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == n2:
                matrix[i][j]='O'
            print(matrix[i][j], end=" ")
        print()
    winner()