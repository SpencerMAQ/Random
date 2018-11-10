import random

num_simulations = 100000

num_times_right = 0

# switch choices or nay?
switch_bool = False

for i in range(num_simulations):
    doors = ['car', 'goat', 'goat']

    random.shuffle(doors)

    first_choice = random.choice(doors)
    first_choice_index = doors.index(first_choice)

    # the two remaining items can be car, goat or goat, goat
    doors.pop(first_choice_index)

    # switch gate
    if switch_bool:
        # remaining goat/s index, only get one
        remaining_goat_index = doors.index('goat')

        doors.pop(remaining_goat_index)

        if doors[0] == 'car':
            num_times_right+=1

    else:
        if first_choice == 'car':
            num_times_right+=1

pct_correct = (num_times_right/num_simulations)*100
print(pct_correct)
