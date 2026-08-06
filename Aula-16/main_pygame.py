import pygame



pygame.init()



janela  =  pygame.display.set_mode([500,500])
run  =  True


while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run  =  False