#decorator function is a function which run another function and return the result
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before function
        function()
        #Do something after function
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")
    
@delay_decorator
def say_bye():
    print("Bye")

def say_greetings():
    print("How are you")
    
say_hello()

