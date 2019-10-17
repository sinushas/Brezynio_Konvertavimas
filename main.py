import argparse #Parser for command-line options, arguments and sub-commands
import pytesseract #Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images.
import pillow_works  #Pillow library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.
import ezdxf #ezdxf is a Python interface to the DXF (drawing interchange file) format developed by Autodesk,
#             it allows developers to read and modify existing DXF drawings or create new DXF drawings.
import numpy #NumPy is the fundamental package for scientific computing with Python


# Might want to use 'import argparse' to get arguments from command line

# AutoCAD DXF (Drawing Interchange Format, or Drawing Exchange Format) 
# is a CAD data file format developed by Autodesk[2] 
# for enabling data interoperability between AutoCAD and other programs. 
# https://en.wikipedia.org/wiki/AutoCAD_DXF


a = numpy.asarray(image)
print('Shape:', a.shape)

# Convert image to drawing here.


# Create a drawing, we will add things to it
drawing = ezdxf.Drawing()

# In this block we are creating various objects and adding them to the drawing
# Create text object at coordinates 3, 0, 1
text = ezdxf.Text('Hello World!', point=(3, 0, 1))
# Add text to drawing
drawing.append(text)
# Same with line
line = ezdxf.Line(points=[(0,0,0), (1,1,1)])
drawing.append(line)

# Finally, save file to path
drawing.saveas(output_path)
print('Complete')
