
with open('passwords.txt') as f:
    plines = f.read()
    f.close
with open('usernames.txt') as f:
    ulines = f.readlines()
    f.close
print(ulines)
def checkUser():
    for val in ulines:
        if val=="cultiris":
            print(val)

checkUser()
