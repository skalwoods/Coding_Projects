
# Brian Ocque - Portals Class
## This program is supposed aid in the choosing of floors 
#for widget testing.

def main():
    drop_widget()

def drop_widget():
    # Simulate dropping a widget from a certain floor
    highest_safe_floor = 50  # Change this to the actual highest safe floor
    floor = input('What is the starting floor: ')
    if floor <= highest_safe_floor:
        return False  # Widget didn't break
    else:
        return True  # Widget broke

def find_highest_floor():

    lower_bound = 1
    upper_bound = 100

    while lower_bound < upper_bound:
        midpoint = (lower_bound + upper_bound) // 2
        user_input = input(f"Did the widget break when dropped from floor {midpoint}? (y/n): ")
        if user_input.lower() == 'y':
            upper_bound = midpoint - 1
        else:
            lower_bound = midpoint + 1
            best_guess = lower_bound
    return best_guess

highest_floor = find_highest_floor()
print("The highest floor where the widget doesn't break is:", highest_floor)

main()