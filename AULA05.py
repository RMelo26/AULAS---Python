import os

# Nosso estoque
ListaProdutos = [None,"Caderno","Lapis","Borracha"]
PrecoProdutos = [None,2.00,0.90,None]
Bandeira = "continue"
Carrinho = []

while Bandeira == "continue":
    os.system("cls")
    
    print("Produtos disponiveis")
    for i in range(len(ListaProdutos)):
        #print(f"{str(i)}. {ListaProdutos[i]}")
        # ou 
        if ListaProdutos[i] != None:
            print(str(i)+". "+ListaProdutos[i])

    #Pergunta ao cliente
    Decisao = int(input("Qual produto deseja comprar? >"))
    if Decisao == 0:
        Bandeira = "Parar"
        
    else:
        # Mostrando / adicionando ao carrinho
        print("Você adicionou: "+ListaProdutos[Decisao])
        Carrinho.append(ListaProdutos[Decisao])

# Listar os produtos que o usuario já comprou
print("Produtos já comprados: ")
Produtos_ja_avaliados =[]
for ProdutoCliente in Carrinho:
    Contador = 0 

    if ProdutoCliente in  Produtos_ja_avaliados:
        continue
    
    if  ProdutoCliente not in Produtos_ja_avaliados:
        Produtos_ja_avaliados.append(ProdutoCliente)
    

    for x in Carrinho:
        if x == ProdutoCliente:
            Contador+=1
    print("Comprou "+str(Contador)+" "+ProdutoCliente)

ValorTotal = 0.0
for i in Carrinho:
    for a in range(len(ListaProdutos)):
        if i == ListaProdutos[a]:
           if PrecoProdutos[a] != None:
             ValorTotal = ValorTotal + PrecoProdutos[a]

print("O valor total da sua compra ficou em: ")
print(ValorTotal)
