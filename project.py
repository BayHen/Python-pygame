import pygame
import math
import time
from pygame import mouse


pygame.init()

start = False
total_secs = 0
total = 0
screen = pygame.display.set_mode((500,550))

GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)

font = pygame.font.SysFont('sans', 50)
text_1 = font.render('+', True, BLACK)
text_2 = font.render('+', True, BLACK)
text_3 = font.render('-', True, BLACK)
text_4 = font.render('-', True, BLACK)
text_5 = font.render('Start', True, BLACK)
text_6 = font.render('Reset', True, BLACK)


running = True

while running:
    screen.fill(GREY)
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # print(mouse_x,mouse_y)  

    pygame.draw.rect(screen, WHITE, (100,50,50,50))
    pygame.draw.rect(screen, WHITE, (200,50,50,50))
    pygame.draw.rect(screen, WHITE, (300,50,100,50))
    pygame.draw.rect(screen, WHITE, (100,180,50,50))
    pygame.draw.rect(screen, WHITE, (200,180,50,50))
    pygame.draw.rect(screen, WHITE, (300,180,110,50))

    screen.blit(text_1, (112,45))
    screen.blit(text_2, (212,45))
    screen.blit(text_3, (120,175))
    screen.blit(text_4, (220,175))
    screen.blit(text_5, (300,50))
    screen.blit(text_6, (300,180))

    pygame.draw.circle(screen, BLACK, (250,350), 100)
    pygame.draw.circle(screen, WHITE, (250,350), 95)
    pygame.draw.circle(screen, BLACK, (250,350), 5)

    pygame.draw.rect(screen, BLACK, (50,480,400,50))
    pygame.draw.rect(screen, WHITE, (60,490,380,30))
    

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if(100 < mouse_x < 150) and (50 < mouse_y < 100):
                    total_secs += 60
                    print("press + minute")
                if(200 < mouse_x < 250) and (50 < mouse_y < 100):
                    total_secs += 1
                    print("press + second")
                if(100 < mouse_x < 150) and (180 < mouse_y < 230):
                    total_secs -= 60
                    print("press - minute")
                if(200 < mouse_x < 250) and (180 < mouse_y < 230):
                    total_secs -= 1
                    print("press - second")
                if(300 < mouse_x < 400) and (50 < mouse_y < 100):
                    start = True
                    print("press Start")
                if(300 < mouse_x < 410) and (180 < mouse_y < 230):
                    total_secs = 0
                    print("press Reset")
                print("total_secs: " + str(total_secs))
    if start:
        total_secs -= 1
        if total_secs == 0:
            start = False
        time.sleep(1)
          
    if total_secs < 0:
        total_secs = 0
        
    minute = int(total_secs/60)
    second = total_secs - minute*60
    time_total = str(minute) + " : " + str(second)
    text_time = font.render(time_total, True, BLACK)
    screen.blit(text_time, (135,110))

    x_second = 250 + 90 * math.sin(6 * second * math.pi/180)
    y_second = 350 - 90 * math.cos(6 * second * math.pi/180)
    pygame.draw.line(screen, BLACK, (250,350), (int(x_second),int(y_second)))

    x_minute = 250 + 40 * math.sin(6 * minute * math.pi/180)
    y_minute = 350 - 40 * math.cos(6 * minute * math.pi/180)
    pygame.draw.line(screen, GREEN, (250,350), (int(x_minute),int(y_minute)))

    if total != 0:
        pygame.draw.rect(screen, GREEN, (60,490, int(380 * (total_secs/total)), 30))
    pygame.display.flip()

pygame.quit()
