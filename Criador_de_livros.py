from Livro import Livro

livro1 = Livro('Curso de python em 6h','Alcimar Costa','Udemy', '878-98-9988-9',2018)
livro2 = Livro('Python para Web','Alcimar Costa','Udemy', '878-98-9988-9',2018)
livro3 = Livro('Inteligência Artificila','Alcimar Costa','Udemy', '878-98-9988-9',2018)

livros = [livro1, livro2, livro3]

for l in livros:
    print(l)