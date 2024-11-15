# This is a simple Pong game using Pygame
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
BALL_RADIUS = 7
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Clock to control the frame rate
clock = pygame.time.Clock()

# Player paddles
paddle_a = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_b = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)
ball_speed_x = 5
ball_speed_y = 5

# Score
score_a = 0
score_b = 0
font = pygame.font.Font(None, 36)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle_b.y -= 5
    if keys[pygame.K_DOWN]:
        paddle_b.y += 5
    if keys[pygame.K_w]:
        paddle_a.y -= 5
    if keys[pygame.K_s]:
        paddle_a.y += 5

    # Keep paddles on the screen
    if paddle_b.y <= 0:
        paddle_b.y = 0
    if paddle_b.y >= HEIGHT - PADDLE_HEIGHT:
        paddle_b.y = HEIGHT - PADDLE_HEIGHT
    if paddle_a.y <= 0:
        paddle_a.y = 0
    if paddle_a.y >= HEIGHT - PADDLE_HEIGHT:
        paddle_a.y = HEIGHT - PADDLE_HEIGHT

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collision with paddles
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x = -ball_speed_x

    # Collision with top and bottom
    if ball.y <= 0 or ball.y >= HEIGHT - BALL_RADIUS:
        ball_speed_y = -ball_speed_y

    # Scoring
    if ball.x <= 0:
        score_b += 1
        ball.x = WIDTH // 2 - BALL_RADIUS // 2
        ball.y = HEIGHT // 2 - BALL_RADIUS // 2
        ball_speed_x = -ball_speed_x
    if ball.x >= WIDTH:
        score_a += 1
        ball.x = WIDTH // 2 - BALL_RADIUS // 2
        ball.y = HEIGHT // 2 - BALL_RADIUS // 2
        ball_speed_x = -ball_speed_x

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.rect(screen, WHITE, paddle_a)
    pygame.draw.rect(screen, WHITE, paddle_b)

    # Draw the net
    for y in range(0, HEIGHT, 10):
        pygame.draw.line(screen, WHITE, (WIDTH // 2, y), (WIDTH // 2, y + 5))

    # Draw the score
    score_text = font.render(f"{score_a} - {score_b}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)
 # Import the necessary libraries
