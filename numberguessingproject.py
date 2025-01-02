import random
lower_bound=1
upper_bound=100
chances=7
no_to_guess=random.randint(lower_bound,upper_bound)
guess_count=0
while(guess_count<chances):
    user_input=int(input("enter the number to guess:"))
    if no_to_guess<user_input:
        guess_count=guess_count+1
        print("your guess is too high.Plz select low no.")
    elif no_to_guess>user_input:
        guess_count=guess_count+1
        print("your guess is too low ,plz select high no.")
    elif no_to_guess==user_input:
        print("you have catched right guess,Congratulations!")
        break
    
    if guess_count==chances and no_to_guess!=user_input:
        print("your chances have been finished t,The correct number was:",no_to_guess)


