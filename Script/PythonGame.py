import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Game')
    screen.fill((244, 244, 244))
    ball_image = pygame.image.load('E:/leonwxy/PythonPro/res/1429.jpg')
    screen.blit(ball_image, (50, 50))
    pygame.draw.circle(screen, (255, 0, 0), (100, 100), 50, 0)
    pygame.draw.aaline(screen, (255, 0, 0), (158, 158), (300, 300))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()


