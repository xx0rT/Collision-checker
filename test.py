import pygame
pygame.init()
# okno
WINDOWHEIGHT = 600
WINDOWWIDTH = 800
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("My Game")
# fpska
clock = pygame.time.Clock()
clock.tick(60)
# jeden pohybujicise objekt
rect = pygame.Rect(20, 20, 20, 20)
# definuju kazdy obejkt v array listu loopem
object_list = [
    {"color": (255, 0, 0), "rect": pygame.Rect(100, 100, 50, 50)},
    {"color": (0, 255, 0), "rect": pygame.Rect(200, 200, 50, 50)},
    {"color": (0, 0, 255), "rect": pygame.Rect(300, 300, 50, 50)}
]
# staty pro klavesy
key_pressed = False
key_released = False
key_w = False
key_a = False
key_s = False
key_d = False
# hlavni loop aby udrzel hru na zivu
while True:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        # zkontrolovat jesti SDSDSSje klavesa zmackla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                key_w = True
            elif event.key == pygame.K_a:
                key_a = True
            elif event.key == pygame.K_s:
                key_s = True
            elif event.key == pygame.K_d:
                key_d = True

        # zkontrolovat jestli je klavesa vypla
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                key_w = False
            elif event.key == pygame.K_a:
                key_a = False
            elif event.key == pygame.K_s:
                key_s = False
            elif event.key == pygame.K_d:
                key_d = False

    # logika
    if key_w:
        rect.move_ip(0, -10) 
    if key_a:
        rect.move_ip(-10, 0) 
    if key_s:
        rect.move_ip(0, 10)  
    if key_d:
        rect.move_ip(10, 0)  


    # vykresleni obrazovky
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (222, 11, 111), rect)
    pygame.display.update()
    for obj in object_list:
        pygame.draw.rect(screen, obj["color"], obj["rect"])
    pygame.display.flip()
    # limitovat fps
    clock.tick(60)
    #zkontrolovat kolizi
    for obj in object_list:
        if rect.colliderect(obj["rect"]):
            print("Kolize")