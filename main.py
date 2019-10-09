import PIL  # pip install pillow
import sdxf # pip install sdxf

# Might want to use 'import argparse' to get arguments from command line
input_image_path = 'input.png'
# AutoCAD DXF (Drawing Interchange Format, or Drawing Exchange Format) 
# is a CAD data file format developed by Autodesk[2] 
# for enabling data interoperability between AutoCAD and other programs. 
# https://en.wikipedia.org/wiki/AutoCAD_DXF
output_path = 'output.dxf'
image = PIL.Image.open(input_image_path)
a = numpy.asarray(image)
print('Shape:', a.shape)

# Convert image to drawing here.


# Create a drawing, we will add things to it
drawing = sdxf.Drawing()

# In this block we are creating various objects and adding them to the drawing
# Create text object at coordinates 3, 0, 1
text = sdxf.Text('Hello World!', point=(3, 0, 1))
# Add text to drawing
drawing.append(text)
# Same with line
line = sdxf.Line(points=[(0,0,0), (1,1,1)])
drawing.append(line)

# Finally, save file to path
drawing.saveas(output_path)
print('Complete')
