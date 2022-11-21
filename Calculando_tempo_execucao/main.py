from time import time, sleep
inicio = time()

def decoração():
    print(f'\33[35m*-' * 15)


decoração()
palavra = "Artificial Intelligence"
texto = palavra.split()
a = " "
for i in texto:
    a = a+str(i[0]).upper()
print(a)

#Teste para saber se o tempo esta sendo respeitado
#sleep(2)

fim = time()
tempo_execucao = fim - inicio
print("Execution Time : ", tempo_execucao)
decoração()

'''Esse código é simples, porem pode ser muito util para calcular o tempo de um grande projeto, levando em consideração
 o melhor código o que levar o menor tempo de execução.'''