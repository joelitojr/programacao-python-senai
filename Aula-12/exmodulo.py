
import statistics


def registrar_notas(nome, lista_notas):
     
    p = input(f'Deseja resgistrar as notas? do aluno {nome}')
    while p  ==  'sim':
        nota1 = float(input('nota: '))
        nota2 = float(input('nota: '))
        nota3 = float(input('nota: '))
        lista_notas.extend([nota1, nota2, nota3])
        p = input(f'Deseja  continuar?')
    else:
        return lista_notas
     


def mostrar_estatistica(lista_notas):
    media =  statistics.mean(lista_notas)
    moda =  statistics.mode(lista_notas)
    desvio =  statistics.stdev(lista_notas)
    
    c  =  set(lista_notas)
    if len(lista_notas) ==  len(c):
       return f'Media - {media} | Não tem moda | Desvio Padrão - {desvio}'
    else:
        return f'Media - {media} | Tem moda {moda} | Desvio Padrão - {desvio}'




    