import cv2, argparse
import numpy as np

# info on how this works on the readme

pico_colors = [
    (0, 0, 0), # black
    (29, 43, 83), # dark blue
    (126, 37, 83), # purple
    (0, 135, 81), # dark green
    (171, 82, 54), # brown
    (95, 87, 79), # dark gray
    (194, 195, 199), # light gray
    (255, 241, 232), # white
    (255, 0, 77), # magenta
    (255, 163, 0), # gold
    (255, 236, 39), # yellow
    (0, 228, 54), # green
    (41, 173, 255), # blue
    (131, 118, 156), # cyan
    (255, 119, 168), # pink
    (255, 204, 170) # skin
]

# finds the nearest color from a list to a given color - credit to stack overflow (:
def closest_color(colors,color):
    colors = np.array(colors)
    color = np.array(color)
    distances = np.sqrt(np.sum((colors-color)**2,axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    smallest_distance = colors[index_of_smallest]
    return index_of_smallest[0][0]

# converts a number 0-15 to hexadecimal
def to_hex(x):
    if x >= 10:
        return chr(97 + (x - 10))
    return str(x)

# returns an 128x128 array of color indicies 
# (the same color indicies as in pico8 but in hexadecimal)
def make_label(name):
    img = cv2.imread(name)
    w = 128
    img = cv2.resize(img, (w, w))

    label = [[0 for i in range(128)] for i in range(128)]

    for x in range(w):
        for y in range(w):
            r, g, b = img[x, y]
            pixel = (b, g, r)
            color_index = closest_color(pico_colors, pixel)
            label[x][y] = to_hex(color_index)

    return label

# adds a label to the given cart
def add_label(cart_path, label_path):
    if not cart_path.endswith('.p8'):
        cart_path += '.p8'
    
    label = make_label(label_path)
    fp = open(cart_path, 'r')
    result = ""
    a = 0
    has_label = False

    # replace current label in cart with new one
    for i, line in enumerate(fp):
        if a > 0:
            row = label[len(label) - a]
            result += ''.join(row) + '\n'
        else:
            result += line

        a -= 1

        if '__label__' in line:
            a = 128
            has_label = True

    if not has_label:
        result += '__label__\n'
        for i in range(128):
            row = label[i]
            result += ''.join(row) + '\n'

    f =  open(cart_path, 'w', newline='\n')
    f.write(result)
    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cart", help = "path to the cart you want to modify")
    parser.add_argument("-l", "--label", help = "path to the image label")
    args = parser.parse_args()

    cart = args.cart
    label = args.label

    if not cart:
        cart = input('Please input the relative path to the cartrige: ')
    if not label:
        label = input('Please input the relative path to the label: ')

    add_label(cart, label)
