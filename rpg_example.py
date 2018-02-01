level = 1
xp = 1
lvl_next = 25

strength = 0
dex = 0
int = 0

while xp >= lvl_next:
    level += 1
    xp -= lvl_next
    lvl_next = round(lvl_next * 1.5)

print("Level: ", level)
print("Next: ", lvl_next)
print("Next Level: {}%".format(int((xp / lvl_next) * 100)))


