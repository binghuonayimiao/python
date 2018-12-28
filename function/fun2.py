def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 4
    return damage1, damage2
a, b = damage(skill1 = 2, skill2 = 3)
print(a, b)