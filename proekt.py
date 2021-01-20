import pygame

class Note(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, group, a):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.a = a + 1
        self.add(group)


    def update(self, *args):
        key = pygame.key.get_pressed()
        if self.a == 1:
            if self.rect.y > 580:
                pygame.quit()
            if key[pygame.K_d]:
                if self.rect.y > 310:
                    self.kill()
            else:
                self.rect.y += self.speed
        elif self.a == 2:
            if self.rect.y > 580:
                pygame.quit()
            if key[pygame.K_f]:
                if self.rect.y > 310:
                    self.kill()
            else:
                self.rect.y += self.speed
        elif self.a == 3:
            if self.rect.y > 580:
                pygame.quit()
            if key[pygame.K_g]:
                if self.rect.y > 310:
                    self.kill()
            else:
                self.rect.y += self.speed
        elif self.a == 4:
            if self.rect.y > 580:
                pygame.quit()
            if key[pygame.K_h]:
                if self.rect.y > 310:
                    self.kill()
            else:
                self.rect.y += self.speed
