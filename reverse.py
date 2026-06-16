word = "A Man, a plan, a canal: Panama"
rev =""
for i in word:
    rev = i + rev
if rev == word:
    print("Palinodrome")
else:
    print("No")