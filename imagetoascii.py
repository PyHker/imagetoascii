import webbrowser
from PIL import Image
import time
import os



ASCII_CHARS = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', ',', '"', ',', '^', '`', '.' , ' '] #65 levels of darkness
#ASCII_CHARS = ['.',',',':',';','+','*','?','%','S','#','@'] #11 levels of darkness
#\/\/\/\/ Uncomment the statement below to use the 11 level of brightness above 
ASCII_CHARS = ASCII_CHARS[::-1]

#resizes the image

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
    

#def resize(image, new_width=622):
 #   (width, height) = image.size
 #   ratio = 153 / 622
 #   new_height = int(ratio * new_width)
 #   new_dim = (new_width, new_height)
 #   new_image = image.resize(new_dim)
 #   print("Resizing Image")
 #  time.sleep(.1)
 #   return new_image
    
#turns the image gray
def imgtogray(image):
    print("Converting Image to Grayscale")
    time.sleep(.2)
    return image.convert('L')

#converts pixel in grayed image to corresponding ascii character with the same value
def modify(image):
    pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//4] for pixel_value in pixels]
    print("Turning Grayscaled Image to Ascii Picture")
    time.sleep(.2)
    return ''.join(new_pixels)


#does all the function above
def doall(image):
    image, new_width = resize(image)
    image = imgtogray(image)
    pixels = modify(image)
    len_pixels = len(pixels)
    new_image = [pixels[index:index+new_width] for index in range(0, len_pixels, new_width)]
    return '\n'.join(new_image)
    
#takes the path and uses it in the doall() function above
def results(path):
    image = None
    try:
        image = Image.open(path)
    except Exception:
        print("Unable to find image in",path)
        exit()
        return
    image = doall(image)
    
    with open("ascii_image_text", "w") as f:
        print("Saving Ascii Image on ascii_image_text.txt")
        time.sleep(.2)
        f.write(image)
        f.close
        
#takes the path from the console
if __name__ == '__main__':
    import sys
    import urllib.request
    path = sys.argv[1]
    results(path)
    user = str(input("Would you like to look at the photo? (y/N) :"))
    if user == "y":
        webbrowser.open_new_tab('/home/pyhker/python/ascii_image_text')
        #Can be replaced to the directory of your file
    else:
        os.system("figlet Edi NO!!! | lolcat")
        
#No, it was not fun but it's worth it
