# # 07/08/2026

# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

# Importar a blibioteca "pygame", permitindo utilizar comandos, funções
import pygame

# Inicializa o Pygame
pygame.init()


# ATIVIDADE 1: 

# o que a estrutura(sintaticamente)? para que serve(contexto)? 
# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/

# 1 - cita a estrutura de código
# 2 - contextualiza 




#exemplo:
# 2 varáveis , uma defini a altura a outra a largura 
largura, altura = 400, 400

# 1 variável , onde atribui configurações da tela a partir das informações de "Largura" e "Altura", definidas acima
tela = pygame.display.set_mode((largura, altura))
# Atribui, exibi, título "Labirinto" nessa tela
pygame.display.set_caption("Labirinto")

# 3 varíaveis (uma em cada linha) , que recebem Tuplas , com 3 informações (atributos) cada, definindo cores: preto, branco e vermelho
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)


# 1 variável , que recebe o valor "40", referente ao tamanho da célula (na tela)
tamanho_celula = 40
# 1 variável , que recebe uma lista (10 colunas x 10 linhas), onde cada informação (campo: col x linha) se referente a formação (desenho) do labirinto
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# 2 varáveis , que recebem cálculo inicial (1 *) tamanho da célula, definindo altura x largura
x, y = 1 * tamanho_celula, 1 * tamanho_celula
# 1 variável , que recebe o valor "40", referente ao controle da velocidade do jogo
velocidade = 40

# função para formatação do jogo "Labirinto" na tela, a partir dos parâmetros (variáveis) definidas acima
def desenhar_labirinto():
#   loop , com o comando "for" utilizando "linha" (posições horizontais) como índice, até que atinja o valor de "tamanho" da variável (lista) "labirinto"
    for linha in range(len(labirinto)):
#       loop , com o comando "for" utilizando "coluna" (posições verticais) como índice, até que atinja o valor de "tamanho" da variável (lista) "labirinto"
        for coluna in range(len(labirinto[linha])):
#           1 variável , que recebe a cor a ser exibida em cada posição.
#           Condicional , se a posição (linha x coluna) da lista "labirinto" for igual a "1", exibe a cor "preto" (variável), caso contrário, mostra a cor "branca" (variável)
            cor = preto if labirinto[linha][coluna] == 1 else branco
#           Função para desenhar cada posição do "Labirinto" a ser exibida 
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

# 1 variável , que recebe valor booleano "True" e é utilizada para controle de loop de processamento
executando = True
# loop , com o comando "While" , processando a lógica principal do jogo até que a variável acima mude o seu valor (de "True" para "False") , por condição lógica
while executando:
#   loop , com o comando "for" utilizando "evento" como índice , para capturar a tecla digitada. Ou melhor , a movimentação da "personagem" (quadrado vermelho) ou comando para sair do jogo 
    for evento in pygame.event.get():
#       Condicional , se pressionado comando de Saída do jogo 
        if evento.type == pygame.QUIT:
#           1 variável , que recebe valor booleano "False" , definindo a interrupção do loop principal
            executando = False

# 1 variável , que recebe valor o valor da tela pressionada . Ou seja , comando desejado 
    teclas = pygame.key.get_pressed()
#   Condicional , se pressionado a "Seta para Esquerda"
    if teclas[pygame.K_LEFT]:
#       1 variável , que recebe o cálculo , ou melhor , a subtração do valor da coluna (variável x) pela velocidade (variável)
        novo_x = x - velocidade
#       Condicional , se a posição do "labirinto" é igual a zero . Ou melhor "linha (variável y) x coluna (variável novo_x)" , dividas pelo tamanho da célula (varíavel)
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
#           1 variável , que recebe o valor atual (calculado) da posição "coluna"
            x = novo_x
#   Condicional , se pressionado a "Seta para Direita"
    if teclas[pygame.K_RIGHT]:
#       1 variável , que recebe o cálculo , ou melhor , a adição do valor da coluna (variável x) mais a velocidade (variável)
        novo_x = x + velocidade
#       Condicional , se a posição do "labirinto" é igual a zero . Ou melhor "linha (variável y) x coluna (variável novo_x)" , dividas pelo tamanho da célula (varíavel)
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
#           1 variável , que recebe o valor atual (calculado) da posição "coluna"
            x = novo_x
#   Condicional , se pressionado a "Seta para Cima"
    if teclas[pygame.K_UP]:
#       1 variável , que recebe o cálculo , ou melhor , a subtração do valor da linha (variável y) pela velocidade (variável)
        novo_y = y - velocidade
#       Condicional , se a posição do "labirinto" é igual a zero . Ou melhor "linha (variável novo_y) x coluna (variável x)" , dividas pelo tamanho da célula (varíavel)
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
#           1 variável , que recebe o valor atual (calculado) da posição "linha"
            y = novo_y
#   Condicional , se pressionado a "Seta para Baixo"
    if teclas[pygame.K_DOWN]:
#       1 variável , que recebe o cálculo , ou melhor , a adição do valor da linha (variável y) mais a velocidade (variável)
        novo_y = y + velocidade
#       Condicional , se a posição do "labirinto" é igual a zero . Ou melhor "linha (variável novo_y) x coluna (variável x)" , dividas pelo tamanho da célula (varíavel)
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
#           1 variável , que recebe o valor atual (calculado) da posição "linha"
            y = novo_y

#   Função para preencher o fundo de tela na cor "branca" (variável)
    tela.fill(branco)

#   Função para desenhar a movimentação da "personagem" (quadrado vermelho) durante cada movimento realizado ("realtime")
    desenhar_labirinto()
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

#   Função que atualiza a tela "tudo" o que foi processado. Ou seja, de acordo com a lógica acima
    pygame.display.flip()

#   Função que gerencia, controla o tempo de execução do jogo
    pygame.time.Clock().tick(10)

# Função para parar o jogo , após sair do loop principal ("While")
pygame.quit()