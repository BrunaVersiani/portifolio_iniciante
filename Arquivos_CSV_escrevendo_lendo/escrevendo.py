import csv
import pandas as pd
dados = {"Nome" : ["Bruna", "Lucas", "Gustavo", "Rafaela", "Maria", "Joana", "Nicolas", "joão", "José"],
         "Idade" : [30, 32, 45, 80, 56, 12, 10, 35, 77]}
dados = pd.DataFrame(dados)
dados.to_csv("data.csv", index = False)
print(dados)

#Como escrever dados e salvar como CSV

'''Os arquivos CSV são utilizados para importar e exportar conjuntos de dados, por consumir um espaço menor na memória comparado a um arquivo Excel.'''