#%%

soma = 0 # valor final.
qtd_entrada = 4 # o contador das entrada.

while qtd_entrada >0:
    altura = float(input("Digite a altura da pessoa: "))
    soma += altura
    qtd_entrada -= 1
print("A soma das alturas é:", soma)
# %%
