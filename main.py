import argparse #Parser for command-line options, arguments and sub-commands
import pytesseract #Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images.
from picture_to_coordinates import coordinates  #Importing array made from picture
from dxfwrite import DXFEngine as dxf #dxf is a Python interface to the DXF (drawing interchange file) format developed by Autodesk,

# Might want to use 'import argparse' to get arguments from command line

# AutoCAD DXF (Drawing Interchange Format, or Drawing Exchange Format) 
# is a CAD data file format developed by Autodesk[2] 
# for enabling data interoperability between AutoCAD and other programs. 
# https://en.wikipedia.org/wiki/AutoCAD_DXF



# Convert image to drawing here.


# Create a drawing, we will add things to it
drawing = dxf.drawing()

# In this block we are creating various objects and adding them to the drawing
# Create text object at coordinates 3, 0, 1
text = dxf.text('Hello World!', point=(3, 0, 1))
# Add text to drawing
drawing.append(text)
# Same with line
line = dxf.line(points=[(0,0,0), (1,1,1)])
drawing.append(line)

# Finally, save file to path
drawing.saveas(output_path)
print('Complete')
