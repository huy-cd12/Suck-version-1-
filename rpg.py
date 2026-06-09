

import random

Hero = "Hero"
Monster = "Monster"
hero_hp = 200
mons_hp = 1000
hp_hero_current = 0
hp_mons_current = 0
count = 0

hit_hero = [42, 56, 78, 100]
hit_mons = [10, 22, 13,]




while hero_hp > 0 or  mons_hp >0 :
    action = random.choice([Hero, Monster])

    if action == Hero:
        print("Hero turn")
        dmg_hero = random.choice(hit_hero)
        hp_mons_current = mons_hp - dmg_hero
        mons_hp = hp_mons_current
                
    else: 
        print("Monster turn")
        dmg_mons = random.choice(hit_mons)
        hp_hero_current = hero_hp - dmg_mons
        hero_hp = hp_hero_current
    
    


    count += 1
    if count >= 1:
        print(f"turn {count}")

    if mons_hp <= 0 or hero_hp <= 0:
        break