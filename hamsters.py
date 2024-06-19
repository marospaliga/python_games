import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPAWN_INTERVAL = 850  # 5000 milliseconds (5 seconds)
HAMSTER_SIZE = (50, 50)  # New size for the hamster image (width, height)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hamster Click Game")

# Hamster class
class Hamster:
    def __init__(self, image_path, size):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.spawn_random()

    def spawn_random(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Main loop
def main():
    clock = pygame.time.Clock()
    hamster_image_path = "/Users/maros/Documents/images/Drawing-Pin.png"  # Replace with the path to your hamster image

    # Create initial hamster
    hamster = Hamster(hamster_image_path, HAMSTER_SIZE)

    # Set up a custom event for spawning hamsters
    SPAWN_HAMSTER_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_HAMSTER_EVENT, SPAWN_INTERVAL)

    hit_count = 0
    miss_count = 0
    player_clicked = False

    running = True
    game_won = False
    game_lost = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == SPAWN_HAMSTER_EVENT:
                if not player_clicked:
                    game_lost = True
                    miss_count += 1
                hamster = Hamster(hamster_image_path, HAMSTER_SIZE)
                game_won = False  # Reset game state for the new hamster
                game_lost = False
                player_clicked = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                player_clicked = True
                if hamster.rect.collidepoint(event.pos):
                    game_won = True
                    hit_count += 1
                else:
                    game_lost = True
                    miss_count += 1

        screen.fill(WHITE)
        hamster.draw(screen)

        # Display win or lose message
        font = pygame.font.Font(None, 74)
        if game_won:
            text = font.render("You Win!", True, BLACK)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
        elif game_lost:
            text = font.render("You Lose!", True, BLACK)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

        # Display hit and miss counters
        font = pygame.font.Font(None, 36)
        hit_text = font.render(f"Hits: {hit_count}", True, BLACK)
        miss_text = font.render(f"Misses: {miss_count}", True, BLACK)
        screen.blit(hit_text, (10, 10))
        screen.blit(miss_text, (10, 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
