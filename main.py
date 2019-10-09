import PIL
import sdxf


input_image_path = 'input.png'
output_path = 'output.dxf'
image = PIL.Image.open(input_image_path)
a = numpy.asarray(image)
print('Shape:', a.shape)


# Convert matrix to drawing here.

d = sdxf.Drawing()

text = sdxf.Text(‘Hello World!’,point=(3,0,1))
d.append(text)

line = sdxf.Line(points=[(0,0,0),(1,1,1)])
d.append(line)

d.saveas(output_path)
print('Complete')
