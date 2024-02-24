alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]
output = []
# Inserir um input numerico
palavra = str(input("Digite a chave: "))
# Obter input de frase a cifrar
frase = str(input("Digite a frase a decifrar: "))
val=0

# Array para ver todas as letras da frase e cifrar consoante o numero dado, fazendo a (posicao da letra a cifrar no
# alfabeto) - o numero obtido de forma a termos a posição da letra cifrada e devido resultado
for letra in frase.upper():
    if letra in alfabeto:
        if val > len(palavra) - 2:
            val = 0
        else:
            val = val + 1
        word = palavra[val].upper()
        if (alfabeto.index(letra) + alfabeto.index(word)) > 26:
            output.append(alfabeto[(alfabeto.index(letra) - alfabeto.index(word)) - 26])
        else:
            output.append(alfabeto[(alfabeto.index(letra) - alfabeto.index(word))])
    elif letra == " ":
        output.append(" ")

# Juntar todos os carateres do array do output de forma a criar a frase
print("".join(output))
