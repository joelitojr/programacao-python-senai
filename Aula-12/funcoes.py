

def calculo_sal_horas(carga , salario):
    return salario/ carga 

def hora_extra_hora(sal_hora):
    return sal_hora * 1.5

def total_hora_extra(valor_extra, q):
    return valor_extra * q

def sal_total (salario, total_extra):
    return salario + total_extra



def estatistica(lista_notas):
    moda  =  statistics.mode(lista_notas)
    media = statistics.mean(lista_notas)
    desvio =  statistics.stdev(lista_notas)
    mediana =  statistics.median(lista_notas)
    variancia =  statistics.variance(lista_notas)
    menor =  min(lista_notas)
    maior =  max(lista_notas)

    return moda, media, desvio , mediana, variancia, menor, maior



# Desafio 1
# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA. 
# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE COM ESTATISTICA A MODA E A MEDIA E DESVIO DE PADRÃO, DAS NOTAS DE ALUNOS DE UM COLÉGIO, ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA, SEPARE EM FUNÇÕES DIFERENTES 
# 1 -  ***VOCÊ CRIAR SEUS PRÓPRIOS MÓDULOS***
# 2 - ***OU USAR STATISTICS *****
import math
import statistics

def calcular_media_propria(notas):
    """Calcula a média aritmética simples."""
    if not notas:
        return 0
    return sum(notas) / len(notas)

def calcular_moda_propria(notas):
    """Calcula a moda (valor que mais se repete). Retorna uma lista de modas."""
    if not notas:
        return []
    
    frequencias = {}
    for nota in notas:
        frequencias[nota] = frequencias.get(nota, 0) + 1
        
    max_frequencia = max(frequencias.values())
    
    # Se nenhuma nota se repetir (frequência máxima é 1), não há moda (amodal)
    if max_frequencia == 1 and len(notas) > 1:
        return "Amodal (Nenhuma nota se repete)"
        
    modas = [nota for nota, freq in frequencias.items() if freq == max_frequencia]
    return modas

def calcular_desvio_padrao_proprio(notas):
    """Calcula o desvio padrão populacional."""
    if not notas or len(notas) < 2:
        return 0
    
    media = calcular_media_propria(notas)
    # Soma dos quadrados das diferenças em relação à média
    variancia = sum((nota - media) ** 2 for nota in notas) / len(notas)
    return math.sqrt(variancia)

def obter_extremos_proprio(notas):
    """Retorna a menor e a maior nota em uma tupla (menor, maior)."""
    if not notas:
        return 0, 0
    return min(notas), max(notas)




