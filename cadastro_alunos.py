def cadastrar_aluno(a):
    if a in turma_alunos:
        quantidade_notas = int(input ('Quantas notas você quer cadastrar? '))
        for i in range(quantidade_notas):
            nota = float (input ('Quais notas você quer cadastrar? '))
            turma_alunos[aluno].append(nota)
    else:
        turma_alunos[aluno] = []
        print ('Novo aluno sendo cadastrado!')
        quantidade_notas = int(input ('Quantas notas você quer cadastrar? '))
        for i in range(quantidade_notas):
            nota = float (input ('Quais notas você quer cadastrar? '))
            turma_alunos[aluno].append(nota)
    return print (turma_alunos)

def media(a):
   #### media = turma_alunos[a].sum() / turma_alunos[a].len()
    return print (media)

def situacao(nota):
    if nota >= 7.0:
        return print ('Aprovado!')
    else:
        return print ('Reprovado!')
    
def exibir_boletim():
    return

def exibir_todos_boletins():
    return

turma_alunos = {'Cassio': [4,5,8], 'Maria': [], 'João': [] }

try:
    escolha = int (input ('''
    ========MENU=======
    1 - Cadastrar aluno
    2 - Calcular a média de um aluno
    3 - Verificar a situação
    4 - Ver o boletim de um aluno
    5 - Exibir todos os boletins
    0 - Sair
        
    Escolha: '''))
except: 
    print ('Digite um valor válido.')

while True:
    match escolha:
        case 1:
            aluno = input ('Deseja cadastrar qual aluno? ').title()
            cadastrar_aluno (aluno)
        case 2:
            aluno = input ('De qual aluno você quer saber a média? ').title()
            media(aluno)
        case 3:
            situacao()
        case 4:
            exibir_boletim()
        case 5:
            exibir_todos_boletins()
        case 0:
            print ('Saindo...')
    break