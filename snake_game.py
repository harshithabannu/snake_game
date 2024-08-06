import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
BLOCK_SIZE = 20

# Set up some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the snake and food
def reset_game():
    global snake, food, direction, score
    snake = [(200, 200), (220, 200), (240, 200)]
    food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
            random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
    direction = "right"
    score = 0

reset_game()

# Set up the direction
direction = "right"

# Set up the score
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            elif event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_SPACE:
                # Pause the game
                paused = True
                while paused:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                paused = False

    # Move the snake
    head = snake[-1]
    if direction == "up":
        new_head = (head[0], head[1] - BLOCK_SIZE)
    elif direction == "down":
        new_head = (head[0], head[1] + BLOCK_SIZE)
    elif direction == "left":
        new_head = (head[0] - BLOCK_SIZE, head[1])
    elif direction == "right":
        new_head = (head[0] + BLOCK_SIZE, head[1])
    snake.append(new_head)

    # Check for collision with food
    if snake[-1] == food:
        food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
        score += 1
    else:
        snake.pop(0)

    # Check for collision with self or edge
    if (snake[-1][0] < 0 or snake[-1][0] >= WIDTH or
        snake[-1][1] < 0 or snake[-1][1] >= HEIGHT or
        snake[-1] in snake[:-1]):
        # Game over screen
        screen.fill(WHITE)
        text = font.render("Game Over! Press space to restart.", True, RED)
        screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 18))
        pygame.display.flip()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        reset_game()
                        break
                elif event.type == pygame.QUIT:
                    running = False

    # Draw everything
    screen.fill(WHITE)
    for pos in snake:
        pygame.draw.rect(screen, GREEN, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(10 + score)  # Increase speed with score

pygame.quit()
sys.exit()
