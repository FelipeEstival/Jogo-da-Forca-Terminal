import random

palavras_jogo = ["computador", "teclado", "internet", "programa", "algoritmo", "variavel", "funcao", "sistema", "arquivo", "memoria", "software", "hardware", "banco", "servidor", "linguagem", "codigo", "projeto", "rede", "dados", "usuario", "login", "senha", "seguranca", "aplicativo", "debug", "terminal", "compilador", "logica", "classe", "objeto"]

lista = []
palavra = palavras_jogo[random.randint(1,30)].strip().upper()

print("O JOGO COMEÇOU!!")
print(" ")

for i in palavra:
    lista.append('-')   
print("".join(lista))

tentativas = 5

while True:
    if tentativas == 0:
        print("VOCÊ PERDEU")
        break
    if palavra == "".join(lista):
        print("VOCÊ ACERTOU A PALAVRA")
        break
    
    letra_adivinha = input("Tente acertar uma letra:").upper()
    if letra_adivinha in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra_adivinha:
                lista[i] =  letra_adivinha
        print("".join(lista))
        
    elif letra_adivinha not in palavra:
        print(f"Você ERROU, agora tem apenas {tentativas} tentativas...")
        tentativas = tentativas - 1
    
