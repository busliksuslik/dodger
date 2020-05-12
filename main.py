from random import randint
import pygame
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 500)

W = 800
H = 800
WHITE = (255, 255, 255)
BG = ("BG.png")
MH = ("MH.png")
BG_SURF = []  # для хранения готовых bad guys-поверхностей

sc = pygame.display.set_mode((W, H))

for i in range(4):
    BG_SURF.append(pygame.image.load(BG).convert_alpha())
    
class Main_hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(MH).convert_alpha()
        self.rect = self.image.get_rect(center=(200, 200))
    def update(self,x,y):
        self.rect.y = y
        self.rect.x = x

            
class Bad_guy(pygame.sprite.Sprite):
    def __init__(self, x, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.add(group)  # добавляем в группу
        self.speed = randint(1, 10)  # у машин будет разная скорость
 
    def update(self):
        if self.rect.y < H:
            self.rect.y += self.speed
        else:
            # теперь не перебрасываем вверх,
            # а удаляем из всех групп
            self.kill()
            
cars = pygame.sprite.Group()
mh = Main_hero()
# добавляем первую машину, которая появляется сразу
Bad_guy(randint(1, W), BG_SURF[randint(0, 2)], cars)
 
while 1:
    mh.update(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
    for i in pygame.event.get():
        if i.type == pygame.QUIT or pygame.sprite.spritecollide(mh, cars, False) != []:
            pygame.quit()
            exit()
        elif i.type == pygame.USEREVENT:
            Bad_guy(randint(1, W), BG_SURF[randint(0, 2)], cars)
    
 
    sc.fill(WHITE)
    sc.blit(mh.image,mh.rect)
    cars.draw(sc)
    pygame.display.update()
    pygame.time.delay(20)
    cars.update()
 
