import funcoes as fc

# def sistema_calculo_sal():
#     salario = float(input('Salario: '))
#     quantidade = float(input('Quantidade de Hora Extra:'))
#     carga = float(input('Carga Hororária: '))
#     print('SALARIO HORA:')
#     salario_hora = fc.calculo_sal_horas(carga, salario)
#     print('Salario Hora: ', salario_hora)
#     print('********************')
#     valor_hora_extra =  fc.hora_extra_hora(salario_hora)
#     print('R$', valor_hora_extra)
#     print('********************')
#     print('Total hora extra: ')
#     total_extra = fc.total_hora_extra( valor_hora_extra, quantidade)
#     print('R$', total_extra)
#     print('**********************')
#     print('Salario total: ')
#     total_sal =  fc.sal_total(salario, total_extra)
#     print('R$ ', total_sal)

# sistema_calculo_sal()    


# Desafio 1
# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA. 
# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE COM ESTATISTICA A MODA E A MEDIA E DESVIO DE PADRÃO, DAS NOTAS DE ALUNOS DE UM COLÉGIO, ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA, SEPARE EM FUNÇÕES DIFERENTES 
# 1 -  ***VOCÊ CRIAR SEUS PRÓPRIOS MÓDULOS***
# 2 - ***OU USAR STATISTICS *****

import math
import statistics
def sisnotas():

    print('SISTEMA DE NOTAS DE ALUNOS - Visão do Professor' \
        '')
    # Configuração de acesso
    SENHA_CORRETA = "123"
    tentativas_restantes = 3

    print("--- CONTROLE DE ACESSO DO PROFESSOR ---")

    # Loop de controle de acesso
    while tentativas_restantes > 0:
        senha = input("Digite a senha de acesso: ")
        
        if senha == SENHA_CORRETA:
            print("\nAcesso concedido! Bem-vindo, professor.")
            break
        else:
            tentativas_restantes -= 1
            if tentativas_restantes > 0:
                print(f"Senha incorreta! Você tem mais {tentativas_restantes} chance(s).")
            else:
                print("Senha bloqueada! Sistema encerrado.")
                exit() # Interrompe totalmente o processamento do programa


# Menu do sistema de notas (só executa se o login estiver correto)
    print("\n--- SISTEMA DE NOTAS DOS ALUNOS ---")

    notas=[]
    cadastro_alunos=[]

    while True:
        nome = input("\nDigite o nome do aluno (ou 'sair' para encerrar): ")
            
        if nome == 'sair':
            print("Sistema encerrado com sucesso.")
            break

        # Coleta das três notas do aluno    
        nota1 = float(input(f"Digite a 1ª nota de {nome}: "))
        nota2 = float(input(f"Digite a 2ª nota de {nome}: "))
        nota3 = float(input(f"Digite a 3ª nota de {nome}: "))
        notas.extend([nota1,nota2,nota3])
        # Cálculo da média aritmética
        # media = round(sum(notas) /len(notas), 2)

        media1 = fc.calcular_media_propria(notas)
        print('Média de notas do aluno: ', media1)
        print('********************')
        print('')
    
        # Condicionais para avaliar a situação baseada na média
        if media1 >= 7.0:
            situacao = "Aprovado"
        elif media1 >= 5.0:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"

        modal = fc.calcular_moda_propria(notas)
        print('Repetição de notas (moda) do aluno: ', modal)
        print('********************')
        print('')
    
        desv = fc.calcular_desvio_padrao_proprio(notas)
        print('Desvio padrão de notas do aluno: ', desv)
        print('********************')
        print('')
    
        minmax = fc.obter_extremos_proprio(notas)
        print('Menor e maior nota do aluno: ', minmax)
        print('********************')
        print('')

        # Cria a linha (sublista) com os dados do aluno atual
        alunos_medias_sit = [nome, media1, situacao]
        
        # Adiciona a linha dentro da lista principal
        cadastro_alunos.append(alunos_medias_sit)

            
        # Exibição do resultado detalhado
        print(f"\nAluno: {nome}")
        print(f"Média Final: {media1:.1f}")
        print(f"Situação: {situacao}")

    print('\n Lista final de alunos')
    for aluno in cadastro_alunos:
        # Cada 'aluno' é uma linha da sua lista de listas
        print(f"{aluno[0]:<20} | {aluno[1]:<7.1f} | {aluno[2]}")
sisnotas()