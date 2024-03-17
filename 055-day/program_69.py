## Advanced python decorator function

class User:
    def __init__(self, name) -> None:
        self.name = name
        self.is_logged_in = False
    
    def is_authenticated_decorator(function):
        def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function()
    return wrapper()
    
@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s ne blog post")
        
       
new_user = User("albin")
new_user.create_blog_post(new_user)