def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def get_age(age):
    age = age.title() + " "
    return age


print(get_full_name("john", "doe"))
print(get_age("22"))