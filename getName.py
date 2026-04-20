def get_full_name(first_name, last_name):
    full_name = f"{first_name.title()} {last_name.title()}"
    return full_name


def get_age(age):
    return str(age)


print(get_full_name("john", "doe"))
print(get_age(24))