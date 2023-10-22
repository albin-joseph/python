# In this section we are going to learn more about the function with outputs

def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"

full_name = get_full_name("Albin", "Joseph")
print(full_name)

def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"

formatted_name = format_name("albin", "joseph")
print(formatted_name)