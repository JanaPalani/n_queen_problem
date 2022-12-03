a = []
def scratch_board():
    for i in range(8):
        a.append([])
        for j in range(8):
            a[i].append('0')

traverse_dict = {}
for i in range(8):
    traverse_dict[i] =[]
    print(traverse_dict)
queens_num =0
queen_pos  = []

def block_box(pos):
    add_pos = pos[0]+pos[1]
    sub_pos = pos[1]-pos[0]
    for i in range(8):
        for j in range(8):
            if i+j == add_pos or j-i == sub_pos:
                if a[j][i] == '0':
                    a[j][i] = '-'
        if a[pos[1]][i] == '0' :
            a[pos[1]][i] = '-'
        if a[i][pos[0]] == '0':
            a[i][pos[0]]='-'

def mark_x (pos):
    a[pos[1]][pos[0]] = 'x'
    
def backtrack(pos) :
    global a,queens_num
    queens_num -= 1
    a = []
    scratch_board()
    for i in range(queens_num+1,8):
        traverse_dict[i] = []
    queen_pos.remove(pos)
    for i in queen_pos:
        mark_x(i)
        block_box(i)

def place_queen():
    global queens_num
    for i in range(8):
        if a[queens_num][i] == '0':
            if (i,queens_num) not in traverse_dict[queens_num]:
                mark_x((i,queens_num))
                block_box((i,queens_num))
                traverse_dict[queens_num].append((i,queens_num))
                queen_pos.append((i,queens_num))
                queens_num += 1
                break

    else:
        backtrack(queen_pos[-1])
    if queens_num < 8:
        place_queen()
    if queens_num == 8:
        return a

scratch_board()
sol = place_queen()
for i in sol:
    print(i)




