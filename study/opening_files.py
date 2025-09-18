with open("poetry_expl.txt") as poetry_file:
    poetry = poetry_file.read()

print(poetry)

"""
or use
poetry = poetry_file.readlines()
print(poetry)
"""
for line in poetry.splitlines():
    print(f"{line}\n")


print(poetry.replace("life", "nice"))
