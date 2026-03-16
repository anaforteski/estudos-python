print("Digite três nomes para serem ordenados em ordem alfabetica")
nome1 = input("Nome 1\n")
nome2 = input("Nome 2\n")
nome3 = input("Nome 3\n")

if nome1<nome2 and nome1<nome3:
    if nome2<nome3:
        print(nome1, nome2, nome3)
    else:
        print(nome1, nome3, nome2)

if nome2<nome1 and nome2<nome3:
    if nome1<nome3:
        print(nome2, nome1, nome3)
    else:
        print(nome2, nome3, nome1)
if nome3<nome1 and nome3<nome2:
    if nome1<nome2:
        print(nome3, nome1, nome2)
    else:
        print(nome3, nome2, nome1)