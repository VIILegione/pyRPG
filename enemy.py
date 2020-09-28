class Enemy:
    name: str
    health: int
    armorClass: int
    damage: int
    weaponMinDamage: int
    weaponMaxDamage: int
    experienceAmount: int


class Goblin(Enemy):
    name = "Goblin"
    health = 10
    armorClass = 10
    damage = 2
    weaponMinDamage = 1
    weaponMaxDamage = 4
    experienceAmount = 100


class Cobold(Enemy):
    name = "Cobold"
    health = 8
    armorClass = 12
    damage = 2
    weaponMinDamage = 1
    weaponMaxDamage = 4
    experienceAmount = 100


class Wolf(Enemy):
    name = "Wolf"
    health = 12
    armorClass = 12
    damage = 2
    weaponMinDamage = 1
    weaponMaxDamage = 6
    experienceAmount = 100


enemyList = [Goblin(), Cobold(), Wolf()]
