# Categorias Registradas

Categorias = ["Eletronicos", "Brinquedos", "Casa"]



#Variaveis de compras

CumpomDesconto = False

ValorCompra = 0.0

Carrinho = []

#Produtos cadastrados

    # Dicionario "marca","Preço","Categoria"

Produtos = {"Computador":["Acer AMD",2050,"Eletronicos"],"Jogo de Tabuleiro":["Dixit", 169.80,"Brinquedos"], "Sanduicheira Elétrica":["Cadence Click", 89.90, "Casa"]}




def CalculoDeImpostos(Categoria):

    """

        Calculadora de impostos para cada categoria:

            Categoria: Parametro para saber como será calculado o imposto

    """

    if Categoria == "Eletronicos":

        print("Descontos Aplicados!")

        return 450*2
    if Categoria == "Brinquedos":

        print("Descontos Aplicados!")

        return 300*2
    
    if Categoria == "Casa":

        print("Descontos Aplicados!")

        return 250*2



def DescontosProdutos(Categoria,Quantidade):

    """

        Caculo de cada Desconto por categoria e por quantidade

            Categoria: Qual Categoria vai ser analisada

            Quantidade: Quantos itens o cliente esta comprando

    """

    if Categoria == "Eletronicos" and Quantidade >=2:

        return 200.20
    if Categoria == "Brinquedos" and Quantidade>=3:
        return 50
    if Categoria == "Casa" and Quantidade>=2:
        return 20
   

def AdicionarCarrinho(Item,Quantidade):

    """

        Função que armazena a compra do usuario:

            Item: qual Item deseja aplicar ao carrinho

            Quantidade: Quantidade Comprada daquele item

    """

    return Carrinho.append(f"{Item} {str(Quantidade)}")

   




def SistemaCalculoFinanceiro():

    # Crie o seu codigo Aqui!!

    print("SISTEMA DE COMPRAS PARA E-Comerce!")
    Escolher_produto = input("Qual produto você deseja comprar?")
    Quantidade_escolhida = input("Quantos você vai levar?")
    ValorCompra=Produtos[Escolher_produto][1]*int(Quantidade_escolhida)

    print(f"O Valor da Compra deu:{ValorCompra} Deseja Continuar?")
    if input("Sim para continuar") == "Sim":
        AdicionarCarrinho (Produtos[Escolher_produto][0],Quantidade_escolhida)
    
    else:

        print("Compra Cancelada")

        return ValorCompra






while True:

    if SistemaCalculoFinanceiro() == 0.0:

        print("O usuario não comprou nenum item 😢")

    else:

        print(f"Carrinho do usuario 🛒")

        for i in Carrinho:

            print(i)
