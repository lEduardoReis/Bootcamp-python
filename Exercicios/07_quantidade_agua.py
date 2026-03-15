#%%
opcao = int(input("Escolha uma opção: \n1 - Água Mineral \n2 - Água com Gás"))
quantidade = int(input("Digite a quantidade de garrafas: "))

valor_item = 0
if opcao == 1:
    valor_item = 1.50
elif opcao == 2:
    valor_item = 2.00

if valor_item == 0:
    print("Entre com a porra da opção correta, com todo o respeito")

else:
    quantidade_total = valor_item * quantidade
    print(f"O valor total é: R$ {quantidade_total:.2f}")
# %%
