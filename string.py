def quantidade(palavra):
    # a função .count conta a quantidade de vezes que um elemento aparece em uma string. Como usei .lower no input, todas as letras 'a' 
    # estão minúsculas, independentemente de como o usuário digitou
    contador = palavra.count("a")
    return contador

palavra = input("digite uma palavra: ").lower()
output = quantidade(palavra)
print(f"a quantidade de vezes que a letra 'A' aparece é: {output}")
