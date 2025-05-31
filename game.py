import pygame
from pygame.locals import *

class Aspirador:
    def __init__(self, tabuleiro=(5, 5), inicio=(0, 0), sujeiras=None):
        self.tabuleiro = tabuleiro
        self.posicion = inicio
        if sujeiras is None:
            self.sujeiras = [(0, 0), (2, 2), (4, 1)]
        else:
            self.sujeiras = sujeiras

    @staticmethod
    def somar_tuplas(t1, t2):
        return tuple(a + b for a, b in zip(t1, t2))

    def isOut(self, pos):
        x, y = pos
        return (
            x < 0 or x >= self.tabuleiro[0]
            or y < 0 or y >= self.tabuleiro[1]
        )

    def mover(self, direcao):
        nova_pos = self.somar_tuplas(self.posicion, direcao)
        if not self.isOut(nova_pos):
            self.posicion = nova_pos
            # Remove sujeira se estiver no mesmo lugar
            if self.posicion in self.sujeiras:
                self.sujeiras.remove(self.posicion)

# === Inicialização do pygame ===

pygame.init()
tile_size = 128
largura_tela = tile_size * 5
altura_tela = tile_size * 5
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Aspirador de Pó")

# === Carregamento e redimensionamento das imagens ===

aspirador_sprite = pygame.transform.scale(
    pygame.image.load("./assets/aspirador.png"), (tile_size, tile_size)
)
sujeira_sprite = pygame.transform.scale(
    pygame.image.load("./assets/sujeira.png"), (tile_size, tile_size)
)
fundo_sprite = pygame.transform.scale(
    pygame.image.load("./assets/fundo.jpg"), (tile_size, tile_size)
)

# === Criar objeto do jogo ===
import random
Tabuleiro = (5, 5)

inicio = random.sample([(x, y) for x in range(tabuleiro[0]) for y in range(tabuleiro[1])], 1)
def gerar_sujeiras(tabuleiro, quantidade, evitar=None):
    largura, altura = tabuleiro
    todas_posicoes = [(x, y) for x in range(largura) for y in range(altura)]
    
    if evitar:
        todas_posicoes = [pos for pos in todas_posicoes if pos != evitar]

    return random.sample(todas_posicoes, quantidade)
Sujeiras = gerar_sujeiras(tabuleiro, 5, evitar=inicio)
aspirador = Aspirador(tabuleiro=Tabuleiro,sujeiras=Sujeiras)

# === Loop principal ===
rodando = True
clock = pygame.time.Clock()
contador = 0
while rodando:
    contador+=1
    tela.fill((0, 0, 0))

    # Desenhar fundo
    for x in range(5):
        for y in range(5):
            tela.blit(fundo_sprite, (x * tile_size, y * tile_size))

    # Desenhar sujeiras
    for (x, y) in aspirador.sujeiras:
        tela.blit(sujeira_sprite, (x * tile_size, y * tile_size))

    # Desenhar aspirador
    x, y = aspirador.posicion
    tela.blit(aspirador_sprite, (x * tile_size, y * tile_size))

    pygame.display.flip()

    # Eventos
    for evento in pygame.event.get():
        print(evento)
        if evento.type == QUIT:
            rodando = False
        elif evento.type == KEYDOWN:
            if evento.key == K_UP:
                aspirador.mover((0, -1))
            elif evento.key == K_DOWN:
                aspirador.mover((0, 1))
            elif evento.key == K_LEFT:
                aspirador.mover((-1, 0))
            elif evento.key == K_RIGHT:
                aspirador.mover((1, 0))

    clock.tick(10)  # 10 FPS

pygame.quit()
