

import random

hero_hp = 200
mons_hp = 1000
count = 0

hit_hero = [42, 56, 78, 100]
hit_mons = [10, 22, 13,]

print('who gonna first?')
turn = input()

while hero_hp > 0 and mons_hp > 0:
    if turn == "hero":
        dmg = random.choice(hit_hero)
        print(f"hero deal {dmg}")
        mons_hp -= dmg
        print(f"mau cua monster {mons_hp}")
        
        if mons_hp <= 0:
            print("monster lose")

        dmg = random.choice(hit_mons)
        print(f"monster deal {dmg}")
        hero_hp -= dmg
        print(f"mau cua hero {hero_hp}")
        
        if hero_hp <= 0:
            print("hero lose")    
    
        

    else:
        dmg = random.choice(hit_mons)
        print(f"monster deal {dmg}")
        hero_hp -= dmg
        print(f"mau cua hero {hero_hp}")
        
        if hero_hp <= 0:
            print("hero lose")
        
        dmg = random.choice(hit_hero)
        print(f"hero deal {dmg}")
        mons_hp -= dmg
        print(f"mau cua monster {mons_hp}")
        
        if mons_hp <= 0:
            print("monster lose")

    
    
    if mons_hp <= 0 or hero_hp <= 0:
        break

    count += 1
    print (f"turn {count}")

        






