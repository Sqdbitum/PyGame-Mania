import pygame
from proekt import Note
from random import randint
import subprocess

subprocess.call("python game2.py", shell=True)
print(123)
settings = open('fal.txt', 'r', encoding='UTF8')
setting = settings.readlines()
print(setting)

har = ['Too easy', 'Easy', 'Hard', 'Insane', 'Extra']

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)
W, H = 1051, 590
screen = pygame.display.set_mode((W, H))

fon = pygame.image.load('images/backg.jpeg').convert()

clock = pygame.time.Clock()
FPS = 60

notes_im = ['1.jpg', '2.jpg', '3.jpg']
nt = [pygame.image.load('images/' + path).convert_alpha() for path in notes_im]

pygame.mixer.music.load(setting[0].strip())
pygame.mixer.music.play()


notes = pygame.sprite.Group()

def createNote(group):
    indx = randint(0, len(nt) - 1)
    x = randint(20, W - 20)
    a = har.index(setting[1].strip()) + 1
    speed = randint(a, a)
    x1 = 397
    x2 = 478
    x3 = 563
    # x4 = 800
    x4 = 648
    x = []
    x.append(x1)
    x.append(x2)
    x.append(x3)
    x.append(x4)
    a = randint(0, 3)
    return Note(x[a], speed, nt[indx], group, a)


createNote(notes)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createNote(notes)
    screen.blit(fon, (0, 0))
    notes.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    notes.update(H)
