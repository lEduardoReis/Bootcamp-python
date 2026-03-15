#%%
opcao = int(input("Escolha uma opção: \n1 - Água Mineral \n2 - Água com Gás"))

conta = 0
if opcao == 1:
    conta = 1.50
elif opcao == 2:
    conta = 2.00

if conta == 0:
    print("Entre com a porra da opção correta, com todo o respeito")
else:
    print(f"O valor da sua conta é R${conta:.2f}")
# %%
