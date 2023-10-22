import pygame
from lib import Cube
import sys
import pickle
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN_LOW = (0, 100, 0)
GREEN = (0, 200, 0)
WHITE_LOW = (55, 55, 55)
BLUE = (0, 0, 255)
BRAWN = (165, 42, 42)

colors_list = [BLACK, RED, GREEN_LOW, GREEN, WHITE_LOW, BLUE, BRAWN]

def draw_grid(screen, color, line_width):
    # Draw vertical lines
    for x in range(0, WIDTH, line_width):
        pygame.draw.line(screen, color, (x, 0), (x, HEIGHT))

    # Draw horizontal lines
    for y in range(0, HEIGHT, line_width):
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))


# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Dot Game")

class LevelLayOut:
    def __init__(self, screen, color, line_width):
        self.screen = screen
        self.color = color
        self.line_width = line_width
        self.objects = []
        self.object = {
            'A': [],
            'B': [],
        }
    
    def add_point(self, x, y):
        # check if the point is already in the list
        if len(self.object['A']) == 2 and len(self.object['B']) == 2:
            self.objects.append(self.object)
            self.object = {
                'A': [],
                'B': [],
            }
        else:
            for key in self.object:
                if len(self.object[key]) < 2:
                    self.object[key].append(x)
                    self.object[key].append(y)
                    break
            print(self.object)
            if len(self.object['A']) == 2 and len(self.object['B']) == 2:
                self.objects.append(self.object)
                self.object = {
                    'A': [],
                    'B': [],
                }
            
    def draw(self):
        for point in self.object.values():
            if len(point) == 2:
                pygame.draw.circle(self.screen, GREEN_LOW, (point[0], point[1]), 5)
        for obj in self.objects:
            if obj['A'][0] > obj['B'][0]:
                obj['A'][0], obj['B'][0] = obj['B'][0], obj['A'][0]
            if obj['A'][1] > obj['B'][1]:
                obj['A'][1], obj['B'][1] = obj['B'][1], obj['A'][1]
            pygame.draw.rect(self.screen, GREEN_LOW, (obj['A'][0], obj['A'][1], obj['B'][0] - obj['A'][0], obj['B'][1] - obj['A'][1]), 2)

    def save(self):
        objects = []
        for obj in self.objects:
            color = random.choice(colors_list)
            cube = Cube(0,0,0, 0,0,0, 0,0,0, color)
            # x == hight
            cube.points["A"] = {"y": 0, "x": obj['A'][0] , "z": obj['A'][1]}
            cube.points["B"] = {"y": 500, "x": obj['A'][0] , "z": obj['A'][1]},
            cube.points["C"] = {"y": 500, "x": obj['B'][0], "z": obj['A'][1]}
            cube.points["D"] = {"y": 0, "x": obj['B'][0], "z": obj['A'][1]}
            cube.points["E"] = {"y": 0, "x": y, "z": obj['B'][1]}
            cube.points["F"] = {"y": 500, "x": y, "z": obj['B'][1]}
            cube.points["G"] = {"y": 500, "x": obj['B'][0], "z": obj['B'][1]}
            cube.points["H"] = {"y": 0, "x": obj['B'][0], "z": obj['B'][1]}
            
            cube.face = {
                "FrontFace": (cube.points["A"], cube.points["B"], cube.points["C"] , cube.points["D"]),
                "BackFace": (cube.points["E"], cube.points["F"], cube.points["B"] , cube.points["A"]),
                "LeftFace": (cube.points["A"], cube.points["E"], cube.points["D"] , cube.points["B"]),
                "RightFace": (cube.points["C"], cube.points["D"], cube.points["F"] , cube.points["E"]),
                "TopFace": (cube.points["A"], cube.points["B"], cube.points["F"] , cube.points["E"]),
                "BottomFace": (cube.points["C"], cube.points["D"], cube.points["B"] , cube.points["A"])
            }
            
            cube.vertex = {
                "AB": (cube.points["A"], cube.points["B"]),
                "AC": (cube.points["A"], cube.points["C"]),
                "AD": (cube.points["A"], cube.points["D"]),
                "AE": (cube.points["A"], cube.points["E"]),
                "AF": (cube.points["A"], cube.points["F"]),
                "AG": (cube.points["A"], cube.points["G"]),
                "AH": (cube.points["A"], cube.points["H"]),
                "BC": (cube.points["B"], cube.points["C"]),
                "BD": (cube.points["B"], cube.points["D"]),
                "BE": (cube.points["B"], cube.points["E"]),
                "BF": (cube.points["B"], cube.points["F"]),
                "BG": (cube.points["B"], cube.points["G"]),
                "BH": (cube.points["B"], cube.points["H"]),
                "CD": (cube.points["C"], cube.points["D"]),
                "CE": (cube.points["C"], cube.points["E"]),
                "CF": (cube.points["C"], cube.points["F"]),
                "CG": (cube.points["C"], cube.points["G"]),
                "CH": (cube.points["C"], cube.points["H"]),
                "DE": (cube.points["D"], cube.points["E"]),
                "DF": (cube.points["D"], cube.points["F"]),
                "DG": (cube.points["D"], cube.points["G"]),
                "DH": (cube.points["D"], cube.points["H"]),
                "EF": (cube.points["E"], cube.points["F"]),
                "EG": (cube.points["E"], cube.points["G"]),
                "EH": (cube.points["E"], cube.points["H"]),
                "FG": (cube.points["F"], cube.points["G"]),
                "FH": (cube.points["F"], cube.points["H"]),
                "GH": (cube.points["G"], cube.points["H"])
            }
            objects.append(cube)
        print(objects)
        return objects       

layout = LevelLayOut(screen, GREEN, 5)


# Main loop
running = True
while running:
    # Fill the screen with black
    screen.fill(BLACK)
    draw_grid(screen, WHITE_LOW, 25)
    pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 2), 5)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Capture mouse clicks and add the click position as a point
                x, y = event.pos
                layout.add_point(x,y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                obj = layout.save()
                pickle.dump(obj, open("map", "wb"))
                

    # Draw a red dot in the center
    layout.draw()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()