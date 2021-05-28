# Imports
import pygame
import random
import json


# Window settings
GRID_SIZE = 64
WIDTH = 29 * GRID_SIZE
HEIGHT = 12 * GRID_SIZE
TITLE = "Key Quest"
FPS = 60


# Create window
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (0, 150, 255)
GRAY = (175, 175, 175)

#Stages
START = 0
PLAYING = 1
LOSE = 2
COMPLETE = 3
WIN = 4

# Load fonts
font_xl = pygame.font.Font('assets/fonts/Dinomouse-Regular.otf', 96)
font_lg = pygame.font.Font('assets/fonts/Dinomouse-Regular.otf', 64)
font_md = pygame.font.Font('assets/fonts/Dinomouse-Regular.otf', 32)
font_sm = pygame.font.Font('assets/fonts/Dinomouse-Regular.otf', 24)
font_xs = pygame.font.Font(None, 14)

# Load images
hero_idle_imgs_rt = [pygame.image.load('assets/images/characters/player_idle.png').convert_alpha()]
hero_idle_imgs_lt = [pygame.transform.flip(img, True, False) for img in hero_idle_imgs_rt]

hero_walk_imgs_rt = [pygame.image.load('assets/images/characters/player_walk1.png').convert_alpha(),
                      pygame.image.load('assets/images/characters/player_walk2.png').convert_alpha()]
hero_walk_imgs_lt = [pygame.transform.flip(img, True, False) for img in hero_walk_imgs_rt]

hero_jump_imgs_rt = [pygame.image.load('assets/images/characters/player_jump.png').convert_alpha()]
hero_jump_imgs_lt = [pygame.transform.flip(img, True, False) for img in hero_jump_imgs_rt]

hero_swim_imgs_rt = [pygame.image.load('assets/images/characters/player_swim1.png').convert_alpha(),
                     pygame.image.load('assets/images/characters/player_swim2.png').convert_alpha()]
hero_swim_imgs_lt = [pygame.transform.flip(img, True, False) for img in hero_swim_imgs_rt]

grass_dirt_img = pygame.image.load('assets/images/tiles/grass_dirt.png').convert_alpha()
grass_stone_img = pygame.image.load('assets/images/tiles/grass_stone.png').convert_alpha()
sand_img = pygame.image.load('assets/images/tiles/sand.png').convert_alpha()
quick_sand_img = pygame.image.load('assets/images/tiles/quick_sand.png').convert_alpha()
water_img = pygame.image.load('assets/images/tiles/water.png').convert_alpha()
top_water_img = pygame.image.load('assets/images/tiles/top_water.png').convert_alpha()
grass_stone_img = pygame.image.load('assets/images/tiles/grass_stone.png').convert_alpha()
platform_img = pygame.image.load('assets/images/tiles/block.png').convert_alpha()
dirt_img = pygame.image.load('assets/images/tiles/dirt.png').convert_alpha()
stone_img = pygame.image.load('assets/images/tiles/stone.png').convert_alpha()
stone1_img = pygame.image.load('assets/images/tiles/stone.png').convert_alpha()
brick_img = pygame.image.load('assets/images/tiles/brick.png').convert_alpha()
dark_img = pygame.image.load('assets/images/tiles/dark.png').convert_alpha()
dark_brick_img = pygame.image.load('assets/images/tiles/dark_brick.png').convert_alpha()
box_img = pygame.image.load('assets/images/tiles/box.png').convert_alpha()
open_door_img = pygame.image.load('assets/images/tiles/open_door.png').convert_alpha()
door1_img = pygame.image.load('assets/images/tiles/locked_door.png').convert_alpha()
door2_img = pygame.image.load('assets/images/tiles/blue_locked_door.png').convert_alpha()
gem_img = pygame.image.load('assets/images/items/gem.png').convert_alpha()
heart_img = pygame.image.load('assets/images/items/heart.png').convert_alpha()

blade_imgs_lt = [pygame.image.load('assets/images/characters/enemy2a.png').convert_alpha(),
              pygame.image.load('assets/images/characters/enemy2b.png').convert_alpha()]
blade_imgs_rt = [pygame.transform.flip(img, True, False) for img in blade_imgs_lt]

spike_img = pygame.image.load('assets/images/tiles/spike.png').convert_alpha()

zombie_imgs_rt = [pygame.image.load('assets/images/characters/zombie_walk1.png').convert_alpha(),
               pygame.image.load('assets/images/characters/zombie_walk2.png').convert_alpha()]
zombie_imgs_lt = [pygame.transform.flip(img, True, False) for img in zombie_imgs_rt]

key_img = pygame.image.load('assets/images/items/key1.png').convert_alpha()

dragon_imgs_lt = [pygame.image.load('assets/images/characters/dragon1.png').convert_alpha(),
              pygame.image.load('assets/images/characters/dragon2.png').convert_alpha(),
              pygame.image.load('assets/images/characters/dragon3.png').convert_alpha(),
              pygame.image.load('assets/images/characters/dragon4.png').convert_alpha(),
              pygame.image.load('assets/images/characters/dragon5.png').convert_alpha(),
              pygame.image.load('assets/images/characters/dragon4.png').convert_alpha(),
              pygame.image.load('assets/images/characters/dragon3.png').convert_alpha(),
              pygame.image.load('assets/images/characters/dragon2.png').convert_alpha()]
dragon_imgs_rt = [pygame.transform.flip(img, True, False) for img in dragon_imgs_lt]

fire_img = pygame.image.load('assets/images/items/fire.png').convert_alpha()

torch_imgs = [pygame.image.load('assets/images/tiles/torch1.png').convert_alpha(),
              pygame.image.load('assets/images/tiles/torch2.png').convert_alpha(),
              pygame.image.load('assets/images/tiles/torch3.png').convert_alpha(),
              pygame.image.load('assets/images/tiles/torch4.png').convert_alpha(),
              pygame.image.load('assets/images/tiles/torch5.png').convert_alpha(),
              pygame.image.load('assets/images/tiles/torch6.png').convert_alpha(),
              pygame.image.load('assets/images/tiles/torch7.png').convert_alpha(),
              pygame.image.load('assets/images/tiles/torch8.png').convert_alpha(),
              pygame.image.load('assets/images/tiles/torch9.png').convert_alpha()]

# Load sounds
coin_snd = pygame.mixer.Sound('assets/sounds/coin.ogg')
achievement_snd = pygame.mixer.Sound('assets/sounds/achievement.wav')
heart_snd = pygame.mixer.Sound('assets/sounds/heart.ogg')
hurt_snd = pygame.mixer.Sound('assets/sounds/hurt.ogg')
jump_snd = pygame.mixer.Sound('assets/sounds/jump.wav')
key_snd = pygame.mixer.Sound('assets/sounds/key.wav')

#Music
theme = 'assets/music/Videogame2.wav'


#Levels
levels = ['assets/levels/level-1.json',
          'assets/levels/level-2.json',
          'assets/levels/level-3.json']

# Game classes
class Entity(pygame.sprite.Sprite):
    
    def __init__(self, x, y, image):
        super().__init__()
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x * GRID_SIZE + GRID_SIZE // 2
        self.rect.centery = y * GRID_SIZE + GRID_SIZE // 2

        self.vx = 0
        self.vy = 0

    def apply_gravity(self):
        if self.in_quick_sand() == True:
            self.vy = 1
        else:
            self.vy += gravity
            if self.vy > terminal_velocity:
                self.vy = terminal_velocity

class AnimatedEntity(Entity):
    def __init__(self, x, y, images):
        super().__init__(x, y, images[0])

        self.images = images
        self.image_index = 0
        self.ticks = 0
        self.animation_speed = 12

    def set_image_list(self):
        self.images = self.images

    def animate(self):
        self.set_image_list()
        self.ticks += 1

        if self.ticks % self.animation_speed == 0:
            self.image_index +=1

            if self.image_index >= len(self.images):
                self.image_index = 0
                
            self.image = self.images[self.image_index]

class Hero(AnimatedEntity):
    
    def __init__(self, x, y, images):
        super().__init__(x, y, images)

        self.speed = 5
        self.jump_power = 22
        self.hurt_timer = 0

        self.vx = 0
        self.vy = 0

        self.gems = 0
        self.hearts = 10
        self.score = 0
        
        self.facing_right = True
        self.jumping = False

        self.has_key = False

    def move_to(self, x, y):
        self.rect.centerx = x * GRID_SIZE + GRID_SIZE // 2
        self.rect.centery = y * GRID_SIZE + GRID_SIZE // 2

    def move_right(self):
        if self.in_quick_sand() == True:
            self.vx = self.speed // 2
            self.facing_right = True
        else:
            self.vx = self.speed
            self.facing_right = True
    	
    def move_left(self):
        if self.in_quick_sand() == True:
            self.vx = -1 * self.speed // 2
            self.facing_right = False
        else:
            self.vx = -1 * self.speed
            self.facing_right = False

    def stop(self):
        self.vx = 0

    def on_object(self):
        self.rect.y += 1
        hits_1 = pygame.sprite.spritecollide(self, platforms, False)
        hits_2 = pygame.sprite.spritecollide(self, boxes, False)
        self.rect.y -= 1
        if len(hits_1) + len(hits_2) > 0:
            return True
        else:
            return False

    def in_quick_sand(self):
        self.rect.y += 1
        hits_1 = pygame.sprite.spritecollide(self, quick_sands, False)
        self.rect.y -= 1
        if len(hits_1) > 0:
            return True
        else:
            return False

    def in_water(self):
        self.rect.y += 1
        hits_1 = pygame.sprite.spritecollide(self, waters, False)
        self.rect.y -= 1
        if len(hits_1) > 0:
            return True
        else:
            return False

    def apply_gravity(self):
        if self.in_quick_sand() == True or self.in_water() == True:
            self.vy = 1
        else:
            self.vy += gravity
            if self.vy > terminal_velocity:
                self.vy = terminal_velocity
    
    def jump(self):
        if self.on_object() == True or self.in_quick_sand() == True:
            self.vy = -1 * self.jump_power
            jump_snd.play()
            self.jumping = True
        elif self.in_water():
            self.vy = -1 * self.jump_power - 10

    def move_and_check_blocks(self):
        self.rect.x += self.vx
        hits = pygame.sprite.spritecollide(self, platforms, False)

        for platform in hits:
            if self.vx > 0:
                self.rect.right = platform.rect.left
            elif self.vx < 0:
                self.rect.left = platform.rect.right

        self.rect.y += self.vy
        hits = pygame.sprite.spritecollide(self, platforms, False)

        for platform in hits:
            if self.vy > 0:
                self.rect.bottom = platform.rect.top
                self.jumping = False
            elif self.vy < 0:
                self.rect.top = platform.rect.bottom

            self.vy = 0

    def check_world_edges(self):
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > world_width:
            self.rect.right = world_width
        elif self.rect.top > world_height:
            if self.hearts > 0:
                self.hearts -= 1

    def check_items(self):
        hits = pygame.sprite.spritecollide(self, items, True)
        
        for item in hits:
            item.apply(self)

    def check_enemies(self):
        hits = pygame.sprite.spritecollide(self, enemies, False)

        for enemy in hits:
            if enemy.jump_killable == True and self.rect.bottom == enemy.rect.top:
                enemy.kill()
            else:
                if self.hurt_timer == 0:
                    self.hearts -= 1
                    self.hurt_timer = 1.0 * FPS
                    hurt_snd.play()

                if self.rect.x < enemy.rect.x:
                    self.vx = -15
                elif self.rect.x > enemy.rect.x:
                    self.vx = 15

                if self.rect.y < enemy.rect.y:
                    self.vy = -5
                elif self.rect.y > enemy.rect.y:
                    self.vy = 5

        else:
            self.hurt_timer -=1
                
            if self.hurt_timer < 0:
                self.hurt_timer = 0

    def check_fire(self):
        hits = pygame.sprite.spritecollide(self, fires, True)
        
        for fire in hits:
            hurt_snd.play()
            self.hearts -= 1

    def check_boxes(self):
        hits = pygame.sprite.spritecollide(self, boxes, False)

        for box in hits:
            if self.vy > 0:
                self.rect.bottom = box.rect.top
                self.jumping = False
                
        hits = pygame.sprite.spritecollide(self, boxes, False)

        for box in hits:
            if self.vx > 0 and self.rect.bottom != box.rect.top:
                box.rect.left = self.rect.right
                box.vx = self.vx
            elif self.vx < 0:
                box.rect.right = self.rect.left
                box.vx = self.vx

    def reached_goal(self):
        return pygame.sprite.spritecollideany(self, goals)

    def set_image_list(self):
        if self.facing_right:
            if self.in_water() == True:
                self.images = hero_swim_imgs_rt
            elif self.jumping:
                self.images = hero_jump_imgs_rt
            elif self.vx != 0:
                self.images = hero_walk_imgs_rt
            else:
                self.images = hero_idle_imgs_rt
        else:
            if self.in_water() == True:
                self.images = hero_swim_imgs_lt
            elif self.jumping:
                self.images = hero_jump_imgs_lt
            elif self.vx != 0:
                self.images = hero_walk_imgs_lt
            else:
                self.images = hero_idle_imgs_lt

    def update(self):
        self.check_enemies()
        self.move_and_check_blocks()
        self.check_world_edges()
        self.check_items()
        self.check_boxes()
        self.apply_gravity()
        self.check_fire()
        self.animate()
    	 
class Platform(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

class Quick_sand(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

class Water(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

class Goal(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

class Background(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

class Torch(AnimatedEntity):
    def __init__(self, x, y, images):
        super().__init__(x, y, images)

        self.images = images
        self.rect = self.image.get_rect()
        self.rect.centerx = x * GRID_SIZE + GRID_SIZE // 2
        self.rect.bottom = y * GRID_SIZE + GRID_SIZE

    def update(self):
        self.animate()

class Gem(Entity):
    
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def apply(self, character):
        coin_snd.play()
        character.gems += 1
        character.score += 5
        if character.gems >= 5:
            character.hearts += 1
            character.gems = 0
        print(character.gems)
        print(character.hearts)

class Heart(Entity):
    
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def apply(self, character):
        heart_snd.play()
        if character.hearts >= 3:
            character.score += 10
        else:
            character.hearts += 1
        print(character.hearts)

class Key(Entity):
    
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def apply(self, character):
        key_snd.play()
        character.has_key = True
        character.score += 10

class Open_door(Entity):
    
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

class Closed_door(Entity):
    
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

class Box(Entity):
    
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

        self.vx = 0
        self.vy = 0

    def move_and_check_blocks(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)

        for platform in hits:
            if self.vx > 0:
                self.rect.right = platform.rect.left
                hero.rect.right = self.rect.left
            elif self.vx < 0:
                self.rect.left = platform.rect.right
                hero.rect.left = self.rect.right

        self.rect.y += self.vy
        hits = pygame.sprite.spritecollide(self, platforms, False)

        for platform in hits:
            if self.vy > 0:
                self.rect.bottom = platform.rect.top
            elif self.vy < 0:
                self.rect.top = platform.rect.bottom

            self.vy = 0

    def in_quick_sand(self):
        self.rect.y += 1
        hits_1 = pygame.sprite.spritecollide(self, quick_sands, False)
        self.rect.y -= 1
        if len(hits_1) > 0:
            return True
        else:
            return False

    def check_world_edges(self):
        if self.rect.left < 0:
            self.rect.left = 0
            hero.rect.left = self.rect.right
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
            hero.rect.right = self.rect.left

    def check_boxes(self):
        hits = pygame.sprite.spritecollide(self, boxes, False)
        hits.remove(self)

        for box in hits:
            if self.vy > 0:
                self.rect.bottom = box.rect.top
        
                
        hits = pygame.sprite.spritecollide(self, boxes, False)
        hits.remove(self)

        for box in hits:
            if self.vx > 0 and self.rect.bottom != box.rect.top:
                box.rect.left = self.rect.right
                box.vx = self.vx
            elif self.vx < 0 and self.rect.bottom != box.rect.top:
                box.rect.right = self.rect.left
                box.vx = self.vx

    def update(self):
        self.apply_gravity()
        self.move_and_check_blocks()
        self.check_world_edges()
        self.check_boxes()

class Enemy(AnimatedEntity):
    
    def __init__(self, x, y, images):
        super().__init__(x, y, images)

        self.speed = 2
        self.vx = -1 * self.speed
        self.vy = 0

    def reverse(self):
        self.vx *= -1

    def move_and_check_blocks(self):
        if self.in_quick_sand() == True:
            self.rect.x += self.vx // 2
        else:
            self.rect.x += self.vx
        hits = pygame.sprite.spritecollide(self, platforms, False)

        for platform in hits:
            if self.vx > 0:
                self.rect.right = platform.rect.left
                self.reverse()
            elif self.vx < 0:
                self.rect.left = platform.rect.right
                self.reverse()

        self.rect.y += self.vy
        hits = pygame.sprite.spritecollide(self, platforms, False)

        for platform in hits:
            if self.vy > 0:
                self.rect.bottom = platform.rect.top
            elif self.vy < 0:
                self.rect.top = platform.rect.bottom

            self.vy = 0

    def in_quick_sand(self):
        self.rect.y += 1
        hits_1 = pygame.sprite.spritecollide(self, quick_sands, False)
        self.rect.y -= 1
        if len(hits_1) > 0:
            return True
        else:
            return False

    def check_world_edges(self):
        if self.rect.left < 0:
            self.rect.left = 0
            self.reverse()
        elif self.rect.right > world_width:
            self.rect.right = world_width
            self.reverse()

    def check_boxes(self):      
        hits = pygame.sprite.spritecollide(self, boxes, True)

        for box in hits:
            if self.vx > 0:
                box.rect.left = self.rect.right
                self.vx = -1 * self.speed
            elif self.vx < 0:
                box.rect.right = self.rect.left
                self.vx = self.speed

    def check_boxes2(self):      
        hits = pygame.sprite.spritecollide(self, boxes, False)

        for box in hits:
            if self.vx > 0:
                box.rect.left = self.rect.right
                self.vx = -1 * self.speed
            elif self.vx < 0:
                box.rect.right = self.rect.left
                self.vx = self.speed

    def check_enemies(self):      
        hits = pygame.sprite.spritecollide(self, enemies, False)
        hits.remove(self)
        
        for enemy in hits:
            if self.vx > 0:
                self.rect.right = enemy.rect.left
                self.vx = -1 * self.speed
            elif self.vx < 0:
                self.rect.left = enemy.rect.right
                self.vx = self.speed

    def check_platform_edges(self):
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, platforms, False)
        self.rect.y -= 2
        
        must_reverse = True
        
        for platform in hits:
            if self.vx < 0 and platform.rect.left <= self.rect.left:
                must_reverse = False
            elif self.vx > 0 and platform.rect.right >= self.rect.right:
                must_reverse = False

        if must_reverse:
            self.reverse()

class Blade(Enemy):
    def __init__(self, x, y, images):
        super().__init__(x, y, images)
        
        self.speed = 2
        self.vx = -1 * self.speed
        self.vy = 0

    def jump_killable(self):
        return False

    def set_image_list(self):
        if self.vx > 0:
            self.images = blade_imgs_rt
        else:
            self.images = blade_imgs_lt

    def update(self):
        self.move_and_check_blocks()
        self.check_world_edges()
        self.check_boxes()
        self.check_enemies()
        self.check_platform_edges()
        self.jump_killable()
        self.animate()

class Zombie(Enemy):
    
    def __init__(self, x, y, images):
        super().__init__(x, y, images)

        self.speed = 3
        self.vx = -1 * self.speed
        self.vy = 0

    def jump_killable(self):
        return True

    def set_image_list(self):
        if self.vx > 0:
            self.images = zombie_imgs_rt
        else:
            self.images = zombie_imgs_lt

    def update(self):
        self.move_and_check_blocks()
        self.check_world_edges()
        self.check_boxes2()
        self.check_enemies()
        self.apply_gravity()
        self.jump_killable()
        self.animate()
        self.in_quick_sand()

class Fire(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()

        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.speed = 3

    def check_blocks(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)

        for platform in hits:
            self.kill()

    def check_boxes(self):
        hits = pygame.sprite.spritecollide(self, boxes, False)

        for box in hits:
            self.kill()

    def update(self):
        self.check_blocks()
        self.check_boxes()
        
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()

class Dragon(Enemy):
    
    def __init__(self, x, y, images):
        super().__init__(x, y, images)

        self.speed = 2
        self.vx = -1 * self.speed
        self.vy = 0

        self.fire_rate = 2

    def jump_killable(self):
        return True

    def attack(self):
        r = random.randrange(0, 120)
            
        if r < self.fire_rate:
            x = self.rect.left
            y = self.rect.bottom
            fires.add( Fire(x, y, fire_img) )

    def set_image_list(self):
        if self.vx > 0:
            self.images = dragon_imgs_rt
        else:
            self.images = dragon_imgs_lt

    def update(self):
        self.move_and_check_blocks()
        self.check_world_edges()
        self.check_enemies()
        self.jump_killable()
        self.attack()
        self.animate()

class Spike(pygame.sprite.Sprite):
    
    def __init__(self, x, y, image):
        super().__init__()
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = x * GRID_SIZE
        self.rect.top = y * GRID_SIZE + 30

        
    def check_boxes(self):      
        hits = pygame.sprite.spritecollide(self, boxes, True)

    def jump_killable(self):
        return False

    def update(self):
        self.jump_killable()
        self.check_boxes()

# Helper functoins
def draw_grid(offset_x=0, offset_y=0):
    for x in range(0, WIDTH + GRID_SIZE, GRID_SIZE):
        adj_x = x - offset_x % GRID_SIZE
        pygame.draw.line(screen, GRAY, [adj_x, 0], [adj_x, HEIGHT], 1)

    for y in range(0, HEIGHT + GRID_SIZE, GRID_SIZE):
        adj_y = y - offset_y % GRID_SIZE
        pygame.draw.line(screen, GRAY, [0, adj_y], [WIDTH, adj_y], 1)

    for x in range(0, WIDTH + GRID_SIZE, GRID_SIZE):
        for y in range(0, HEIGHT + GRID_SIZE, GRID_SIZE):
            adj_x = x - offset_x % GRID_SIZE + 4
            adj_y = y - offset_y % GRID_SIZE + 4
            disp_x = x // GRID_SIZE + offset_x // GRID_SIZE
            disp_y = y // GRID_SIZE + offset_y // GRID_SIZE
            
            point = '(' + str(disp_x) + ',' + str(disp_y) + ')'
            text = font_xs.render(point, True, GRAY)
            screen.blit(text, [adj_x, adj_y])

def show_hud():
    text = font_md.render(str(hero.score), True, WHITE)
    rect = text.get_rect()
    rect.midtop = WIDTH // 2, 16
    screen.blit(text, rect)

    screen.blit(gem_img, [WIDTH - 100, 16])
    text = font_sm.render('x' + str(hero.gems), True, WHITE)
    rect = text.get_rect()
    rect.topleft = WIDTH - 60, 20
    screen.blit(text, rect)

    for i in range(hero.hearts):
        x = i * 36 + 16
        y = 16
        screen.blit(heart_img, [x, y])

    if hero.has_key == True:
        screen.blit(key_img, [16 , 56])

def show_start_screen():
    text = font_xl.render(TITLE, True, WHITE)
    rect = text.get_rect()
    rect.midbottom = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)

    text = font_sm.render('Press any key to start', True, WHITE)
    rect = text.get_rect()
    rect.midtop = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)

def show_lose_screen():
    text = font_lg.render('Game over', True, WHITE)
    rect = text.get_rect()
    rect.midbottom = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)

    text = font_sm.render('Press \'r\' to play again', True, WHITE)
    rect = text.get_rect()
    rect.midtop = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)

def show_win_screen():
    text = font_lg.render('You Won!', True, WHITE)
    rect = text.get_rect()
    rect.midbottom = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)

    text = font_sm.render('Press \'r\' to play again', True, WHITE)
    rect = text.get_rect()
    rect.midtop = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)

def show_level_complete_screen():
    text = font_lg.render('Level Complete!', True, WHITE)
    rect = text.get_rect()
    rect.midbottom = WIDTH // 2, HEIGHT // 2
    screen.blit(text, rect)

#Set up
def start_game():
    global hero, stage, current_level
    
    hero = Hero(0, 0, hero_idle_imgs_rt)
    stage = START
    current_level = 0
    
def start_level():
    global player, platforms, background, doors, items, boxes, enemies, fires, goals, all_sprites, torches, quick_sands, waters
    global gravity, terminal_velocity, world_width, world_height

    platforms = pygame.sprite.Group()
    background = pygame.sprite.Group()
    doors = pygame.sprite.Group()
    goals = pygame.sprite.Group()
    items = pygame.sprite.Group()
    boxes = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    fires = pygame.sprite.Group()
    torches = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    player = pygame.sprite.GroupSingle()
    quick_sands = pygame.sprite.Group()
    waters = pygame.sprite.Group()

    #Load Level File
    with open(levels[current_level]) as f:
        data = json.load(f)

    world_width = data['width'] * GRID_SIZE
    world_height = data['height'] * GRID_SIZE

    #Add
    hero.move_to(data['start'][0], data['start'][1])
    player.add(hero)

    if 'grass_locs' in data:
        for loc in data['grass_locs']:
            platforms.add(Platform(loc[0], loc[1], grass_dirt_img))

    if 'sand_locs' in data:
        for loc in data['sand_locs']:
            platforms.add(Platform(loc[0], loc[1], sand_img))

    if 'quick_sand_locs' in data:
        for loc in data['quick_sand_locs']:
            quick_sands.add(Quick_sand(loc[0], loc[1], quick_sand_img))

    if 'block_locs' in data:
        for loc in data['block_locs']:
            platforms.add(Platform(loc[0], loc[1], platform_img))

    if 'dirt_locs' in data:
        for loc in data['dirt_locs']:
            platforms.add(Platform(loc[0], loc[1], dirt_img))

    if 'stone_locs' in data:
        for loc in data['stone_locs']:
            platforms.add(Platform(loc[0], loc[1], stone_img))

    if 'brick_locs' in data:
        for loc in data['brick_locs']:
            platforms.add(Platform(loc[0], loc[1], brick_img))

    if 'dark_brick_locs' in data:
        for loc in data['dark_brick_locs']:
            background.add(Background(loc[0], loc[1], dark_brick_img))

    if 'dark_locs' in data:
        for loc in data['dark_locs']:
            background.add(Background(loc[0], loc[1], dark_img))

    if 'torch_locs' in data:
        for loc in data['torch_locs']:
            torches.add(Torch(loc[0], loc[1], torch_imgs))

    if 'open_door_locs' in data:
        for loc in data['open_door_locs']:
            doors.add(Open_door(loc[0], loc[1], open_door_img))

    if 'door1_locs' in data:
        for loc in data['door1_locs']:
            goals.add(Goal(loc[0], loc[1], door1_img))

    if 'gem_locs' in data:
        for loc in data['gem_locs']:
            items.add(Gem(loc[0], loc[1], gem_img))

    if 'heart_locs' in data:
        for loc in data['heart_locs']:
            items.add(Heart(loc[0], loc[1], heart_img))

    if 'key_locs' in data:
        for loc in data['key_locs']:
            items.add(Key(loc[0], loc[1], key_img))

    if 'box_locs' in data:
        for loc in data['box_locs']:
            boxes.add(Box(loc[0], loc[1], box_img))

    if 'blade_locs' in data:
        for loc in data['blade_locs']:
            enemies.add(Blade(loc[0], loc[1], blade_imgs_lt))

    if 'spike_locs' in data:
        for loc in data['spike_locs']:
            enemies.add(Spike(loc[0], loc[1], spike_img))

    if 'zombie_locs' in data:
        for loc in data['zombie_locs']:
            enemies.add(Zombie(loc[0], loc[1], zombie_imgs_lt))

    if 'dragon_locs' in data:
        for loc in data['dragon_locs']:
            enemies.add(Dragon(loc[0], loc[1], dragon_imgs_lt))

    if 'water_locs' in data:
        for loc in data['water_locs']:
            waters.add(Water(loc[0], loc[1], water_img))

    if 'top_water_locs' in data:
        for loc in data['top_water_locs']:
            waters.add(Water(loc[0], loc[1], top_water_img))

    if 'grass_stone_locs' in data:
        for loc in data['grass_stone_locs']:
            platforms.add(Platform(loc[0], loc[1], grass_stone_img))

    if 'background_sand_locs' in data:
        for loc in data['background_sand_locs']:
            background.add(Background(loc[0], loc[1], sand_img))

    # Settings
    gravity = data['gravity']
    terminal_velocity = data['terminal_velocity']

    all_sprites.add(enemies, boxes, platforms, quick_sands)
    pygame.mixer.music.load(theme)
    pygame.mixer.music.play(-1)
        
# Game loop
grid_on = False
running = True
start_game()
start_level()

while running:
    # Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if stage == START:
                stage = PLAYING

            elif stage == PLAYING:
                if event.key == pygame.K_SPACE:
                    hero.jump()

            elif stage == LOSE or stage == WIN:
                if event.key == pygame.K_r:
                   start_game()
                   start_level()

            if event.key == pygame.K_g:
                grid_on = not grid_on

    pressed = pygame.key.get_pressed()
    
    if stage == PLAYING:
        if pressed[pygame.K_LEFT]:
            hero.move_left()
        elif pressed[pygame.K_RIGHT]:
            hero.move_right()
        else:
            hero.stop()

    
    # Game logic
    if stage == PLAYING:
        player.update()
        boxes.update()
        enemies.update()
        fires.update()
        torches.update()

        if hero.hearts == 0:
            stage = LOSE

        elif hero.reached_goal() and hero.has_key:
            achievement_snd.play()
            stage = COMPLETE
            pygame.mixer.music.stop()
            countdown = 2 * FPS
            hero.has_key = False

    elif stage == COMPLETE:
        countdown -= 1
        if countdown <= 0:
            current_level += 1

            if current_level < len(levels):
                start_level()
                stage = PLAYING
            else:
                stage = WIN

    if hero.rect.centerx < WIDTH // 2:
        offset_x = 0
    elif hero.rect.centerx > world_width - WIDTH // 2:
        offset_x = world_width - WIDTH
    else:
        offset_x = hero.rect.centerx - WIDTH // 2

    
    if hero.rect.centery < HEIGHT:
        offset_y = 0
    elif hero.rect.centery > world_height - HEIGHT // 2:
        offset_y = world_height - HEIGHT
    else:
        offset_y = hero.rect.centery - HEIGHT // 2


            
    # Drawing code
    screen.fill(SKY_BLUE)

    for sprite in waters:
        screen.blit(sprite.image, [sprite.rect.x - offset_x, sprite.rect.y - offset_y])

    for sprite in background:
        screen.blit(sprite.image, [sprite.rect.x - offset_x, sprite.rect.y - offset_y])

    for sprite in torches:
        screen.blit(sprite.image, [sprite.rect.x - offset_x, sprite.rect.y - offset_y])

    for sprite in fires:
        screen.blit(sprite.image, [sprite.rect.x - offset_x, sprite.rect.y - offset_y])

    for sprite in doors:
        screen.blit(sprite.image, [sprite.rect.x - offset_x, sprite.rect.y - offset_y])

    for sprite in goals:
        screen.blit(sprite.image, [sprite.rect.x - offset_x, sprite.rect.y - offset_y])

    for sprite in items:
        screen.blit(sprite.image, [sprite.rect.x - offset_x, sprite.rect.y - offset_y])

    for sprite in player:
        screen.blit(sprite.image, [sprite.rect.x - offset_x, sprite.rect.y - offset_y])

    for sprite in all_sprites:
        screen.blit(sprite.image, [sprite.rect.x - offset_x, sprite.rect.y - offset_y])

    show_hud()

    if grid_on:
        draw_grid(offset_x)

    if stage == START:
        show_start_screen()
        
    elif stage == LOSE:
        show_lose_screen()

    elif stage == COMPLETE:
        show_level_complete_screen()

    elif stage == WIN:
        show_win_screen()
        
    # Update screen
    pygame.display.update()


    # Limit refresh rate of game loop 
    clock.tick(FPS)


# Close window and quit
pygame.quit()

