alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]
output = []
# Inserir um input numerico
chave = int(input("Digite o valor da chave: "))
# Obter input de frase a cifrar
frase = str(input("Digite a frase a decifrar: "))

for letra in frase.upper():
    if letra in alfabeto:
        if (alfabeto.index(letra) + chave) >= len(alfabeto):
            output.append(alfabeto[(alfabeto.index(letra) + chave) - 26])
        else:
            output.append(alfabeto[(alfabeto.index(letra) + chave)])
    elif letra == " ":
        output.append(" ")

print("".join(output))
