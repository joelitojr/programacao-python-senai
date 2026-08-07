# # 07/08/2026

# # Exemplo da professora 

import pygame
import sys
import random

pygame.init()

# tamanho da tela
LARGURA = 800
ALTURA = 400

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("T-Rex Runner")

# carregar imagens
trex1 = pygame.image.load("trex1.png")
trex2 = pygame.image.load("trex2.png")
cacto_img = pygame.image.load("cacto.png")
chao = pygame.image.load("chao.png")

# posição do trex
trex_x = 100
trex_y = 300

# física do pulo
vel_y = 0
gravidade = 1
pulando = False

# chão infinito
chao_x = 0

# cacto
cacto_x = 800
cacto_y = 300

# animação
frame = 0

# pontuação
score = 0
fonte = pygame.font.SysFont("Arial", 30)

# controle do jogo
game_over = False

clock = pygame.time.Clock()

while True:

    # eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # pular
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and not pulando:
                vel_y = -15
                pulando = True

            if evento.key == pygame.K_r and game_over:
                # reiniciar jogo
                trex_y = 300
                cacto_x = 800
                score = 0
                game_over = False

    if not game_over:

        # aplicar gravidade
        vel_y += gravidade
        trex_y += vel_y

        # limitar no chão
        if trex_y >= 300:
            trex_y = 300
            pulando = False

        # mover chão
        chao_x -= 5
        if chao_x <= -800:
            chao_x = 0

        # mover cacto
        cacto_x -= 5

        if cacto_x < -50:
            cacto_x = random.randint(800,1000)
            score += 1

        # animação
        frame += 1
        if frame > 20:
            frame = 0

        if frame < 10:
            trex = trex1
        else:
            trex = trex2

        # colisão
        trex_rect = trex.get_rect(topleft=(trex_x, trex_y))
        cacto_rect = cacto_img.get_rect(topleft=(cacto_x, cacto_y))

        if trex_rect.colliderect(cacto_rect):
            game_over = True

    # desenhar fundo
    tela.fill((255,255,255))

    # chão infinito
    tela.blit(chao,(chao_x,340))
    tela.blit(chao,(chao_x+800,340))

    # desenhar trex
    tela.blit(trex,(trex_x,trex_y))

    # desenhar cacto
    tela.blit(cacto_img,(cacto_x,cacto_y))

    # pontuação
    texto = fonte.render("Score: "+str(score),True,(0,0,0))
    tela.blit(texto,(650,20))

    if game_over:
        texto2 = fonte.render("GAME OVER - Aperte R",True,(255,0,0))
        tela.blit(texto2,(250,200))

    pygame.display.update()

    clock.tick(30)