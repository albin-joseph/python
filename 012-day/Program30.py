#In this section we are going to learn more about Scope
#Local scope inside the function 

def localScope():
    value = 1
    print(value)
    
localScope()
##print(value) This make error

#Global scope

player_health = 10

def get_player_health():
    player_health = 12#This is a local variable
    
get_player_health()
print(player_health)

#There is no Block Scope in python

#How to global scope modify in function
#We are using return statement for this

enemies = 1

def increase_enemies():
    print(f"inside fn enemies: {enemies}")
    return enemies + 1
    
enemies = increase_enemies()
print(f"Outside fn enemies: {enemies}")

#Global constants. We declate in capita case
PI = 3.16
URL = "http://www.google.com"