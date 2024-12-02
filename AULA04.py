# # TRUQUES COM PYTHON
# Numero = 0 
# Numero = 5

# # avançar uma casa a frente com INT
# Numero+=1
# Numero = Numero+1

# #Avanço utilizando outra variavel
# Avancar = 3
# Numero = Numero+Avancar
# VarivavelNova = Numero+Avancar

# #Recorte de String
# String_ = "AlunoEAluna"
# String_[4:]
# String_[:4]
# String_[1:6]

# #Conversão de string para lista
# ListaDeNomes = "Luana;Raphael;Natalia;Lucas"
# ListaDeNomes = ListaDeNomes.split(";")
# print(ListaDeNomes[0])



# Taxa  = 0.2
# for T in range(0,10):
#   print("Executou"+str(T)) 
#   Taxa = Taxa*1,2
# print(Taxa) 

# Valores = [2,5,6,7,8]
# for ValorTemporario in Valores:
#     print(ValorTemporario+4)

# Quantidade = 0
# while Quantidade < len(Valores)-1:
#      print(Valores[Quantidade]+4)
#      Quantidade+=1


# for ComData in range(0,len(Valores)-1):
#     print(ComData+4)

#Crie um laço de repetição que faça 8 repetições
#e a cada repetição adicione +2 na variavel "Escala"
#e a cada iteração adiciona o valor modificado na lista 
#ValorEScala"

Escala = 2
ValoresEscala = []
for Temp in range(1,8):
    Escala+=2
    ValoresEscala.append(Escala+2)

print(ValoresEscala)