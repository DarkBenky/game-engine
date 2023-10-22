import pygame
import sys
import math
import pickle
from itertools import combinations

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 1000, 800
width_center, height_center =  height // 2, width // 2 -250
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Render Square")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)



class Cube():
    def __init__(self , x , y , z , width , height , depth , x_rotation , y_rotation , z_rotation , color = white):
        self.color = color
        self.coordinates = {
            'x' : x,
            'y' : y,
            'z' : z,
            'center_x': (x + x + width // 2),
            'center_y': (y + y + height // 2),
            'center_z': (z + z + depth // 2)
        }
        
        self.dimensions = {
            'width' : width,
            'height' : height,
            'depth' : depth
        }
    
        self.points = {
            "A": {"x": x, "y": y, "z": z},
            "B": {"x": x + width, "y": y, "z": z},
            "C": {"x": x + width, "y": y + height, "z": z},
            "D": {"x": x, "y": y + height, "z": z},
            "E": {"x": x, "y": y, "z": z + depth},
            "F": {"x": x + width, "y": y, "z": z + depth},
            "G": {"x": x + width, "y": y + height, "z": z + depth},
            "H": {"x": x, "y": y + height, "z": z + depth},
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
            "AC": (self.points["A"], self.points["C"]),
            "AD": (self.points["A"], self.points["D"]),
            "AE": (self.points["A"], self.points["E"]),
            "AF": (self.points["A"], self.points["F"]),
            "AG": (self.points["A"], self.points["G"]),
            "AH": (self.points["A"], self.points["H"]),
            "BC": (self.points["B"], self.points["C"]),
            "BD": (self.points["B"], self.points["D"]),
            "BE": (self.points["B"], self.points["E"]),
            "BF": (self.points["B"], self.points["F"]),
            "BG": (self.points["B"], self.points["G"]),
            "BH": (self.points["B"], self.points["H"]),
            "CD": (self.points["C"], self.points["D"]),
            "CE": (self.points["C"], self.points["E"]),
            "CF": (self.points["C"], self.points["F"]),
            "CG": (self.points["C"], self.points["G"]),
            "CH": (self.points["C"], self.points["H"]),
            "DE": (self.points["D"], self.points["E"]),
            "DF": (self.points["D"], self.points["F"]),
            "DG": (self.points["D"], self.points["G"]),
            "DH": (self.points["D"], self.points["H"]),
            "EF": (self.points["E"], self.points["F"]),
            "EG": (self.points["E"], self.points["G"]),
            "EH": (self.points["E"], self.points["H"]),
            "FG": (self.points["F"], self.points["G"]),
            "FH": (self.points["F"], self.points["H"]),
            "GH": (self.points["G"], self.points["H"])
        }
        
        self.rotation = {
            'x' : x_rotation,
            'y' : y_rotation,
            'z' : z_rotation
        }
    
    
    def rotate(self, x_rotation, y_rotation, z_rotation):
        x_offset, y_offset, z_offset = 0, 0, 0

        # Translate the object to the origin
        for point in self.points:
            self.points[point]['x'] -= x_offset
            self.points[point]['y'] -= y_offset
            self.points[point]['z'] -= z_offset

        if x_rotation != 0:
            # Apply the rotation around the x-axis
            for point in self.points:
                y = self.points[point]['y']
                z = self.points[point]['z']
                self.points[point]['y'] = y * math.cos(math.radians(x_rotation)) - z * math.sin(math.radians(x_rotation))
                self.points[point]['z'] = y * math.sin(math.radians(x_rotation)) + z * math.cos(math.radians(x_rotation))

        if y_rotation != 0:
            # Apply the rotation around the y-axis
            for point in self.points:
                x = self.points[point]['x']
                z = self.points[point]['z']
                self.points[point]['x'] = x * math.cos(math.radians(y_rotation)) + z * math.sin(math.radians(y_rotation))
                self.points[point]['z'] = -x * math.sin(math.radians(y_rotation)) + z * math.cos(math.radians(y_rotation))

        if z_rotation != 0:
            # Apply the rotation around the z-axis
            for point in self.points:
                x = self.points[point]['x']
                y = self.points[point]['y']
                self.points[point]['x'] = x * math.cos(math.radians(z_rotation)) - y * math.sin(math.radians(z_rotation))
                self.points[point]['y'] = x * math.sin(math.radians(z_rotation)) + y * math.cos(math.radians(z_rotation))

        # Translate the object back to its original position
        for point in self.points:
            self.points[point]['x'] += x_offset
            self.points[point]['y'] += y_offset
            self.points[point]['z'] += z_offset
    def update_all_data(self , x , y , z):
        self.coordinates['x'] += x
        self.coordinates['y'] += y
        self.coordinates['z'] += z
        
        self.coordinates['center_x'] += x
        self.coordinates['center_y'] += y
        self.coordinates['center_z'] += z
        
        for point in self.points:
            self.points[point]['x'] += x
            self.points[point]['y'] += y
            self.points[point]['z'] += z
            self.points[point]['x'] += x
            self.points[point]['y'] += y
            self.points[point]['z'] += z
    
    def check_if_point_in(self , point):
        x, y, z = point['x'], point['y'], point['z']
        print(x, y, z)
        print(self.points['A']['x'] , self.points['B']['x'], 'and point is' , x)
        print(self.points['A']['y'] , self.points['G']['y'], 'and point is' , y)
        print(self.points['A']['z'] , self.points['E']['z'], 'and point is' , z)
        if (
            self.points['A']['x'] <= x <= self.points['B']['x'] and
            self.points['A']['y'] <= y <= self.points['D']['y'] and
            self.points['A']['z'] <= z <= self.points['H']['z']
        ):
            print("True")
            return True
        return False

def calculate_distance(point1, point2):
    # check if the points are behind the camera
    if point1['z'] < 0 or point2['z'] < 0:
        return -math.sqrt((point1['x'] - point2['x'])**2 + (point1['y'] - point2['y'])**2 + (point1['z'] - point2['z'])**2)
    return math.sqrt((point1['x'] - point2['x'])**2 + (point1['y'] - point2['y'])**2 + (point1['z'] - point2['z'])**2)


class Camera():
    def __init__(self , x , y , z):
        self.coordinates = {
            'x' : x,
            'y' : y,
            'z' : z
        }
        
    def render(self, objects):
        distances = {}
        for obj in objects:
            for point in obj.points:
                distance = (obj.points[point]['z'] - self.coordinates['z'])
                distance_ = calculate_distance(obj.points[point], self.coordinates)
                print(distance , "distance")
                distances[obj] = (distance , distance_)
                
                
        
        sorted_distances = sorted(distances.items(), key=lambda x: x[1])
        
        for obj in sorted_distances:
            if distances[obj[0]]:
                scaled_points = []
                color_strength = []
                lines_strength = []
                for point in obj[0].points:
                    
                    s = 3/(1+distances[obj[0]][0]/2001)
                    strength = (1 / (distances[obj[0]][0] / 500))
                    
                    color = list(obj[0].color)
                    for i in range(3):
                        color[i] = int(color[i] * strength)
                        if color[i] < 0:
                            color[i] = 0
                        elif color[i] > 255:
                            color[i] = 255
                    
                    color_strength.append(color)
                    
                    line_strength = int(1 + math.sqrt(distances[obj[0]][1] * (math.sqrt(distances[obj[0]][1]) / 3000)))
                    lines_strength.append(line_strength)
                     
                    x = obj[0].points[point]['x'] * s + width_center
                    y = obj[0].points[point]['y'] * s + height_center
                    
                    scaled_points.append((x, y))
                
                combinations_list = list(combinations(scaled_points, 3))

                for i in range(len(combinations_list)):
                    pygame.draw.polygon(screen, color_strength[0], combinations_list[i])

                for i in range(len(scaled_points)):
                    for j in range(len(scaled_points)):
                        pygame.draw.line(screen, black , scaled_points[i], scaled_points[j], lines_strength[i])
                        
                            
    def move(self,option, objects):
        if option == "Forward":
            test = True
            cor = self.coordinates.copy()
            cor['z'] += 10
            for obj in objects:
                if obj.check_if_point_in(cor):
                    test = False
                    break
            if test:
                for obj in objects:
                    obj.update_all_data(0, 0, 10)
            else:
                for obj in objects:
                    obj.update_all_data(0, 0, -100)
                    
        elif option == "Backward":
            test = True
            cor = self.coordinates.copy()
            cor['z'] -= 10
            for obj in objects:
                if obj.check_if_point_in(cor):
                    test = False
                    break
            if test:
                for obj in objects:
                    obj.update_all_data(0, 0, -10)
            else:
                for obj in objects:
                    obj.update_all_data(0, 0, 100)
                    
        elif option == "Left":
            test = True
            cor = self.coordinates.copy()
            cor['x'] -= 10
            for obj in objects:
                if obj.check_if_point_in(cor):
                    test = False
                    break
            if test:
                for obj in objects:
                    obj.update_all_data(-10, 0, 0)
            else:
                for obj in objects:
                    obj.update_all_data(10, 0, 0)
                
        elif option == "Right":
            test = True
            cor = self.coordinates.copy()
            cor['x'] += 10
            for obj in objects:
                if obj.check_if_point_in(cor):
                    test = False
                    break
            if test:
                for obj in objects:
                    obj.update_all_data(10, 0, 0)
            else:
                for obj in objects:
                    obj.update_all_data(-10, 0, 0)


    def rotate(self,option, objects):
        for obj in objects:
            if option == "Q":
                obj.rotate(0, 2, 0)
            elif option == "E":
                obj.rotate(0, -2, 0)
                        
cube = Cube(400, 0, 100, 500, 500, 100, 0, 0, 0, red)
cube2 = Cube(200, 200, 500, 100, 100, 100, 0, 0, 0, green)
cube3 = Cube(200, 0, 120, 100, 100, 100, 0, 0, 0, blue)
cube4 = Cube(0, 0, 200, 400, 500, 100, 0, 0, 0, white)
# objects = [cube, cube2, cube3, cube4]
objects = [cube4 , cube2]#

# objects = pickle.load(open("map", "rb"))
# for obj in objects:
#     for point in obj.points.keys():
#         try:
#             obj.points[point] = (obj.points[point][0])
#         except:
#             pass


camera = Camera(0, 0, 0)


key_states = {
    pygame.K_w: False,
    pygame.K_s: False,
    pygame.K_a: False,
    pygame.K_d: False,
    pygame.K_q: False,
    pygame.K_e: False,
}

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in key_states:
                key_states[event.key] = True
        if event.type == pygame.KEYUP:
            if event.key in key_states:
                key_states[event.key] = False         

    if key_states[pygame.K_w]:
        camera.move("Backward", objects=objects)
    if key_states[pygame.K_s]:
        camera.move("Forward", objects=objects)
    if key_states[pygame.K_a]:
        camera.move("Right", objects=objects)
    if key_states[pygame.K_d]:
        camera.move("Left", objects=objects)
    if key_states[pygame.K_q]:
        camera.rotate("Q" , objects=objects)
    if key_states[pygame.K_e]:
        camera.rotate("E" , objects=objects)

    # Clear the screen
    screen.fill(black)
    
    # Render the cube
    camera.render(objects=objects)

    # Update the display
    pygame.display.update()
    # set fps
    pygame.time.Clock().tick(24)

# Quit Pygame
pygame.quit()
sys.exit()