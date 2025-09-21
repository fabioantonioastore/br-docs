from br_docs import cpf


cpfs = ["11111111111", "28412832103", "21037322002"]

for c in cpfs:
    print(c)
    c = cpf.mask(c)
    print(cpf.mask(c))
    print(cpf.is_valid(c))
    new_cpf = cpf.generate()
    print(new_cpf)
    print(cpf.is_valid(new_cpf))
    for i in cpf.gen_generate():
        print(i)
        print(cpf.is_valid(i))
