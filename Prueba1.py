import pygame as pygame
from pygame import *
# Inicialización
pygame.init()

# Configuración de la ventana
screen_width = 800
screen_height = 450
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego Medieval")
background_image = pygame.image.load("C:\\Users\\santo\\Desktop\\Pygame\\Castle.jpg").convert()
# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
player_image = pygame.image.load(f"C:\\Users\\santo\\Desktop\\Pygame\\caballero.png").convert_alpha()
# Clase para el jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image  # Asigna la imagen cargada
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2
        self.rect.y = screen_height - 100
        self.vel_x = 0
        self.vel_y = 0
        self.is_jumping = False
        self.jump_count = 10
        self.gravity = 0.8

    def update(self):
        self.rect.x += self.vel_x

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel_x = -5
        elif keys[pygame.K_RIGHT]:
            self.vel_x = 5
        else:
            self.vel_x = 0
        self.vel_y += self.gravity

        # Aplicar movimiento horizontal
        self.rect.x += self.vel_x

        # Aplicar movimiento vertical (salto)
        if self.is_jumping:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10

        # Aplicar gravedad
        self.rect.y += self.vel_y

        # Restringir el jugador a la pantalla
        if self.rect.y >= screen_height - self.rect.height:
            self.rect.y = screen_height - self.rect.height
            self.vel_y = 0

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_count = 10
            self.vel_y = -10

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Grupo de sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
    # Actualización
    all_sprites.update()

    # Dibujado
    window.fill(BLACK)
    
    window.blit(background_image, (0, 0))
    all_sprites.draw(window)

    # Actualización de la pantalla
    pygame.display.flip()
    clock.tick(60)

# Finalización del juego
pygame.quit()