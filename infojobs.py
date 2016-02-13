import requests
try: from bs4 import BeautifulSoup
except ImportError:
    print('''
BeautifulSoup não instalado

Faça a instalação do BeautifulSoup e da html5lib
[+] Links
BeautifulSoup: https://pypi.python.org/pypi/beautifulsoup4
html5lib: https://pypi.python.org/pypi/html5lib
''')
    exit(1)
def infojobs_s(cidade, estado, termo=None):
    global infojobs
    if termo:
        url = 'http://www.infojobs.com.br/vagas-de-emprego-{termo}-em-{cidade},-{estado}.aspx?Categoria=74' .format(termo=termo, cidade=cidade, estado=estado)
    else:
        url = 'http://www.infojobs.com.br/empregos-de-informatica-ti-telecomunicacoes-em-{cidade},-{estado}.aspx' .format(cidade=cidade, estado = estado)
    print('Buscando vagas na área: Informática, TI, Telecomunicações em: {cidade}'
          .format(cidade=cidade))
    while True:
        infojobs = requests.get(url)
        infojobs = BeautifulSoup(infojobs.text, 'html5lib')
        class_ = infojobs.findAll(class_="vagaTitle js_vacancyTitle", href=True, title=True)
        for n in class_:
            print('''
Vaga: {vaga}
Link: {link}
--------------------------------------------------'''
          .format(vaga=n['title'], link=n['href']))
        h = infojobs.find(class_='lnkNext js_Next', href=True) #para que uma pagina seguinte exista, n pagina atual deve exitir a classe 'lnkNext js_Next'
        if h:
            continuar = input('Ir para a próxima página?: (sim/não): ')
            if continuar.lower() == 'não' or continuar.lower() == 'nao':
                break
            else:
                url = 'http://www.infojobs.com.br'+h['href']
        else:
            break


