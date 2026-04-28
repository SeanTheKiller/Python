from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

# --- Game State & Time ---
time_mult = 0.05
game_paused = False

# --- Levels & Collision ---
ground = Entity(model='plane', scale=100, texture='white_cube', 
               texture_scale=(100,100), color=color.light_gray, collider='box')

# Perimeter Walls
wall_n = Entity(model='cube', scale=(100, 10, 1), z=50, y=5, color=color.white, collider='box')
wall_s = Entity(model='cube', scale=(100, 10, 1), z=-50, y=5, color=color.white, collider='box')
wall_e = Entity(model='cube', scale=(1, 10, 100), x=50, y=5, color=color.white, collider='box')
wall_w = Entity(model='cube', scale=(1, 10, 100), x=-50, y=5, color=color.white, collider='box')

# Second Floor & Stairs
second_floor = Entity(model='cube', scale=(20, 1, 20), x=15, y=5, z=15, 
                      texture='white_cube', color=color.light_gray, collider='box')
stairs = Entity(model='cube', scale=(5, 1, 12), x=15, y=2.5, z=0, 
                rotation_x=-25, texture='white_cube', color=color.gray, collider='box')

# --- NEW: Pillars (Cover) ---
pillar_coords = [(-10, -10), (-10, 10), (5, -15), (25, -10)]
pillars = [Entity(model='cube', scale=(2, 10, 2), x=p[0], z=p[1], y=5, 
                  color=color.white, collider='box') for p in pillar_coords]

# --- Player ---
player = FirstPersonController(model='cube', y=2, color=color.white, speed=10)
player.collider = 'box'

# --- Menu Logic ---
pause_menu = Entity(parent=camera.ui, enabled=False)
menu_bg = Entity(parent=pause_menu, model='quad', scale=(0.6, 0.4), color=color.black66)
menu_text = Text(parent=pause_menu, text='PAUSED', origin=(0,0), y=0.1, scale=2)

def quit_game():
    application.quit()

def resume_game():
    global game_paused
    game_paused = False
    pause_menu.enabled = False
    mouse.locked = True
    application.resume()

quit_button = Button(parent=pause_menu, text='Quit Game', color=color.red, 
                     scale=(0.2, 0.05), y=-0.05, on_click=quit_game)
resume_button = Button(parent=pause_menu, text='Resume', color=color.gray, 
                       scale=(0.2, 0.05), y=0.02, on_click=resume_game)

# --- Classes ---
class Enemy(Entity):
    def __init__(self):
        super().__init__(model='cube', color=color.red, scale=(1, 2, 1), collider='box')
        self.head = Entity(parent=self, model='sphere', y=0.6, scale=0.5, color=color.rgb(100, 0, 0))
        self.respawn()

    def respawn(self):
        self.position = (random.randint(-20, 20), 1, random.randint(-20, 20))
        if random.random() > 0.7:
            self.position = (random.randint(10, 20), 7, random.randint(10, 20))

    def update(self):
        if game_paused: return
        self.look_at_2d(player.position, 'y')
        if distance(self.position, player.position) > 5:
            self.position += self.forward * time_mult * 4 * time.dt

class Bullet(Entity):
    def __init__(self, pos, direction, bullet_color, target):
        super().__init__(model='sphere', scale=0.2, color=bullet_color, position=pos, collider='sphere')
        self.direction = direction
        self.target = target

    def update(self):
        if game_paused: return
        self.position += self.direction * 50 * time.dt * time_mult
        hit = self.intersects()
        if hit.hit:
            if self.target == "enemy" and isinstance(hit.entity, Enemy):
                hit.entity.respawn()
                destroy(self)
            elif self.target == "player" and hit.entity == player:
                player.position = (0, 2, 0)
                destroy(self)
            # Destroy bullet if it hits floor, stairs, walls, or pillars
            else:
                destroy(self)

enemies = [Enemy() for _ in range(6)]

# --- Global Controls ---
def input(key):
    global game_paused
    if key == 'escape':
        game_paused = not game_paused
        pause_menu.enabled = game_paused
        mouse.locked = not game_paused
        if game_paused: application.pause()
        else: application.resume()

    if key == 'left mouse down' and not game_paused:
        Bullet(player.position + Vec3(0,1.5,0), camera.forward, color.black, "enemy")

def update():
    global time_mult
    if game_paused: return
    moving = held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']
    shooting = held_keys['left mouse']
    target_time = 1.0 if (moving or shooting) else 0.03
    time_mult = lerp(time_mult, target_time, time.dt * 10)

app.run()