import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

hand = pygame.image.load("images/mickeyclock (1).jpeg").convert_alpha()
hand = pygame.transform.scale(hand, (150, 150))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    rect = hand.get_rect(center=(200, 200))
    screen.blit(hand, rect)

    pygame.display.flip()

pygame.quit()