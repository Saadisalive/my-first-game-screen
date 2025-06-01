import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Game Screen")

background_color = (58, 58, 58)

image = pygame.image.load("eagle.png.png")
image = pygame.transform.scale(image, (300, 300))
image_rect = image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill(background_color)
    display_surface.blit(image, image_rect)
    pygame.display.update()

pygame.quit()