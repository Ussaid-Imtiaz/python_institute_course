
rows = [list(input("")) for i in range(0,9)]
cols = [[rows[row][col] for row in range(len(rows))] for col in range(len(rows[0]))]
squares = [
    [rows[i + x][j + y] for x in range(3) for y in range(3)]
    for i in range(0, 9, 3) for j in range(0, 9, 3)
]

def check_sudoko(rows):
    num_to_check = [str(i) for i in range(1,10)]
# Check Rows
    for i in rows:
        i.sort()
        if i != num_to_check:
            print("No")
            return

# Check Columns
    for i in cols:
        i.sort()
        if i != num_to_check:
            print("No")
            return

# Check sub-squares
    for i in squares:
        i.sort()
        if i != num_to_check:
            print("No")
            return       
    print("Yes")
           
check_sudoko(rows)


