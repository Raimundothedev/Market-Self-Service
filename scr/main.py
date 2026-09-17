from database.database import *

opcao = input("Digite uma opcao: ")
match opcao:
    case "1":
        name = input("Digite o nome do produto: ")
        price = float(input("Digite o preço do produto: "))
        amount = int(input("Digite a quantidade do produto: "))
        add_product(name, price, amount)
    case "2":
        id = input("Digite o id do produto que irá deletar: ")
        remove_product(id)

