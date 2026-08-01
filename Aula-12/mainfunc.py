

import funcoes as fc

def sistema_calculo_sal():
    salario = float(input('Salario: '))
    quantidade = float(input('Quantidade de Hora Extra:'))
    carga = float(input('Carga Hororária: '))
    print('SALARIO HORA:')
    salario_hora = fc.calculo_sal_horas(carga, salario)
    print('Salario Hora: ', salario_hora)
    print('********************')
    valor_hora_extra =  fc.hora_extra_hora(salario_hora)
    print('R$', valor_hora_extra)
    print('********************')
    print('Total hora extra: ')
    total_extra = fc.total_hora_extra( valor_hora_extra, quantidade)
    print('R$', total_extra)
    print('**********************')
    print('Salario total: ')
    total_sal =  fc.sal_total(salario, total_extra)
    print('R$ ', total_sal)

sistema_calculo_sal()    