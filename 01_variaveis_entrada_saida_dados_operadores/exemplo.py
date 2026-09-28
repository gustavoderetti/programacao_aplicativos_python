# 1. Estrutura Condicionais

nota = 6

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# 2. Condicionais e Operadores Lógicos
# and -> Todas as condições devem ser verdadeiras
# or -> Pelo menos uma condição deve ser vervadeira
# not -> inverte o resultado

idade = 20
ingresso = True

if idade >= 18 and ingresso:
    print("Entrada Permitida")
else:
    print("Entrada não permitida")

# 3. Estrutura de Repetição while
contador = 1
while contador <= 5:
    print(contador)
    contador +=1

# 4. Estrutura de repetição for
for numero in range(1, 6):
    print(numero)

# 5. percorrendo uma lista
nomes = ["ana", "Carlos", "joão", "maria"]
for nome in nomes:
    print(nome)

    # 6. Break, continue, pass
    for numero in range(1, 11):
        if numero == 6:

print(numero)
# break
# continue
# pass
print(numero)

#7. Percorrendo uma lista
    for nome in nomes:
        print(nome)

#8. Verificando se um elemento existe
    if "joao" in nomes:
        print("Joao esta na lista")
    else:
        print("Joao esta na lista")

#10. lista de numeros
notas = [7.5, 8.0, 6.5, 9.0]
soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas)
print(f"Media: {media:.1f}")


