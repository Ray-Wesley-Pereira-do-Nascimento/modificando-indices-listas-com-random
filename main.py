from random import  randint

def impar_par(tam):
    vetF = []
    for i in range(tam):
      if i %  2 == 0:
        vetF.append(randint(0, 100))
      else:
        vetF.append(i*2)
    return vetF

tamanho = int(input("Digite o tamanho da lista: "))
x = impar_par(tamanho)
print(x)


