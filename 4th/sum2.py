def sum(total, arr):
    total += arr.pop(0)
    if len(arr) == 0:
        return(total) 
    else:
        return sum(total, arr)

print(sum(0, [1, 2, 3, 4]))
