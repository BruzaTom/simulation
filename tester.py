import pygame
import pygame_gui

pygame.init()

# Set up the display
window_size = (800, 600)
window_surface = pygame.display.set_mode(window_size)
background = pygame.Surface(window_size)
background.fill(pygame.Color('#000000'))

# Set up the manager
manager = pygame_gui.UIManager(window_size)

# Circle button properties
circle_center = (400, 300)
circle_radius = 50
button_color = pygame.Color('#FF0000')

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            distance = ((mouse_pos[0] - circle_center[0]) ** 2 + (mouse_pos[1] - circle_center[1]) ** 2) ** 0.5
            if distance <= circle_radius:
                print("Circle button clicked!")

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    pygame.draw.circle(window_surface, button_color, circle_center, circle_radius)
    manager.draw_ui(window_surface)

    pygame.display.update()

pygame.quit()
