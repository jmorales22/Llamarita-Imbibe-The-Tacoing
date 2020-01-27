import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH = 700
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (100, 40, 0)

#Game info

WIN = 15
taco_count = 0

#Title

TITLE = "Llamarita's Taco Adventure"

#Player size

player_dimension = 80

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

font_name = pygame.font.match_font('inkfree')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 50 * i
        img_rect.y
        surf.blit(img, img_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((player_dimension, player_dimension))
        self.image = pygame.transform.scale(player_img, (90,90))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = int(WIDTH / 2)
        self.rect.bottom = HEIGHT - 20
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image = pygame.transform.scale(taco_img, (60,60))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Marg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image = pygame.transform.scale(marg_img, (60,60))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image = pygame.transform.scale(cactus_img, (60,60))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, TITLE, 50, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Arrow keys move", 25,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Press space to begin", 25, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    waiting = False

def winning_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "You Win! Hangover Avoided!", 50, WIDTH / 2, HEIGHT * 1 / 4)
    draw_text(screen, "Taco Count:", 50, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, str(taco_count), 50, WIDTH * 3 / 4, HEIGHT / 2)    
    draw_text(screen, "Press space to continue", 25, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    waiting = False

def losing_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "You lost! Enjoy the hangover!", 50, WIDTH / 2, HEIGHT * 1 / 8)
    draw_text(screen, "Margarita Count:", 50, WIDTH * 3 / 8, HEIGHT * 3 / 8)
    draw_text(screen, str(marg_counter), 50, WIDTH * 3 / 4, HEIGHT * 3 / 8)  
    draw_text(screen, "Taco Count:", 50, WIDTH * 3.65 / 8, HEIGHT * 4 / 8)
    draw_text(screen, str(taco_count), 50, WIDTH * 3 / 4, HEIGHT * 4 / 8)  
    draw_text(screen, "Press space to continue", 25, WIDTH / 2, HEIGHT * 6 / 8)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    waiting = False

background = pygame.image.load(path.join(img_dir, 'Daytime_Background_1024x800.png')).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, 'llama.png')).convert()
taco_img = pygame.image.load(path.join(img_dir, 'taco.png')).convert()
marg_img = pygame.image.load(path.join(img_dir, 'new_margarita.png')).convert()
cactus_img = pygame.image.load(path.join(img_dir, 'new_cactus.png')).convert()
llama_mini_img = pygame.transform.scale(player_img, (50, 50))
llama_mini_img.set_colorkey(BLACK)
eat_game = pygame.mixer.Sound(path.join(snd_dir, 'chomp.wav'))
gulp_game = pygame.mixer.Sound(path.join(snd_dir, 'gulp.wav'))
scream_game = pygame.mixer.Sound(path.join(snd_dir, 'scream.wav'))
pygame.mixer.music.load(path.join(snd_dir, 'raining_tacos.wav'))
pygame.mixer.music.set_volume(0.3)

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
margs = pygame.sprite.Group()
cactus = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# play game music
pygame.mixer.music.play(loops = -1)

# Game loop
game_win = False
game_lose = False
game_over = True
running = True
while running:
    if game_over:
        if game_win == True:
            winning_screen()
        if game_lose == True:
            losing_screen()
        show_go_screen()
        game_over = False
        game_win = False
        game_lose = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        margs = pygame.sprite.Group()
        cactus = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)

        score = 0
        marg_count = 1
        marg_counter = 0
        health = 3

        for i in range(4):
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)

        for i in range(2):
            m = Marg()
            all_sprites.add(m)
            margs.add(m)

        def marg_function(count):
            for i in range(count):
                if count == WIN:
                    pass
                else:
                    m = Cactus()
                    all_sprites.add(m)
                    cactus.add(m)

    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # check to see if a cactus hit the player
    cactus_hits = pygame.sprite.spritecollide(player, cactus, True)
    if cactus_hits:
        scream_game.play()
        m = Cactus()
        all_sprites.add(m)
        cactus.add(m)
        if health == 1:
            game_lose = True
            game_over = True
        else:
            health -= 1

    # check to see if a taco hit the player
    taco_hits = pygame.sprite.spritecollide(player, mobs, True)
    if taco_hits:
        eat_game.play()
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
        score += 1
        taco_count = score        

    # check to see if a marg hit the player and adds a cactus for every hit
    marg_hits = pygame.sprite.spritecollide(player, margs, True)
    if marg_hits:
        gulp_game.play()
        m = Marg()
        all_sprites.add(m)
        margs.add(m)
        #checks to see if win
        if marg_counter + 1 == WIN:
            game_win = True
            game_over = True
        else:
            marg_function(marg_count)
            marg_counter += 1

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    #lives counter
    draw_lives(screen, WIDTH - 200, 5, health, llama_mini_img)
    #score counter
    draw_text(screen, 'Taco Score:', 20, WIDTH / 2, 10)
    draw_text(screen, str(score), 20, WIDTH / 2 + 75, 10)
    #mararita counter
    draw_text(screen, str(WIN - marg_counter), 20, WIDTH / 2 - 150, 10)
    draw_text(screen, 'Margaritas to go:', 20, WIDTH / 2 - 250, 10)
    #health counter
    #draw_text(screen, str(health), 30, WIDTH / 2 + 200, 10)
    pygame.draw.rect(background, BROWN,(0,HEIGHT-60,WIDTH,60))
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
exit()