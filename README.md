//USAGE

python3 imagetoascii.py [path to image]

//The resolution of the resulting ascii art can be changed in this function in the imagetoascii file:
//By changing the 'new_height' variable, the resolution of the whole image can be changed.

def resize(image, new_height = 153):
    (width, height) = image.size
    print(width , height)
    ratio = width / height
    new_width = int((ratio * new_height) * 2.288)
    print (new_width)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    print("Resizing Image")
    time.sleep(.1)
    return [new_image, new_width]

//The resulting output file can be viewed in a text editor or web browser
//Unzoom to max to better see the image
