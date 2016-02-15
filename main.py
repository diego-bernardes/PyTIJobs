from sites import InfoJobs


cidade = input('Cidade para pesquisa(Ex.: Curitiba): ')

if cidade:
    cidade = cidade.replace(' ', '-')
else:
    print('Cidade não informada') | exit(1)

estado = input('Sigla do estado(Ex.: PR): ')

if len(estado) != 2:
    print('Siga informada de forma incorreta!') | exit(1)

termo = input('Termo de busca(opcional): ')

jobs = InfoJobs(cidade, estado, termo)
for page in jobs:
    for job in page:
        print(job)

    if jobs._has_next and \
       input('Ir para a próxima página?: (sim/não): ').lower()[0] == 'n':
        break
