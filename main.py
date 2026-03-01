import pygame
import math
import os

# 1. Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 600, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Rotação para o Mouse")
clock = pygame.time.Clock()


try:
    imagem_fundo = pygame.image.load("assets/rosa_b.png").convert()
    imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))
    
    imagem_topo = pygame.image.load("assets/agulha_b.png").convert_alpha()
    imagem_topo = pygame.transform.scale(imagem_topo, (LARGURA, ALTURA))
except pygame.error as e:
    print(f"Erro ao carregar imagens: {e}")
    print("Verifique se 'fundo.png' e 'personagem.png' existem.")
    pygame.quit()
    exit()

personagem_pos = [LARGURA // 2, ALTURA // 2]

# --- Loop Principal ---
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False


    tela.fill((0, 100, 255))
    mx, my = pygame.mouse.get_pos()
    dx = mx - personagem_pos[0]
    dy = my - personagem_pos[1]
    
    angulo = math.degrees(math.atan2(-dy, dx))

    personagem_rotacionado = pygame.transform.rotate(imagem_topo, angulo - 90)
    print("rotação é igual a:", int(angulo - 90))
    
    novo_rect = personagem_rotacionado.get_rect(center=personagem_pos)

    tela.blit(imagem_fundo, (0, 0))
    tela.blit(personagem_rotacionado, novo_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()