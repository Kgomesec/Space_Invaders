import pygame

#definir fps
clock = pygame.time.Clock()
fps = 60

largura_tela = 600
altura_tela = 800

screen = pygame.display.set_mode((largura_tela, altura_tela))

background = pygame.image.load("Images/background.jpg")

def draw_bg():
    screen.blit(background, (0, 0))

#gerar imagem
pygame.init()

#deixar aberto
running = True
while running:

    clock.tick(fps)

    #background
    draw_bg()

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

        print(event)

    pygame.display.update()

pygame.quit()