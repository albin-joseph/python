import random
#In this section we are learning the randomisation in Python

random_int = random.randint(1, 10)

print(random_int)

#As like any program we can modulise the program for different purpose and import in other modules and
#programs we can use the function or methods defined in that module.

import my_reusable_module

print(my_reusable_module.pi)

# Head or tail program

random_side = random.randint(0, 1)

if random_side == 0:
    print("Head")
else:
    print("Tail")
