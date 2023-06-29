def arrange_coins(n):
    complete_rows = 0
    total_coins = 0
    row = 1

    while total_coins + row <= n:
        complete_rows += 1
        total_coins += row
        row += 1

    return complete_rows
n = 5

complete_rows = arrange_coins(n)
print(complete_rows)  