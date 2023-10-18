import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Render Square")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Square properties
square_size = 100
square_x = (width - square_size) // 2
square_y = (height - square_size) // 2

def convert_degrees_to_2D(degrees):
    radians = math.radians(degrees)
    x = math.cos(radians)
    y = math.sin(radians)
    return x, y


class Cube():
    def __init__(self , x , y , z , width , height , depth , x_rotation , y_rotation , z_rotation):
        self.coordinates = {
            'x' : x,
            'y' : y,
            'z' : z
        }
        
        self.points = {
            "A": {
               "x" : x,
               "y" : y,
               "z" : z 
            },
            "B": {
               "x" : x + width,
               "y" : y,
               "z" : z
            },
            "C": {
               "x" : x + width,
               "y" : y,
               "z" : z + depth
            },
            "D": {
               "x" : x,
               "y" : y,
               "z" : z + depth
            },
            "E": {
               "x" : x,
               "y" : y + height,
               "z" : z
            },
            "F": {
               "x" : x,
               "y" : y + height,
               "z" : z + depth
            }
        }
        
        self.face = {
            "FrontFace": (self.points["A"], self.points["B"], self.points["C"] , self.points["D"]),
            "BackFace": (self.points["E"], self.points["F"], self.points["B"] , self.points["A"]),
            "LeftFace": (self.points["A"], self.points["E"], self.points["D"] , self.points["B"]),
            "RightFace": (self.points["C"], self.points["D"], self.points["F"] , self.points["E"]),
            "TopFace": (self.points["A"], self.points["B"], self.points["F"] , self.points["E"]),
            "BottomFace": (self.points["C"], self.points["D"], self.points["B"] , self.points["A"])
        }
        
        self.vertex = {
            "AB": (self.points["A"], self.points["B"]),
            "BC": (self.points["B"], self.points["C"]),
            "CD": (self.points["C"], self.points["D"]),
            "DA": (self.points["D"], self.points["A"]),
            "BE": (self.points["E"], self.points["B"]),
            "EF": (self.points["F"], self.points["E"]),
            "FD": (self.points["F"], self.points["D"]),
            "DC": (self.points["D"], self.points["C"]),
            "AF": (self.points["A"], self.points["F"]),
            "CE": (self.points["C"], self.points["E"]),
            "BD": (self.points["B"], self.points["D"])
        }
        
        self.rotation = {
            'x' : x_rotation,
            'y' : y_rotation,
            'z' : z_rotation
        }
        


class Camera():
    def __init__(self , x , y , z , width , height , x_rotation , y_rotation):
        self.coordinates = {
            'x' : x,
            'y' : y,
            'z' : z
        }
        self.camera = {
            'width' : width,
            'height' : height,
        }
        self.rotation = {
            'x' : x_rotation,
            'y' : y_rotation,
        }
        
    def render(self, objects):
        for depth in range(125, 0, -1):
            for hight in range(self.camera['width']):
                for width in range(self.camera["height"]):
                    for object in objects:
                        for vertex in object.vertex.keys():
                            if depth in range(object.vertex[vertex][0]['z']-1,object.vertex[vertex][1]['z']+1):
                                if hight in range(object.vertex[vertex][0]['y']-1,object.vertex[vertex][1]['y']+1):
                                    # print((object.vertex[vertex][0]['z'],object.vertex[vertex][1]['z']))
                                    # print(object.vertex[vertex][0]['x']-1,object.vertex[vertex][1]['x']+1)
                                    if width in range(object.vertex[vertex][0]['x']-1,object.vertex[vertex][1]['x']+1):
                                        pygame.draw.rect(screen, white, (width, hight, 1, 1))
                                        break
                                
                            
cube  = Cube(0, 0, 50, 50, 25, 100, 0, 0, 0)
camera = Camera(0, 0, 0, 150, 100, 0, 0)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Render the cube
    camera.render([cube])

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()