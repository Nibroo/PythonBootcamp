artist = {
    "first": "Neil",
    "last": "Young",
}
#full_name = f"{artist['first']} {artist['last']}"

full_name = artist['first'] + ' ' + artist['last']
print(full_name)
#?------------------------------------------------------------------------------

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
#total_donations = sum(donations.values())

total_donations = 0
for k,v in donations.items():
    total_donations += v

print(total_donations)
#?------------------------------------------------------------------------------

from random import choice

food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])
print(f'Do you have {food}?')

bakery_stock = {"almond croissant" : 12,"toffee cookie": 3,"morning bun": 1,"chocolate chunk cookie": 9,"tea cake": 25}

if food in bakery_stock:
    print(f'{bakery_stock[food]} left')
else:
    print("We don't make that")
#?------------------------------------------------------------------------------

game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]

initial_game_state = {}.fromkeys(game_properties,0)
print(initial_game_state)
#?------------------------------------------------------------------------------

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
stock_list = inventory.copy()
print(stock_list)

stock_list['cookie'] = 18
print(stock_list)

stock_list.pop('cake')
print(stock_list)
#?------------------------------------------------------------------------------

parity = {num: ('even' if num%2==0 else 'odd') for num in range(1,101)}
print(parity)