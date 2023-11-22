#In this section we are going to learn about errors, exceptions and save JSON data
try:
    file = open ("x_file.txt")
    a_file_data = file.readline()
    a_dict = {"key": "Value"}
    print(a_dict["ksdd"])
except FileNotFoundError:
    file = open("x_file.txt", "w")
    file.write("Write from except")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")