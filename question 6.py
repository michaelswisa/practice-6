# הגדר רשימה של מספרים. החלף כל שני איברים צמודים ברשימה.


x = [1, 2, 3, 4, 5, 6]
print(x)
b = x[0:] = x[1], x[0], x[3], x[2], x[5], x[4]
print(b)