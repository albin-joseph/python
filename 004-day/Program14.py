#In this section we are going to learn about multilevel/ nested lists.
#It's basically list inside another list

fruits = ["apple", "avacado", "orange"]
vegitables = ["cabage", "cucumber", "carrot"]

veg_n_fruit = [vegitables, fruits]

print(veg_n_fruit)
print(f"fruits: {veg_n_fruit[1]}")
print(veg_n_fruit[1][1])


#Below a simple game; place an entered string in a multilevel list
row1 = ["-", "_", "_"]
row2 = ["-", "_", "_"]
row3 = ["-", "_", "_"]

print(f"{row1}\n{row2}\n{row3}\n")
