#In this section we are going to learn more about Scope
#Local scope inside the function or inside block of code

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

