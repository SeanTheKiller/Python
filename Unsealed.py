import pygame
import sys
import threading
import math
from turtle import Screen, Turtle, done


# ---------- INIT ----------
pygame.init()
WIDTH, HEIGHT = 800, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE | pygame.SCALED)
pygame.display.set_caption("Secret Feelings")
clock = pygame.time.Clock()


# ---------- FONTS ----------
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 48)


# ---------- STATES ----------54
MENU = 0
SCENE_LOGIN = 1
SCENE_STORY = 2
SCENE_PROPOSAL = 3
scene = MENU


# ---------- PASSWORD ----------
user_input = ""
PASSWORD = "iloveher"


# ---------- BACKGROUND ----------
bg_x = 0


# ---------- STORY TEXT ----------
story_lines = [
    "I tried to belong.",
    "I gave more than I had.",
    "Silence was the answer.",
    "So I stopped chasing.",
    "Now I choose myself."
]
current_line = 0
alpha = 0
fade_speed = 2


# ---------- BUTTONS ----------
def draw_button(text, x, y, w, h, color_bg, color_text):
    pygame.draw.rect(screen, color_bg, (x, y, w, h))
    txt = font.render(text, True, color_text)
    screen.blit(txt, (x + w // 2 - txt.get_width() // 2, y + h // 2 - txt.get_height() // 2))
    return pygame.Rect(x, y, w, h)


# ---------- TURTLE HEART ----------
def run_heart():
    # Parametric heart shape
    def hearta(k):
        return 16 * math.sin(k) ** 3


    def heartb(k):
        return 13 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)


    t_screen = Screen()
    t_screen.bgcolor("black")
    t = Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("#f73487")


    # Move to starting point, draw the heart
    t.penup()
    t.goto(hearta(0) * 20, heartb(0) * 20)
    t.pendown()
    for i in range(1, 6000):
        t.goto(hearta(i) * 20, heartb(i) * 20)


    # Write a message centered below the heart
    t.penup()
    t.goto(0, -220)
    t.color("#ffb6c1")
    t.write("Just for you <333", align="center", font=("Arial", 24, "bold"))
    done()


# Run Turtle in separate thread so it doesn't freeze Pygame
def run_heart_thread():
    threading.Thread(target=run_heart, daemon=True).start()


# ---------- MAIN LOOP ----------
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = True


        # -------- LOGIN INPUT --------
        if scene == SCENE_LOGIN and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_RETURN:
                if user_input == PASSWORD:
                    scene = SCENE_STORY
                user_input = ""
            else:
                user_input += event.unicode


        # -------- NEXT STORY LINE --------
        if scene == SCENE_STORY and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_line += 1
                alpha = 0
                if current_line >= len(story_lines):
                    current_line = len(story_lines) - 1


    # ---------- BACKGROUND ----------
    bg_x -= 1
    if bg_x <= -WIDTH:
        bg_x = 0
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (15,15,15), (bg_x,0,WIDTH,HEIGHT))
    pygame.draw.rect(screen, (25,25,25), (bg_x + WIDTH,0,WIDTH,HEIGHT))


    # ---------- MENU ----------
    if scene == MENU:
        btn_story = draw_button("Unsealed", 200, 150, 200, 60, (50,50,50), (255,255,255))
        btn_proposal = draw_button("Proposal", 200, 250, 200, 60, (50,50,50), (255,255,255))
        if mouse_click:
            if btn_story.collidepoint(mouse_pos):
                scene = SCENE_LOGIN
            if btn_proposal.collidepoint(mouse_pos):
                run_heart_thread()
                scene = SCENE_PROPOSAL


    # ---------- LOGIN SCENE ----------
    elif scene == SCENE_LOGIN:
        text = font.render("Enter password: " + user_input, True, (200,200,200))
        screen.blit(text, (50, HEIGHT//2))
        btn_exit = draw_button("Back to Menu", 600, 20, 150, 40, (100,0,0), (255,255,255))
        if mouse_click and btn_exit.collidepoint(mouse_pos):
            scene = MENU
            user_input = ""


    # ---------- STORY SCENE ----------
    elif scene == SCENE_STORY:
        if alpha < 255: alpha += fade_speed
        line_surface = big_font.render(story_lines[current_line], True, (220,220,220))
        line_surface.set_alpha(alpha)
        screen.blit(line_surface, (WIDTH//2 - line_surface.get_width()//2, HEIGHT//2))
        hint = font.render("Press SPACE", True, (120,120,120))
        screen.blit(hint, (WIDTH-160, HEIGHT-40))
        btn_exit = draw_button("Back to Menu", 600, 20, 150, 40, (100,0,0), (255,255,255))
        if mouse_click and btn_exit.collidepoint(mouse_pos):
            scene = MENU
            current_line = 0
            alpha = 0


    # ---------- PROPOSAL SCENE ----------
    elif scene == SCENE_PROPOSAL:
        # Display message and start the heart graphics
        text = big_font.render("Just for you <333", True, (255,150,200))
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 40))
        btn_exit = draw_button("Back to Menu", 600, 20, 150, 40, (100,0,0), (255,255,255))
        if mouse_click and btn_exit.collidepoint(mouse_pos):
            scene = MENU
        else:
            # ensure the heart thread starts when entering the proposal scene
            # (start it once per entry)
            pass


    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()
