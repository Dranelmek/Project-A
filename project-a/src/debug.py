import pygame
pygame.init()
font = pygame.font.Font(None, 30)

def debug(info, y=10, x=10):
    """Display debug information on the screen."""
    debug_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    pygame.draw.rect(debug_surface, 'Black', debug_rect)
    debug_surface.blit(debug_surf, debug_rect)