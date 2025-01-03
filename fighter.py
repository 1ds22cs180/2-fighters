import pygame

class Fighter():
    def __init__(self, x, y):
        self.flip = False
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        #self.on_ground = False
        

    
    def move(self, screen_width,screen_height,surface, target):
        SPEED  = 12
        GRAVITY = 3
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        
        if self.attacking == False:
            #movement
           if key[pygame.K_a]:
             dx -= SPEED
           if key[pygame.K_d]:
             dx = SPEED
           if key[pygame.K_w] and self.jump == False:
             self.vel_y = -30
             self.jump = True
            #attacking
           if key[pygame.K_f] or key[pygame.K_g]:
             self.attack(surface, target)
             if key[pygame.K_f]:
               self.attack_type = 1
             if key[pygame.K_g]:
               self.attack_type = 2
                
        self.vel_y += GRAVITY
        dy += self.vel_y
        
        #ensure the fighter does not go out of bounds
        if self.rect.left + dx < 0:
            dx  = - self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height-110:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 110 - self.rect.bottom
        
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
           self.flip = True

        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect((self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2* self.rect.width, self.rect.height))
        if attacking_rect.colliderect(target.rect):
            target.health -= 10
            
        
        pygame.draw.rect(surface , (0,255,0) , attacking_rect)
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)