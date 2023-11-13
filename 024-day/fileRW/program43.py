#In this section we are learning basic file operations
#Once we open the file we need to close the file. Becuase when we open a file program will asccess some resources.
#So we need to free or release the resources. So we need to close the file.

# file = open("/my_file.txt")
# content = file.read()
# print(content)
# file.close()

#We can open the file in  a different way
#In this we don't want to close the file
with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)
    
#For write some thing to a file we can use the write method
#By default file open in read mode so we need to exclusively define the mode as write
#Please find the example below
with open("my_file.txt", "w") as file:
    # content = file.read()
    # print(content)
    file.write("Hello, my name is Anu")
    # content = file.read()
    # print(content)
    
#when we give 'a' mode it will append the file `r+` the we can read and write.
# We only give `w`, file will overwrite