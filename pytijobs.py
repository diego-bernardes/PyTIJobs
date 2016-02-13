from infojobs import infojobs

cidade = input('Cidade para pesquisa(Ex.: Curitiba): ')
if cidade:
    cidade = cidade.replace(' ', '-')
else:
    print('Cidade não informada')|exit(1)
estado = input('Sigla do estado(Ex.: PR): ')
if len(estado) != 2:  print('Siga informada de forma incorreta!')|exit(1)
termo = input('Termo de busca(opcional): ')
infojobs(cidade, estado, termo)

