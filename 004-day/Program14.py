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
list = [row1,row2,row3]
print(f"{list[0]}\n{list[1]}\n{list[2]}\n")

row_position = int(input("Which row select to place your text? "))
column_position = int(input("Which column select to place your text? "))
text = input("Enter text you wish to place in the position: ")

list[row_position-1][column_position-1] = text

print(f"{list[0]}\n{list[1]}\n{list[2]}\n")
