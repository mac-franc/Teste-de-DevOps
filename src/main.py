def get_full_name(first_name, last_name):
    return f"{first_name.title()} {last_name.title()}"


def get_age(age):
    return str(age)


print(get_full_name("john", "doe"))
print(get_age(24))
