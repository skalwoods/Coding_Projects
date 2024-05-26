#THis is a program used to calculate how many trees would cover a walmart floor

def welcome():
    print('==============================')
    print('====TREE PROBLEM CALCULATOR===')
    print('==============================')
    print()
    print('A common material used in linoleum tile production is wood flour, which is cellulose pulp from trees.') 
    print('Our task is to find out how many trees it would take to make enough pulp to tile a Walmart Floor')
    print('Enter the square FEET of the floor into the first prompt, then the length and width of the tile you want to use.')
    print('The result will be the number of trees used to make enough cellulose to cover that floors area.')
    print()
    print()

def main():

    #Calculate the number of tiles that would go in a given floor space. This function will convert the inputted footage to inches

    floor_space = int(input('How many feet is the floor?'))
    length = float(input('What is the tile length in inches?'))
    width = float(input('What is the tile width in inches?'))
    tile_size_inches = length * width
    converted_floor_footage = floor_space * 12
    number_of_tiles = converted_floor_footage / tile_size_inches

    # Calculate how much wood flour would be present for the total number of tiles used
    wood_flour_per_tile = .18
    total_wood_flour = wood_flour_per_tile * number_of_tiles

    #Calculate how many trees that total wood flour would consume. Converting inches back to feet here also
    trees_used = (total_wood_flour * 12) / 250
    print()
    print()
    print('The number of trees needed to complete the job would be',trees_used)





welcome()
main()