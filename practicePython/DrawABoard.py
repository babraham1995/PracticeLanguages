# checkX = [1,2,3,4,5,7]
# checkY = [1,2,3,4,5,7]
# # blankDummy = [9,9,9,9,9,9]

# def inputMoves():
#     x = input("choose a x square")
#     y = input("choose a y square")
#     moves(x,y)

# def moves(x, y):
#     checkX.append(x)
#     checkY.append(y)
#     return checkY, checkX

# # def drawBoard(rows, columns, checkX, checkY):
# #     for i in range(0, rows):
# #         drawHorizontal(columns)
# #         print("\n")
# #         drawVertical(columns, checkX, checkY)
# #         print("\n")
# #     drawHorizontal(columns)
    
# def drawHorizontal(rows):
#     for i in range(0, rows):
#             print(' ___', end='')

# def drawVertical(columns, checkX, checkY):
#     for x in range(0, columns+1):
#         if checkX[x] == 0:
#             print("|   ", end='')
#             continue
#         elif x == checkX[x]:
#             print("| * ", end='')
#             continue
#     print("|   ", end='')


# def drawBoard(rows, columns, checkX, checkY):
#     for rowi in range(0, rows):
#         drawHorizontal(columns)
#         print("\n")
#         for columnx in range(0, columns+1):
#             # print(x, rowi, checkX[x], checkX[i])
#             for arrayx in checkX:
#                 if arrayx == checkX[columnx] & rowi == checkY[rowi]:
#                     print("| * ", end='')
#                     continue
#             print("|   ", end='')
#         # drawVertical(columns, checkX, checkY)
#         print("\n")
#     drawHorizontal(columns)








# # inputMoves()
# drawBoard(5, 5, checkX, checkY)

points=[[1,0,0],[0,1,0],[0,0,1]]

for i in points:
    for x in i:
        if x==1:
            print("*", end='')
        else: print(".", end='')
    print("\n")

# for 1, 3:
#     if x= 1:
#         for 1, 3:


        

# for y in range(0,boardYLength):
#     for x in range(0,boardXLength):
#         if x in array[x][0] & y in array[0][x]:
#             print('*')
#         else:print('.')