
#shot = 10
#beer = 5
#wine = 1

def drinking_game():
    print("Welcome to Italian Day!")
    user = input("What is your name? ")
    print("The rules are simple. Don't drink too much.")
    import random
    sobriety = 0
    shot = 0
    beer = 0
    wine = 0
    while sobriety < random.randint(89,121):
        drink = input("Choose a (s)hot, a (b)eer, or a glass of (w)ine: ")
        if drink == "s":
            sobriety += 10 
            shot += 1
            print("Your alcohol content is now",sobriety,user)
        if drink == "b":
            sobriety += 5
            beer += 1
            print("Your alcohol content is now",sobriety,user)
        if drink == "w":
            sobriety += 3 
            wine += 1
            print("Your alcohol content is now",sobriety,user)
        food = input("Choose to eat (m)eat and cheeses, (c)heese cake, or (s)alad: ")
        if food == "m":
            sobriety -= 7 
            print("Your alcohol content is now",sobriety,user)
        if food == "c":
            sobriety += 100 
            print("Your alcohol content is now",sobriety,user)
        if food == "s":
            sobriety -= 2 
            print("Your alcohol content is now",sobriety,user)
    print("//////////////////////////////////////////////////////////////////////////////")        
    print("You're shit faced",user,"and made a mess of the bathroom!")
    print("You had",shot,"shots,",beer,"beers, and",wine,"glasses of wine!")
    print("GAME OVER MAN GAME OVER")
    
drinking_game()

