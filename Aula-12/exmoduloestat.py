
import statistics
     

def mostrar_estatistica(nome_empresa, lista_notas):
    media =  statistics.mean(lista_notas)
    moda =  statistics.mode(lista_notas)
    desvio =  statistics.stdev(lista_notas)
    mediana =  statistics.median(lista_notas)

    print(f'Nome da empresa', nome_empresa)
    print('Media -', media)
    print('Moda - ', moda)
    print('Mediana - ', mediana)
    print('Desvio - ', desvio)





    