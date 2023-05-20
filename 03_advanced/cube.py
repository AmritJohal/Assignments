# ADVANCED ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

"""
CUBE CLASS

1. CREATE an abstract class "Cube" with the functions:
   translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
   All functions store and print out the data in the cube (translate, rotate, scale and color).

2. ADD an __init__(name) and create 3 cube objects.

3. ADD the function print_status() which prints all the variables nicely formatted.

4. ADD the function update_transform(ttype, value).
   "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats.
   This function should trigger either the translate, rotate or scale function.

   BONUS: Can you do it without using ifs?

5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
   Use Object as the parent for your Cube class.
   Update the Cube class to not repeat the content of Object.

"""
class Object:
   translate_value = [0, 0, 0]
   rotate_value = [0, 0, 0]
   scale_value = [1, 1, 1]
  


class Cube(Object):
   color_val = [0, 0, 0]
   
   def __init__(self, name):
      self.name = name


   def translate(self, x, y, z):
      self.translate_value = [x, y, z]
      print(self.translate_value)

   def rotate(self, x, y, z):
      self.rotate_value = [x, y, z]
      print(self.rotate_value)


   def scale(self, x, y, z):
      self.scale_value = [x, y, z]
      print(self.scale_value)


   def colour(self, R, G, B):
      self.colour_value = [R, G, B]
      print(self.colour_value) 

   def print_status(self):
      print(f'\nName: {self.name}')
      print(f'Translation value: {self.translate_value}')
      print(f'Rotate value:      {self.rotate_value}')
      print(f'Scale value:       {self.scale_value}')
   

   def update_transform(self, ttype, value):
      transforms = {'translate' : self.translate,
                     'rotate'    : self.rotate,
                     'scale'     : self.scale}
        
      transforms[ttype](value[0], value[1], value[2])




cube1 = Cube('cube1')
cube2 = Cube('cube2')
cube3 = Cube('cube3')

cube1.print_status()
cube2.print_status()
cube3.print_status()

cube1.translate(1,3,6)
cube1.print_status()
cube1.update_transform('scale', [60, 60, 60])
cube1.print_status()