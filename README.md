# pico-label
A tool for Pico-8 that transforms any .png file to a cartrige label.

# What is Pico 8?
PICO-8 is a fantasy console for making, sharing and playing tiny games and other computer programs. It feels like a regular console, but runs on Windows / Mac / Linux. When you turn it on, the machine greets you with a commandline, a suite of cartridge creation tools, and an online cartridge browser called SPLORE.

# How to use
There are two ways to use this program:
1. Execute the script with the `--cart/-c` and `--label/-l` arguments or leave them blank to enter them inside the program.
2. call pico_label.add_label(cart_path, label_path) inside of your own script.

# Why use it
Pico 8's label system is very limited. In order to create your own label you often need to alter your code and sprites just to draw a full-screen logo. This approach enables you to use your editing software of choice to make a label, or even squash an existing image into the correct size and colors.

# How it works
Pico 8 cartriges contain a `__label__` tag, which contains a 128 by 128 grid of characters, representing a label image. Each character is a hexadecimal value for a color in Pico 8's color palette, in the range of 0-15. When pressing F2 inside Pico 8, the program will take whatever is on the screen and assign to the label, but we can edit the label however we want to.
The script executes the following steps:
- Resize the label image to 128x128.
- For each pixel, find the most similar color out of the Pico8 palette.
- Take the color's index and convert it to hex.
- Write it all to the cartrige.
