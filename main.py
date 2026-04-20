"""Programa para formatar nome e idade."""


def get_full_name(first_name, last_name):
    """Retorna o nome completo formatado."""
    return f"{first_name.title()} {last_name.title()}"


def get_age(age):
    """Retorna a idade em formato texto."""
    return str(age)


print(get_full_name("john", "doe"))
print(get_age(24))
