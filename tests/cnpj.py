from br_docs import cnpj


cnpjs = [
    "11444777000161",
    "10298312031283"
]

for c in cnpjs:
    print(cnpj.is_valid(c))
    c = cnpj.mask(c)
    print(c)
    print(cnpj.remove_mask(c))
    c = cnpj.generate()
    print(c)
    print(cnpj.mask(c))
    print(cnpj.is_valid(c))
