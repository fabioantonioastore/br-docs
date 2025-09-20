from doctest import master

from br_docs import cpf


cpfs = [
    "11111111111",
    "28412832103",
    "21037322002"
]

for c in cpfs:
    print(c)
    c = cpf.mask(c)
    print(cpf.mask(c))
    print(cpf.is_valid(c))