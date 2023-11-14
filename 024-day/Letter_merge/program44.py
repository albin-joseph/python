import os

PLACEHOLDER = "[name]"

with open(f"{os.getcwd()}/024-day/Letter_merge/input_files/names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
with open(f"{os.getcwd()}/024-day/Letter_merge/input_files/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"{os.getcwd()}/024-day/Letter_merge/output_files/ready_to_send/letter_to_{name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)