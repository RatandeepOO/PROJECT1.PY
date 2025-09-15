import pygame
import random
import sys

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen setup
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake-Water-Gun Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FLASH_COLORS = [(255, 69, 0), (50, 205, 50), (65, 105, 225), (255, 165, 0), (138, 43, 226)]

# Fonts
font_big = pygame.font.SysFont("Arial", 40, bold=True)
font_small = pygame.font.SysFont("Arial", 28)

# Load images
snake_img = pygame.image.load("assets/snake.png")
water_img = pygame.image.load("assets/water.png")
gun_img = pygame.image.load("assets/gun.png")

# Resize images
snake_img = pygame.transform.scale(snake_img, (80, 80))
water_img = pygame.transform.scale(water_img, (80, 80))
gun_img = pygame.transform.scale(gun_img, (80, 80))

images = {"Snake": snake_img, "Water": water_img, "Gun": gun_img}
choice_values = {"Snake": 1, "Water": -1, "Gun": 0}
choices = ["Snake", "Water", "Gun"]

# Load sounds
click_sound = pygame.mixer.Sound("assets/click.wav")
win_sound = pygame.mixer.Sound("assets/win.wav")
lose_sound = pygame.mixer.Sound("assets/lose.wav")

# Button positions
button_rects = {
    "Snake": pygame.Rect(80, 400, 150, 50),
    "Water": pygame.Rect(270, 400, 150, 50),
    "Gun": pygame.Rect(460, 400, 150, 50)
}

# Scores and result
player_score = 0
computer_score = 0
result_text = ""
animation_counter = 0
show_countdown = False
countdown_text = ""
computer_choice_img = None
particles = []

def determine_winner(player_choice, computer_choice):
    global player_score, computer_score
    if player_choice == computer_choice:
        return "Draw!"
    elif (player_choice == 1 and computer_choice == -1) or \
         (player_choice == -1 and computer_choice == 0) or \
         (player_choice == 0 and computer_choice == 1):
        player_score += 1
        create_particles((350, 250), (50, 205, 50))
        win_sound.play()
        return "You Win! 😍"
    else:
        computer_score += 1
        create_particles((350, 250), (220, 20, 60))
        lose_sound.play()
        return "You Lose! 🤣"

def create_particles(position, color):
    for _ in range(30):
        x = position[0]
        y = position[1]
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)
        particles.append({"pos": [x, y], "vel": [dx, dy], "color": color, "life": 20})

def update_particles():
    for p in particles[:]:
        p["pos"][0] += p["vel"][0]
        p["pos"][1] += p["vel"][1]
        p["life"] -= 1
        if p["life"] <= 0:
            particles.remove(p)
        else:
            pygame.draw.circle(screen, p["color"], (int(p["pos"][0]), int(p["pos"][1])), 5)

def start_countdown(choice):
    global show_countdown, animation_counter, selected_choice
    show_countdown = True
    animation_counter = 0
    selected_choice = choice
    click_sound.play()

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
    # Draw heading
    heading = font_big.render("Snake-Water-Gun", True, BLACK)
    screen.blit(heading, (WIDTH//2 - heading.get_width()//2, 20))
    
    # Draw buttons with images
    for choice, rect in button_rects.items():
        pygame.draw.rect(screen, FLASH_COLORS[choices.index(choice)], rect, border_radius=10)
        img = images[choice]
        screen.blit(img, (rect.x + rect.width//2 - 40, rect.y - 90))  # place image above button
        text = font_small.render(choice, True, WHITE)
        screen.blit(text, (rect.x + rect.width//2 - text.get_width()//2,
                           rect.y + rect.height//2 - text.get_height()//2))
    
    # Display scores
    score_text = font_small.render(f"Score - You: {player_score}  Computer: {computer_score}", True, BLACK)
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 100))
    
    # Countdown animation
    if show_countdown:
        if animation_counter < 3:
            countdown_words = ["Snake...", "Water...", "Gun..."]
            screen.fill(FLASH_COLORS[animation_counter])
            countdown_text = font_big.render(countdown_words[animation_counter], True, WHITE)
            screen.blit(countdown_text, (WIDTH//2 - countdown_text.get_width()//2, HEIGHT//2 - 50))
            pygame.display.flip()
            pygame.time.delay(500)
            animation_counter += 1
        else:
            show_countdown = False
            player_choice = choice_values[selected_choice]
            comp_choice_name = random.choice(choices)
            comp_choice = choice_values[comp_choice_name]
            computer_choice_img = images[comp_choice_name]
            result_text = f"You chose: {selected_choice} | Computer chose: {comp_choice_name} || {determine_winner(player_choice, comp_choice)}"
    
    # Display result text
    if result_text:
        color = (50, 205, 50) if "Win" in result_text else (220, 20, 60) if "Lose" in result_text else (138, 43, 226)
        result_display = font_small.render(result_text, True, color)
        screen.blit(result_display, (WIDTH//2 - result_display.get_width()//2, 250))
    
    # Display computer choice image
    if computer_choice_img:
        screen.blit(computer_choice_img, (WIDTH//2 - 40, 300))
    
    # Update particle effects
    update_particles()
    
    pygame.display.flip()
    clock.tick(60)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not show_countdown:
            pos = pygame.mouse.get_pos()
            for choice, rect in button_rects.items():
                if rect.collidepoint(pos):
                    start_countdown(choice)

pygame.quit()
sys.exit()
