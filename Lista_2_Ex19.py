# Questão 19. Problema real — Controle de estoque
# Uma pequena loja possui os produtos ["Teclado", "Mouse", "Monitor", "Notebook", "Headset"] e as respectivas quantidades [12, 25, 4, 3, 8].
# Desenvolva um programa que permita consultar um produto, alterar sua quantidade e listar os produtos com estoque inferior a 5 unidades.
# Ao final, informe qual produto possui a maior quantidade em estoque.

produtos = ["Teclado", "Mouse", "Monitor", "Notebook", "Headset"]
quantidades = [12, 25, 4, 3, 8]

print("Estoque atual:")
for produto, quantidade in zip(produtos, quantidades):
    print(f"{produto}: {quantidade} unidades")

produto_consultado = input("\nDigite o nome do produto que deseja consultar: ")

encontrado_consulta = False
for indice, produto in enumerate(produtos):
    if produto == produto_consultado:
        print(f"Consulta: {produto_consultado} tem {quantidades[indice]} unidades.")
        encontrado_consulta = True

if not encontrado_consulta:
    print(f"Produto '{produto_consultado}' não encontrado no estoque.")

produto_para_alterar = input("\nDigite o nome do produto que deseja mudar a quantidade: ")

encontrado_alteracao = False
for indice, produto in enumerate(produtos):
    if produto == produto_para_alterar:
        nova_quantidade = int(input(f"Digite a nova quantidade para {produto_para_alterar}: "))
        quantidades[indice] = nova_quantidade
        encontrado_alteracao = True

if encontrado_alteracao:
    print(f"Depois da alteração, {produto_para_alterar} agora possui {quantidades[produtos.index(produto_para_alterar)]} unidades.")
else:
    print(f"Produto '{produto_para_alterar}' não encontrado no estoque.")

print("\nProdutos com menos de 5 unidades no estoque:")
for produto, quantidade in zip(produtos, quantidades):
    if quantidade < 5:
        print(f"{produto} ({quantidade} unidades)")

maior_quantidade = quantidades[0]
produto_com_maior_estoque = produtos[0]
for indice, quantidade in enumerate(quantidades):
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        produto_com_maior_estoque = produtos[indice]

print(f"\nProduto com maior estoque: {produto_com_maior_estoque} ({maior_quantidade} unidades)")
