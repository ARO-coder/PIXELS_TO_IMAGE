from PIL import Image, ImageChops

i = Image.open("d.png").convert('RGB')

w,h=i.size

for x in range(w):
    for y in range(h):
    
        r,g,b = i.getpixel((x,y))
        print (r,g,b)
    
    
