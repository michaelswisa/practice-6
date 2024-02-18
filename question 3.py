# כתוב מחרוזת כלשהי במשתנה. קלוט אות מהמשתמש והדפס את מספר את המחרוזת עד האות שבחר
# המשתמש - ועד בכלל.
# למשל: המחרוזת היא "שלום" והמשתמש בחר "ו" יודפס "שלו"


a = "hello world"
print(a)
b = input("Select a letter from the string\n")
if b in a:
    b = a.index(b) + 1
    print(a[:b])
else:
    print("Inserting a letter that does not exist")
