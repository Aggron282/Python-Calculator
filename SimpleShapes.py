import math;
from math import pi;

class Square:

    def __init__(self,side):
        self.name = "square"
        self.side = side
        self.choices = [
            {
            "name":"get_area",
            "exec": self.get_area()
            },
            {
            "name": "get_perimeter",
            "exec":self.get_perimeter()
            }
        ]
        self.style = """
        
        - - - - - - - - - -
        -                 -
        -                 -
        -                 -
        -                 -
        -                 -
        - - - - - - - - - - 
        
        """

    def get_area(self):
        return self.side * self.side;

    def get_perimeter(self):
        return self.side * 4;

class Triangle:

    def __init__(self, side,base,height):
        self.name = "triangle"
        self.side = side
        self.base = base
        self.height = height;
        self.choices = [
            {
                "name": "get_area",
                "exec": self.get_area()
            },
            {
                "name": "get_perimeter",
                "exec": self.get_perimeter()
            }
        ]
        self.style = """ 
        
            -
           -  -
          -    -
         -      -
        -        -
       -          -
      -            -
     -              -
    -                -
    - - - - - - - - - -
    
        """

    def get_area(self):
        return (self.base * self.height) / 2;

    def get_perimeter(self):
        return (2 * self.side) + self.height;

class Circle:

    def __init__(self,radius):
        self.name  = "circle"
        self.radius = radius
        self.choices = [
            {
                "name": "get_circumference",
                "exec": self.get_circumference()
            },
            {
                "name": "get_area",
                "exec": self.get_area()
            }
        ]
        self.style = """
                                                                                                             
                                                                          
                                             ----------                                             
                                           --------------                                           
                                          ----------------                                          
                                         ------------------                                         
                                         ------------------                                         
                                         ------------------                                         
                                         ------------------                                         
                                          ----------------                                          
                                            ------------                                            
                                                ----                                                
                                                                                                    
                                                                                                         
                                                                                                    
                                                                
               """

    def get_circumference(self):
        circ = float(self.radius) * float(2);
        return float(pi * circ)

    def get_area(self):
        circ = float(self.radius) ** float(2);
        return pi * circ;

class Rectangle:

    def __init__(self, width,length):
        self.name = "rectangle"
        self.length = length
        self.width = width
        self.choices = [
            {
                "name": "get_area",
                "exec": self.get_area()
            },
            {
                "name": "get_perimeter",
                "exec": self.get_perimeter()
            },
        ]
        self.style = """
        
            - - - - - - - - - - - - 
            -                     -
            -                     -
            -                     -
            -                     -
            -                     -
            -                     -
            -                     -
            -                     -  
            -                     -
            -                     -
            -                     -
            - - - - - - - - - - - - 
            
        """

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (self.width * 2) + (self.length * 2)

class Trapezoid:

    def __init__(self, base_a,base_b,height,length):
        self.name = "trapezoid"
        self.base_a = base_a
        self.base_b = base_b
        self.height = height
        self.length = length
        self.choices = [
            {
                "name": "get_area",
                "exec": self.get_area()
            },
            {
                "name": "get_perimeter",
                "exec": self.get_perimeter()
            },
        ]
        self.style = """
        
            - - - - - - - - - - - - -
           -                          -
          -                            -
         -                              -
        -                                -
       -                                  -
      -                                    -
     -                                      -
   - - - - - - - - - - - - - - - - - - - - - - 
            
        """

    def get_area(self):
        return ((self.base_a + self.base_b) / 2) * self.height

    def get_perimeter(self):
        return self.base_a + self.base_b + self.height + self.length


class SimpleShapes:

    def __init__(self):
        self.name = "simple_shapes"
        self.shapes = [Trapezoid,Circle,Square,Rectangle,Triangle]
        self.created_shape = None,
        self.choices = [
            {
                "name":"Square",
                "exec":self.create_square,
                "prompt":"Enter one value to determine the size of square"
            },
            {
                "name": "Circle",
                "exec": self.create_circle,
                "prompt": "Enter one value to determine the size of circle"
            },
            {
                "name": "Triangle",
                "exec": self.create_triangle,
                "prompt": "Enter 3 values to create triangle 2.side, 3.base 4.height "
            },
            {
                "name": "Rectangle",
                "exec": self.create_rectangle,
                "prompt": "Enter two values to create rectangle, 1.width, 2.length "
            },
            {
                "name":"Trapezoid",
                "exec": self.create_trapezoid,
                "prompt": "Enter four values to create trapezoid, 1.base_a 2.base_b 3.height 4.length"
            }
        ]

    def show_choices(self):
        prompt = input("Select Following Shapes:"+self.shapes)
        chosen_shape = self.find_shape(prompt);
        print(chosen_shape.style + "\n");
        print("Select following options for shape: "+ chosen_shape.choices)

    def find_shape(self,chosen_shape):
        for shape in self.shapes:
            if(shape.lower() == chosen_shape.lower()):
                return shape

    def create_rectangle(self,values):
        print(values);
        if self.validate_numbers(values) == False or len(values) < 2:
            print("Invalid Input");
            return;

        self.created_shape = Rectangle(values[0],values[1])
        print(self.created_shape.style)
        print(f"You have created square with width of {values[0]}, and length of {values[1]} \n")

    def create_circle(self,values):
        if self.validate_numbers(values) == False or len(values) < 1:
            print("Invalid Input");
            return;

        self.created_shape = Circle(values[0])

        print(self.created_shape.style)
        print(f"You have created circle with a radius of {values[0]} \n")

    def create_square(self,values):
        if self.validate_numbers(values) == False or len(values) < 1:
            print("Invalid Input");
            return;

        self.created_shape = Square(values[0])

        print(self.created_shape.style)
        print(f"You have created square with sides of {values[0]} \n")

    def create_trapezoid(self,values):
        if self.validate_numbers(values) == False or len(values) < 4:
            print("Invalid Input");
            return;

        self.created_shape = Trapezoid(values[0],values[1],values[2],values[3])

        print(self.created_shape.style)
        print(f"You have created a trapezoid with the base_a of {values[0]}, and the base_b of {values[1]}, and the length of {values[2]} \n and the height of {values[3]} \n")


    def create_triangle(self, values):

        if self.validate_numbers(values) == False or len(values) < 2:
            print("Invalid Input");
            return;

        self.created_shape = Triangle(values[0],values[1],values[2])

        print(self.created_shape.style)
        print(f"You have created a triangle with the height of {values[0]}, and the side length of {values[1]} \n")

    def validate_numbers(self,values):
        for value in values:
            if isinstance(value, (int,float)) == False:
                return False;
        return True;

    def execute_choice(self, choice):

            for choice_ in self.choices:

                if choice_.get("name").strip().lower() == choice.strip().lower():

                    prompt = input(choice_.get("prompt") + "\n")
                    exec_ = choice_.get("exec")
                    values = prompt.split(" ");
                    values_ = []
                    for value in values:

                        if len(value) == 0:
                            pass;
                        else:
                            value_ = float(value);
                            values_.append(value_);
                    print(values_);
                    exec_(values_)
                    print("---------------------------------------------------------------------------- \n");
                    self.show_shape_choices();

    def show_shape_choices(self):
        if not self.created_shape:
            print("No Shape Chosen");
            return;

        print("Choose which calculation for the shape you want")

        for choice in self.created_shape.choices:

            print(choice.get("name"));
            print("__________________________")

        calc_prompt = input("Choose which calculation you would like \n");

        for calc_choice in self.created_shape.choices:

            if calc_prompt.strip().lower() == calc_choice.get("name").strip().lower():
                answer = calc_choice.get("exec");
                print(f"The {calc_choice.get('name')} for the shape {self.created_shape.name} is {answer}");

