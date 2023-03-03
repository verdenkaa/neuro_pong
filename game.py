import pygame, random



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
WIDTH, HEIGHT = 10, 70


class Board(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, 250)
        self.score = 0


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (350, 250)
        self.x_velocity = random.choice([-2, 2])
        self.y_velocity = random.choice([-2, 2])

    def update(self):
        if self.rect.center[1] <= 5 or self.rect.center[1] >= 495:
            self.y_velocity *= -1
        if self.rect.center[0] <= 5 or self.rect.center[0] >= 695:
            self.x_velocity *= -1
            if self.rect.center[0] <= 5:
                neuro.score += 1
            else:
                player.score += 1
        if pygame.sprite.collide_rect(self, player) or pygame.sprite.collide_rect(self, neuro):
            self.x_velocity *= -1
        self.rect.center = (self.rect.center[0] + self.x_velocity, self.rect.center[1] + self.y_velocity)




pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
carryOn = True
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Board(10)
neuro = Board(690)
ball = Ball()
all_sprites.add(player)
all_sprites.add(neuro)
all_sprites.add(ball)

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if player.rect.center[1] > HEIGHT - 30:
            player.rect.center = (player.rect.center[0], player.rect.center[1] - 2)
    elif keys[pygame.K_DOWN]:
        if player.rect.center[1] < 500 - HEIGHT + 30:
            player.rect.center = (player.rect.center[0], player.rect.center[1] + 2)
    screen.fill(BLACK)
    #pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    all_sprites.update()
    text_surface = my_font.render(f'{player.score}:{neuro.score}', False, (255, 0, 0))
    screen.blit(text_surface, (330, 10))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

