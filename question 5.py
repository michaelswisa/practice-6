# נתונה רשימה של מספרים. הדפס את כל המספרים את כל המספרים מחצי הרשימה האחרונה בסדר הפוך
# ואת תחילת הרשימה בסדר רגיל.


a = list("123456")
print(a[0:3] + a[:2:-1])
