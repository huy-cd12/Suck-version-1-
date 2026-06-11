

import random

hero_hp = 200
mons_hp = 1000
count = 0
hero = "hero"
mons = "monster"
hit_hero = [42, 56, 78, 100]
hit_mons = [10, 22, 13,]

print('who gonna first?')
turn = input().strip().lower()

while turn != hero and turn != mons:
    print("wrong input")
    turn = input().strip().lower()

while hero_hp > 0 and mons_hp > 0:
    count += 1
    print(f"\nTurn {count}")
    
    if turn == hero:
        dmg = random.choice(hit_hero)
        print(f"Hero deal {dmg}")
        mons_hp -= dmg
        
        if mons_hp <=0:
            print()
            print("monster = 0")
            print("monster lose")
            break
        
        print(f"Monster's hp {mons_hp}")
        turn = mons
        
    elif turn == mons:
        dmg = random.choice(hit_mons)
        print(f"Monster deal {dmg}")
        hero_hp -= dmg

        if hero_hp <= 0:
            print("----------------------")
            print("Hero = 0")
            print("Hero lose")
            break
        
        print (f"hero's hp {hero_hp}")
        turn = hero


    print("----------------------")

