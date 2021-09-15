
class Livro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo # Atributo privado
        self.autor = autor

    # getter and setter

    @property
    def titulo(self):
        return  self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo


# exemplo de acesso direto modificado a intancia da classe

livro1 = Livro('Curso de Python','Alcimar Costa')
print(livro1.autor)
print(livro1.titulo)
livro1.titulo = 'Novo autor'
print(livro1.titulo)


