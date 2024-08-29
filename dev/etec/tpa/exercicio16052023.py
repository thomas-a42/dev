# while dentro do outro
# linhas x colunas
# a cada linha (while externo) roda 5 vezes a coluna (while interno)

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

