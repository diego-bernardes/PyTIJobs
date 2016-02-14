class Job(object):
    """
    Class com os dados da vaga.
    """
    def __init__(self, titulo, link, descricao=None):
        self.titulo = titulo
        self.link = link
        self.descricao = descricao

    def __str__(self):
        return '''
Vaga: {titulo}
Link: {link}
--------------------------------------------------'''\
                .format(titulo=self.titulo, link=self.link)


class Jobs:
    _has_next = True
    _jobs = []

    def find(self):
        self._jobs = []
        self._has_next = False

    def __iter__(self):
        return self

    def __next__(self):
        if not self._has_next:
            raise StopIteration
        else:
            return self.find()
