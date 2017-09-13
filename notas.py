#coding: UTF-8

#Instala as bibliotecas necessárias
def instalar_biblioteca(biblioteca):
    import importlib
    try:
        importlib.import_module(biblioteca)
    except ImportError:
        import pip
        pip.main(['install', biblioteca])
    finally:
        globals()[biblioteca] = importlib.import_module(biblioteca)

instalar_biblioteca('robobrowser')
instalar_biblioteca('bs4')

#Importa as bibliotecas utilizadas
import os
import re
import bs4
import getpass
from robobrowser import RoboBrowser

#Limpa console
os.system('cls' if os.name == 'nt' else 'clear')

br = RoboBrowser()

#Requisita ao usúario login e senha
username = str(input("Digite os 2 últimos números do seu login (mátricula): "))
password = getpass.getpass("Digite a sua senha do portal do aluno (ela ficará invisível): ")

#Efetua o login no site
url = 'https://portal.ufsm.br/aluno/turmas/list.html'
br.open(url)
form = br.get_form()
form['j_username'] = '2017112760%s' % username
form['j_password'] = password
br.submit_form(form)
if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
    os.system ('cls' if os.name == 'nt' else 'clear')
    print ("Login e/ou senha estão errados!")
    input("\nPressione ENTER para fechar!")
    exit()
form = br.get_form()
br.submit_form(form)
codigo = str(br.parsed)

os.system('cls' if os.name == 'nt' else 'clear')      

#Escolhe a disciplina
print ("| 1 - Algoritmos  | 2 - Artes -  | 3 - Ed. Física             |")
print ("| 4 - Filosofia   | 5 - Física   | 6 - Fundamentos / Hardware |")
print ("| 7 - Geografia   | 8 - Inglês   | 9 - Português              |")
print ("| 10 - Matemática | 11 - Química | 12 - Redes de computadores |")
print ("| 13 - Sociologia |\n")
escolha = int(input("Digite a disciplina desejada: "))

os.system('cls' if os.name == 'nt' else 'clear')

#Redireciona o usúario para a url referente a disciplina escolhida
if escolha == 1:
    urlMateria = re.search (r'(itemCurriculoAluno=)(.*?)(" title="Detalhes da turma">\n........................Algoritmos)', codigo)
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=%s" % urlMateria.group(2)
    print ("=========== ALGORITMOS ===========")

if escolha == 2:
    urlMateria = re.search (r'(itemCurriculoAluno=)(.*?)(" title="Detalhes da turma">\n........................Artes)', codigo)
    urlNota = 'https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=%s' % urlMateria.group (2)
    print ("=========== ARTES ===========")

if escolha == 3:
    urlMateria = re.search (r'(itemCurriculoAluno=)(.*?)(" title="Detalhes da turma">\n........................Educação)', codigo)
    urlNota = 'https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=%s' % urlMateria.group (2)
    print ("=========== ED. FÍSICA ===========")

if escolha == 4:
    urlMateria = re.search (r'(itemCurriculoAluno=)(.*?)(" title="Detalhes da turma">\n........................Filosofia)', codigo)
    urlNota = 'https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=%s' % urlMateria.group (2)
    print ("=========== FILOSOFIA ===========")

if escolha == 5:
    urlMateria = re.search (r'(itemCurriculoAluno=)(.*?)(" title="Detalhes da turma">\n........................Física)', codigo)
    urlNota = 'https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=%s' % urlMateria.group (2)
    print ("=========== FÍSICA ===========")

if escolha == 6:
    urlMateria = re.search (r'(itemCurriculoAluno=)(.*?)(" title="Detalhes da turma">\n........................Fundamentos)', codigo)
    urlNota = 'https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=%s' % urlMateria.group (2)
    print ("=========== FUNDAMENTOS / HARDWARE ===========")

if escolha == 7:
    urlMateria = re.search (r'(itemCurriculoAluno=)(.*?)(" title="Detalhes da turma">\n........................Geografia)', codigo)
    urlNota = 'https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=%s' % urlMateria.group (2)
    print ("=========== GEOGRAFIA ===========")

if escolha == 8:
    urlMateria = re.search (r'(itemCurriculoAluno=)(.*?)(" title="Detalhes da turma">\n........................Língua Estrangeira)', codigo)
    urlNota = 'https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=%s' % urlMateria.group (2)
    print ("=========== INGLÊS ===========")

if escolha == 9:
    urlMateria = re.search (r'(itemCurriculoAluno=)(.*?)(" title="Detalhes da turma">\n........................Língua Portuguesa)', codigo)
    urlNota = 'https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=%s' % urlMateria.group (2)
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070444"
    print ("=========== PORTUGUÊS ===========")

if escolha == 10:
    urlMateria = re.search (r'(itemCurriculoAluno=)(.*?)(" title="Detalhes da turma">\n........................Matemática)', codigo)
    urlNota = 'https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=%s' % urlMateria.group (2)
    print ("=========== MATEMÁTICA ===========")

if escolha == 11:
    urlMateria = re.search (r'(itemCurriculoAluno=)(.*?)(" title="Detalhes da turma">\n........................Química)', codigo)
    urlNota = 'https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=%s' % urlMateria.group (2)
    print ("=========== QUÍMICA ===========")

if escolha == 12:
    urlMateria = re.search (r'(itemCurriculoAluno=)(.*?)(" title="Detalhes da turma">\n........................Redes)', codigo)
    urlNota = 'https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=%s' % urlMateria.group (2)
    print ("=========== REDES DE COMPUTADORES ===========")

if escolha == 13:
    urlMateria = re.search (r'(itemCurriculoAluno=)(.*?)(" title="Detalhes da turma">\n........................Sociologia)', codigo)
    urlNota = 'https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=%s' % urlMateria.group (2)
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070448"
    print ("=========== SOCIOLOGIA ===========")

#Recolhe e escreve as informações de notas e presenças
br.open(urlNota)
codigo = str(br.parsed)
soup = bs4.BeautifulSoup (codigo, 'html.parser')
totalPresencas = re.search(r'(class="icon-warning-sign ausente"></i> )(.*)', codigo)
totalFaltasID = re.search(r'(id=")(.*)(_label">Total de faltas</span>)', codigo)
totalFaltas = re.search(r'(%s" style="">)(.*)(</span>)' % (totalFaltasID.group (2)), codigo)
minPresencaID = re.search(r'(id=")(.*)(_label">Mínimo de presenças</span>)', codigo)
minPresencas = re.search(r'(%s" style="">)(.*)(</span>)' % (minPresencaID.group (2)), codigo)
cargaHorariaID = re.search(r'(id=")(.*)(_label">Carga horária</span>)', codigo)
cargaHoraria = re.search(r'(%s" style="">)(.*)(</span>)' % (cargaHorariaID.group (2)), codigo)

nota1 = re.search (r'(<td class="" data-value="1">Nota 1</td>\n<td class="number ">10</td>\n<td class="number ">\n<span class="" style="">)(.*?)(</span>)', codigo)
nota2 = re.search (r'(<td class="" data-value="2">Nota 2</td>\n<td class="number ">10</td>\n<td class="number ">\n<span class="" style="">)(.*?)(</span>)', codigo)
nota3 = re.search (r'(<td class="" data-value="3">Nota 3</td>\n<td class="number ">10</td>\n<td class="number ">\n<span class="" style="">)(.*?)(</span>)', codigo)
nota4 = re.search (r'(<td class="" data-value="4">Nota 4</td>\n<td class="number ">10</td>\n<td class="number ">\n<span class="" style="">)(.*?)(</span>)', codigo)
mediaBimestral = re.search (r'(<td class="" data-value="5">Média Bimestral</td>\n<td class="number ">10</td>\n<td class="number ">\n<span class="" style="">)(.*?)(</span>)', codigo)

print ("\n=========== NOTAS ===========\n")

if nota1 != None:
    print ("Nota 1: %s" % nota1.group(2))
if nota1 == None:
    print ("Nota 1: Não informada!")
if nota2 != None:
    print ("Nota 2: %s" % nota2.group(2))
if nota2 == None:
    print ("Nota 2: Não informada!")
if nota3!= None:
    print ("Nota 3: %s" % nota3.group(2))
if nota3 == None:
    print ("Nota 3: Não informada!")
if nota4 != None:
    print ("Nota 4: %s" % nota4.group(2))
if nota4 == None:
    print ("Nota 4: Não informada!")
if mediaBimestral != None:
        print ("Média Bimestral: %s" % mediaBimestral.group(2))
if mediaBimestral == None:
    print ("Média Bimestral: Não informada!")

print ("\n=========== PRESENÇAS ===========\n")
print ("Carga horária: {}".format (cargaHoraria.group (2)))
print ("Mínimo de presenças: {}".format (minPresencas.group (2)))
print ("Total de presenças: {}".format (totalPresencas.group (2)))
print ("Total de faltas: {}".format (totalFaltas.group (2)))

input("\nPressione ENTER para fechar!")
exit ()