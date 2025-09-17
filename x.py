left_board = int(input())
right_board = int(input())

x = True
while True:
    number = int(input())
    if number == '':
        break
    if number >= right_board or number <= left_board:
        x = False
print(x)