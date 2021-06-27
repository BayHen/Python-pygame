import pygame

pygame.init()

srceen = pygame.display.set_mode((500,500))

GREY = (150,150,150)

running = True

while running:
    srceen.fill(GREY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Hen dep trai");
        pass

    pygame.display.flip()

pygame.quit()
