import requests
try:
    from bs4 import BeautifulSoup
except ImportError:
    print('''
BeautifulSoup não instalado

Faça a instalação do BeautifulSoup e da html5lib
[+] Links
BeautifulSoup: https://pypi.python.org/pypi/beautifulsoup4
html5lib: https://pypi.python.org/pypi/html5lib
''')
    exit(1)
from pytijobs import Job
from pytijobs import Jobs


class InfoJobs(Jobs):
    def __init__(self, cidade, estado, termo=None):
        super(Jobs, self).__init__()
        self.cidade = cidade
        self.estado = estado
        self.termo = termo
        self.page = 1

    def find(self):
        super().find()

        if self.termo:
            url = 'http://www.infojobs.com.br/vagas-de-emprego-{termo}-em-{cidade},-{estado}.aspx?Categoria=74&Page={page}' .format(termo=self.termo, cidade=self.cidade, estado=self.estado, page=self.page)
        else:
            url = 'http://www.infojobs.com.br/empregos-de-informatica-ti-telecomunicacoes-em-{cidade},-{estado}.aspx?Page={page}' .format(cidade=self.cidade, estado=self.estado, page=self.page)

        print('Buscando vagas na área: Informática, TI, Telecomunicações em: {cidade}'
              .format(cidade=self.cidade))

        infojobs = requests.get(url)
        infojobs = BeautifulSoup(infojobs.text, 'html5lib')
        class_ = infojobs.findAll(class_="vagaTitle js_vacancyTitle", href=True, title=True)

        for n in class_:
            job = Job(titulo=n['title'], link=n['href'])
            self._jobs.append(job)

        # para que uma pagina seguinte exista, n pagina atual deve exitir a classe 'lnkNext js_Next'
        h = infojobs.find(class_='lnkNext js_Next', href=True)
        if h:
            self._has_next = True
            self.page += 1
            url = 'http://www.infojobs.com.br'+h['href']

        return self._jobs
