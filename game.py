import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (135, 206, 250)  # Sky blue
BUILDING_COLOR = (139, 69, 19)      # Brown
BUILDING_SIZE = (50, 50)
FPS = 30

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Town Building Game")

# Game Variables
buildings = []

def draw_building(x, y):
    pygame.draw.rect(screen, BUILDING_COLOR, pygame.Rect(x, y, BUILDING_SIZE[0], BUILDING_SIZE[1]))

def main():
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Add a building where the mouse is clicked
                x, y = pygame.mouse.get_pos()
                buildings.append((x - BUILDING_SIZE[0] // 2, y - BUILDING_SIZE[1] // 2))
        
        # Fill the background
        screen.fill(BACKGROUND_COLOR)
        
        # Draw all buildings
        for building in buildings:
            draw_building(building[0], building[1])
        
        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()