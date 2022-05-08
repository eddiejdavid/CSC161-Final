import random
yourPokemonHP = 20
garyPokemonHP = 20
hasPotion = True
hasGrowl = True
attackLowered = False
pokemonChoice = "-1"

while pokemonChoice != "1" and pokemonChoice != "2" and pokemonChoice != "3":
    print("==== Pick a Pokemon ====")
    print("1. Bulbasaur")
    print("2. Squirtle")
    print("3. Charmander")
    print("========================")
    pokemonChoice = input("Enter 1, 2, or 3: ")
    if pokemonChoice == "1":
        yourPokemon = "Bulbasaur"
        garyPokemon = "Charmander"
    elif pokemonChoice == "2":
        yourPokemon = "Squirtle"
        garyPokemon = "Bulbasaur"
    elif pokemonChoice == "3":
        yourPokemon = "Charmander"
        garyPokemon = "Squirtle"
    else:
        print("Invalid input")

print("========================")
print("You picked", yourPokemon)
print("Gary picked", garyPokemon)
print("========================")
print("Gary challenged you to a Pokemon Battle!")
print("You sent out", yourPokemon + "!")
print("Gary sent out", garyPokemon + "!")
print("========================")

while(yourPokemonHP > 0 and garyPokemonHP > 0):
    
    print("------------------------")
    print("| 1. Fight    2. Items |")
    print("| 3. Pokemon  4. Run   |")
    print("------------------------")
    moveChoice = input("Enter 1, 2, 3, or 4: ")

    if moveChoice == "1":
        print("------------------------")
        print("| 1. Tackle            |")
        print("|                      |")
        print("------------------------")
        attackChoice = input("Make a choice: ")
        if attackChoice == "1":
            print("========================")
            print(yourPokemon, "used Tackle!")
            if attackLowered == False:
                garyPokemonHP -= 5
            else:
                garyPokemonHP -= 3
            if garyPokemonHP > 0:
                if hasGrowl == True:
                    random.seed(a=None, version=2)
                    randomNumber = random.randint(1, 10)
                else:
                    randomNumber = 1

                if randomNumber <= 7:
                    yourPokemonHP -= 5
                    print("The opposing", garyPokemon, "used Tackle!")
                    print(yourPokemon + ":", yourPokemonHP, "HP")
                    print(garyPokemon + ":", garyPokemonHP, "HP")
                    print("========================")
                else:
                    hasGrowl = False
                    attackLowered = True
                    print("The opposing", garyPokemon, "used Growl!")
                    print(yourPokemon + "'s attack has been lowered!")
                    print(yourPokemon + ":", yourPokemonHP, "HP")
                    print(garyPokemon + ":", garyPokemonHP, "HP")
                    print("========================")
        else: 
            print("Invalid choice")

    elif moveChoice == "2":
        if hasPotion == True:
            print("------------------------")
            print("| 1. Potion            |")
            print("|                      |")
            print("------------------------")
            itemChoice = input("Make a choice: ")
            if itemChoice == "1":
                print("========================")
                print("You used a potion!")
                print("Your ", yourPokemon + "'s HP has been increased by", 20 - yourPokemonHP, "!")
                yourPokemonHP = 20
                hasPotion = False

                if garyPokemonHP > 0:
                    if hasGrowl == True:
                        random.seed(a=None, version=2)
                        randomNumber = random.randint(1, 10)
                    else:
                        randomNumber = 1

                    if randomNumber <= 7:
                        yourPokemonHP -= 5
                        print("The opposing", garyPokemon, "used Tackle!")
                        print(yourPokemon + ":", yourPokemonHP, "HP")
                        print(garyPokemon + ":", garyPokemonHP, "HP")
                        print("========================")
                    else:
                        hasGrowl = False
                        attackLowered = True
                        print("The opposing", garyPokemon, "used Growl!")
                        print(yourPokemon + "'s attack has been lowered!")
                        print(yourPokemon + ":", yourPokemonHP, "HP")
                        print(garyPokemon + ":", garyPokemonHP, "HP")
                        print("========================")
        else:
            print("========================")
            print("You have no items!")
            print("========================")

    elif moveChoice == "3":
        print("========================")
        print("You only have", yourPokemon + "!")
        print("========================")

    elif moveChoice == "4":
        print("========================")
        print("You can't run from a trainer battle!")
        print("========================")

if garyPokemonHP <= 0:
    print("The opposing", garyPokemon, "has fainted!")
    print("You win!")
    print(yourPokemon, "gained 30 exp!")
    print("Gary paid you $100!")

else:
    print(yourPokemon, "has fainted!")
    print("You pay Gary $100")

quit = input("Press enter to quit")