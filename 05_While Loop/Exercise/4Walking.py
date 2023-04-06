length = int(input())
width = int(input())
all_pieces = length * width
eaten_pieces = 0
no_cake = False
command = input()
eaten_cake = 0

while command != 'STOP':
    eaten_pieces = int(command)
    all_pieces -= eaten_pieces
    if all_pieces <= 0:
        no_cake = True
        break
    command = input()

left = abs(all_pieces)

if no_cake:
    print(f'No more cake left! You need {left} pieces more.')
else:
    print(f'{left} pieces are left.')
