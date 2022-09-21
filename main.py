# Программа должна вывести первые n строк треугольника Паскаля, каждую на отдельной строке

def pascal(row_numb):
    l = []
    if row_numb == 0:
        l = [1]
    elif row_numb == 1:
        l = [1, 1]
    else:
        prev_l = pascal(row_numb-1)
        l.append(1)
        for i in range(len(prev_l) - 1):
            l.append(prev_l[i] + prev_l[i+1])
        l.append(1)
    print(*l)
    return l

n = int(input())
print(1)
if n > 1:
    pascal(n - 1)
