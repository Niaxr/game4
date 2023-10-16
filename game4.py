def attack_enemy(self, enemy):
    damage = max(0, self.attack - enemy.defense)
    enemy.take_damage(damage)
    # Calculate enemy damage to the player and apply it
    enemy_damage = max(0, enemy.attack - self.defense)
    self.take_damage(enemy_damage)
    return damage
