

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


while hero_hp > 0 and mons_hp > 0:
    count += 1
    if turn == hero:
        
        print (f"turn {count}") 
        dmg = random.choice(hit_hero)
        print (f"hero deal {dmg} ")
        mons_hp -= dmg

        if mons_hp > 0:
              print(f"hp's monster: {mons_hp}")
              print("----------------------")
              print (f"turn {count}")
              dmg = random.choice(hit_mons)
              print (f"monster deal {dmg} ")
              hero_hp -= dmg
              print(f"hp's hero: {hero_hp}")

        else:
             print("monster lose")
             break

            
    elif turn == mons:
            
            print (f"turn {count}") 
            dmg = random.choice(hit_mons)
            print (f"monster deal {dmg} ")
            hero_hp -= dmg
            

            if hero_hp > 0:
                 print(f"hp's hero: {hero_hp}")
                 print("--------------------")
                 dmg = random.choice(hit_hero)
                 print (f"hero deal {dmg} ")
                 mons_hp -= dmg
                 print(f"hp's monster: {mons_hp}")   
            else:
                 print("hero lose")
                 break

    else:
        print("wrong input")
        while True:
            turn = input().strip().lower()
            if turn == hero or turn == mons:
                 break
            else:
                 print("wrong input")
            

    if hero_hp <=0 or mons_hp <= 0:
        break    
    


