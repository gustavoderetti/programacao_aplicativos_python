nomes =["ana", "carlos", "joao", "maria"]
print(nomes)


print(nomes[0])
print(nomes[1])

print(nomes[-1])

nomes[0] = "Pedro"
print(nomes)

nomes.append("Lucas")
print(nomes)

nomes.insert( 1, "Mariana")
print(nomes)

nomes.remove("Lucas")
print(nomes)

nomes.pop(0)
print(nomes)