import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)

# Questions and answers
questions = [
    ("What does CPU stand for?", ["central processing unit", "central processor unit"]),
    ("What does RAM stand for?", ["random access memory", "random-access memory"]),
    ("What does GPU stand for?", ["graphics processing unit", "graphics processor unit"]),
    ("What does HTTP stand for?", ["hypertext transfer protocol", "hyper text transfer protocol"]),
    ("What does HTML stand for?", ["hypertext markup language", "hyper text markup language", "hypertext mark-up language", "hyper text mark-up language"])
]

score = 0
current_question = 0
input_text = ""

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def show_question():
    global input_text
    screen.fill(WHITE)
    if current_question < len(questions):
        question, _ = questions[current_question]
        draw_text(question, font, BLACK, screen, 20, 20)
        draw_text(input_text, font, BLACK, screen, 20, 100)
    else:
        draw_text(f"🎉 You completed the quiz! Your score is {score}/{len(questions)}.", large_font, BLACK, screen, 20, 20)
        if score == len(questions):
            draw_text("🏆 Excellent! You got all the answers correct!", font, GREEN, screen, 20, 150)
        elif score >= 3:
            draw_text("👍 Good job! You got most of the answers correct!", font, GREEN, screen, 20, 150)
        else:
            draw_text("👋 Better luck next time!", font, RED, screen, 20, 150)

def check_answer():
    global score, current_question, input_text
    answer = input_text.strip().lower()
    correct_answers = questions[current_question][1]
    if answer in correct_answers:
        score += 1
    current_question += 1
    input_text = ""

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                check_answer()
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    show_question()
    pygame.display.flip()

pygame.quit()
sys.exit()
