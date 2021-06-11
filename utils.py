from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Felix',idade=48)
    print(pessoa)
    pessoa.save()

def consulta():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Everton').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felix').first()
    pessoa.nome = 'Rodrigo'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rodrigo').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta()
