import math

white = (255, 255, 255)
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