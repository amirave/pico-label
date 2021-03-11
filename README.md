# pico-label
A tool for Pico-8 that transforms a .png file to a cartrige label.

# What is Pico 8?
>PICO-8 is a fantasy console for making, sharing and playing tiny games and other computer programs. It feels like a regular console, but runs on Windows / Mac / Linux. When you turn it on, the machine greets you with a commandline, a suite of cartridge creation tools, and an online cartridge browser called SPLORE.

# How to use
There are two ways to use this program:
1. Execute the script with the `--cart(-c)` and `--label(-l)` arguments or leave them blank to enter them inside the program.
2. call pico_label.add_label(cart_path, label_path) with the correct arguments.

# Why use it
Pico 8's label system is very limited. If you want to create a good label, you often need to alter and code and the sprites just to draw a big image on the screen, but you have much more control when editing a label in Aseprite or Photoshop.
This tool allows you to create a label image however you want, and even works relatively well with .png files that have bigger dimensions or more colors.

# How it works
Pico 8 cartriges contain a `__label__` tag, which contains a 128 by 128 grid of characters, representing a label image. Each character is a hexadecimal value for a color in Pico 8's color palette, in the range of 0-15. When pressing F2 inside Pico 8, the program will take whatever is on the screen and assign to the label, but we can edit the label however we want to.
My script executes the following steps:
- Resize the label image to 128x128.
- For each pixel, find the nearest Pico 8 color.
- Take the color's index and convert it to hex.
- Write the index to the cartrige.
