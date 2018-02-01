level = 1
xp = 1
lvl_next = 25

p_str = 0
p_dex = 0
p_int = 0

while xp >= lvl_next:
    level += 1
    xp -= lvl_next
    lvl_next = round(lvl_next * 1.5)

print("Level: ", level)
print("XP Needed: ", lvl_next)
print("Next Level: {}%".format(int((xp / lvl_next) * 100)))
