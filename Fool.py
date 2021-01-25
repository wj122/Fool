import pygame
import sys
from pygame import*


def CardsHit(pos):
    HitFlag = 0
    CardNumber = 0
    for i in range(len(CardPos)):
        if (pos[0] >= CardPos[i][0]) and (pos[0] <= CardPos[i][0] + 150):
            if (pos[1] >= CardPos[i][1]) and (pos[1] <= CardPos[i][1] + 216):
                HitFlag = 1
                CardNumber = CardPos[i][2]
    return(HitFlag, CardNumber)
    
class Card(pygame.sprite.Sprite):
    def __init__(self, x,y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

pygame.init()
W = 1900
H = 1000
WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)

sc = pygame.display.set_mode((W, H))

xStart = 100 
yStart = 135

card0 = Card(xStart, yStart, ('6 Krest.png'))
card1 = Card(xStart + 170*1, yStart + (1)//9 * 230, '7 Krest.png')
card2 = Card(xStart + 170*2, yStart + (2)//9 * 230, '8 Krest.png')
card3 = Card(xStart + 170*3, yStart + (3)//9 * 230, '9 Krest.png')
card4 = Card(xStart + 170*4, yStart + (4)//9 * 230, '10 Krest.png')
card5 = Card(xStart + 170*5, yStart + (5)//9 * 230, 'Jack Krest.png')
card6 = Card(xStart + 170*6, yStart + (6)//9 * 230, 'Queen Krest.png')
card7 = Card(xStart + 170*7, yStart + (7)//9 * 230, 'King Krest.png')
card8 = Card(xStart + 170*8, yStart + (8 )//9 * 230, 'Ace Krest.png')
card9 = Card(xStart + 170*0, yStart + (9)//9 * 230, '6 Bibi.png')
card10 = Card(xStart + 170*1, yStart + (10)//9 * 230, '7 Bibi.png')
card11 = Card(xStart + 170*2, yStart + (11)//9 * 230, '8 Bibi.png')
card12 = Card(xStart + 170*3, yStart + (12)//9 * 230, '9 Bibi.png')
card13 = Card(xStart + 170*4, yStart + (13)//9 * 230, '10 Bibi.png')
card14 = Card(xStart + 170*5, yStart + (14)//9 * 230, 'Jack Bibi.png')
card15 = Card(xStart + 170*6, yStart + (15)//9 * 230, 'Queen Bibi.png')
card16 = Card(xStart + 170*7, yStart + (16)//9 * 230, 'King Bibi.png')
card17 = Card(xStart + 170*8, yStart + (17)//9 * 230, 'Ace Bibi.png')
card18 = Card(xStart + 170*0, yStart + (18)//9 * 230, '6 Chervi.png')
card19 = Card(xStart + 170*1, yStart + (19)//9 * 230, '7 Chervi.png')
card20 = Card(xStart + 170*2, yStart + (20)//9 * 230, '8 Chervi.png')
card21 = Card(xStart + 170*3, yStart + (21)//9 * 230, '9 Chervi.png')
card22 = Card(xStart + 170*4, yStart + (22)//9 * 230, '10 Chervi.png')
card23 = Card(xStart + 170*5, yStart + (23)//9 * 230, 'Jack Chervi.png')
card24 = Card(xStart + 170*6, yStart + (24)//9 * 230, 'Queen Chervi.png')
card25 = Card(xStart + 170*7, yStart + (25)//9 * 230, 'King Chervi.png')
card26 = Card(xStart + 170*8, yStart + (26)//9 * 230, 'Ace Chervi.png')
card27 = Card(xStart + 170*0, yStart + (27)//9 * 230, '6 Piki.png')
card28 = Card(xStart + 170*1, yStart + (28)//9 * 230, '7 Piki.png')
card29 = Card(xStart + 170*2, yStart + (29)//9 * 230, '8 Piki.png')
card30 = Card(xStart + 170*3, yStart + (30)//9 * 230, '9 Piki.png')
card31 = Card(xStart + 170*4, yStart + (31)//9 * 230, '10 Piki.png')
card32 = Card(xStart + 170*5, yStart + (32)//9 * 230, 'Jack Piki.png')
card33 = Card(xStart + 170*6, yStart + (33)//9 * 230, 'Queen Piki.png')
card34 = Card(xStart + 170*7, yStart + (34)//9 * 230, 'King Piki.png')
card35 = Card(xStart + 170*8, yStart + (35)//9 * 230, 'Ace Piki.png')


CardPos = []
status = 0


for i in range(36):
    CardPos.append([xStart -75+ 170*(i%9), yStart -108+ (i)//9*230, i, status])

pygame.init()
sc.fill(WHITE)
pygame.display.set_caption('Help for the fool')

PlayerCount = int(input('Введите количество игроков: '))

Players = []

print('Вы - игрок 1')
for i in range(PlayerCount - 1):
    print("Введите имя", i + 2, "го", end='')
    Players.append(input(' игрока: '))

print(Players)

Choice = 'Бита'

f1 = pygame.font.Font(None, 100)
for i in range(PlayerCount - 1):
    text1 = f1.render(Players[i], 10, (100, 0, 100))
    sc.blit(text1, (1600, 170 + i*120))

text1 = f1.render('Бита', 10, RED)
sc.blit(text1, (1600, 50))

text1 = f1.render('Вы', 10, GREEN)
sc.blit(text1, (1600, 800))

while 1:
    for i in pygame.event.get():
            
        if i.type == KEYDOWN and i.key == K_ESCAPE:
            # ESC key pressed
            pygame.quit()
            sys.exit()
        

        if i.type == pygame.MOUSEBUTTONDOWN:

            if i.button == 3:
                Choice = 'Бита'
            if i.button == 1:
                print(i.pos)

                if (i.pos[0] >= 1600):
                    if (i.pos[1] >= 50) and (i.pos[1] <= 150): 
                        Choice = 'Бита'
                    elif (i.pos[1] - 170)//120  < len(Players):
                        Choice = Players[(i.pos[1] - 170)//120]
                    elif (i.pos[1] >= 800):
                        Choice = 'Вы'
                
                else:    
                    CardHit, CardNum = CardsHit(i.pos)
                    print(CardHit, CardNum, Choice)
                    if CardHit == 1:
                        if Choice == 'Бита':
                            CardPos[CardNum][3] = -1            #  status

                        #elif Choice == 'Вы':
                        #    status = Choice
                        else:
                            CardPos[CardNum][3] = Choice
                            
                print(CardPos)
                pygame.display.update()

        if i.type == KEYDOWN and i.key == K_1:
            Choice = 'Вы'
            
        for j in range(1, len(Players) + 1):
            if i.type == KEYDOWN and i.key == globals()[f"K_{j + 1}"]:
                Choice = Players[j - 1]

                            
                        #for i in range(len(Players) - 1):
                            
 
    
 
    sc.fill(WHITE)
    for i in range(len(CardPos)):
        if CardPos[i][3] != -1:
            sc.blit(globals()[f"card{i}"].image, globals()[f"card{i}"].rect)


        if CardPos[i][3] != 0 and CardPos[i][3] != -1:
            if CardPos[i][3] == 'Вы':
                text1 = f1.render('Вы', 10, GREEN)
                sc.blit(text1, (xStart -70+ 170*(i%9), yStart + (i)//9*230))
            else:
                text1 = f1.render(CardPos[i][3], 10, BLUE)
                sc.blit(text1, (xStart -70+ 170*(i%9), yStart + (i//9*230)))                      


    f1 = pygame.font.Font(None, 100)
    for i in range(PlayerCount - 1):
        text1 = f1.render(Players[i], 10, (100, 0, 100))
        sc.blit(text1, (1600, 170 + i*120))

    text1 = f1.render('Бита', 10, RED)
    sc.blit(text1, (1600, 50))

    text1 = f1.render('Вы', 10, GREEN)
    sc.blit(text1, (1600, 800))
            
    pygame.display.update()

    pygame.time.delay(20)
    CardHit = 0
