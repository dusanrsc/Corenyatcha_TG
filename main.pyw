# Importing modules.
import tkinter
import sys
import os

# Importing sub-modules.
from tkinter import *
from PIL import Image, ImageTk

# Main program function.
def main():

	# Settings section.
	# Constants sestion.
	ROOT_WIDTH = 800
	ROOT_HEIGHT = 600
	ROOT_SIZE = f"{ROOT_WIDTH}x{ROOT_HEIGHT}"

	ROOT_TITLE = "Corenyatcha Template Generator"

	# Hexadecimal color constants.
	RED = "#FF0000"
	GREEN = "#00FF00"
	BLUE = "#0000FF"

	BLACK = "#000000"
	WHITE = "#FFFFFF"

	ALPHA = GREEN

	DEFAULT_BACKGDOUND_COLOR = BLACK
	DEFAULT_FOREGROUND_COLOR = BLUE

	# Variable section.
	current_directory = os.getcwd()
	path = current_directory
	
	assets_dir = "assets"
	logo_image = "corenyatcha-logo.png"

	# Thunder variable (metadata).
	__version__ = "v1.0.0"
	__updated__ = "12.12.2024"
	__tag__ = "@dusanrsc"
	__by__ = "Dusan Rosic"

	# JavaScript formating operators
	js_addition_assignment = "+="
	js_assignment = "="
	js_curly_bracket_opened = "{"
	js_curly_bracket_closed = "}"

	# HTML & CSS operators
	html_space = "&nbsp;"
	html_break = "<br/>"

	# Template content variable
	html_template_title = f"Generated via Corenyatcha Template Generator {__version__}!"
	html_template_heading = f"Generated via Corenyatcha{html_break}Template Generator {__version__}!"
	html_template_name = "index.html"
	html_template_body = f"""<!DOCTYPE html>
<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <title>{html_template_title}</title>
        <link rel="icon" href="{assets_dir}/{logo_image}" type="image/x-icon">

	    <!-- Bootstrap loading link -->
	    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">

	    <!-- Style section -->
        <style>

        	/* Style for body */
            body {js_curly_bracket_opened}
                display: flex;
                justify-content: center;
                align-items: center;
                height: 95vh;
                margin: 0;
                background-color: #000000;
            {js_curly_bracket_closed}

            /* Style for rotating image */
            .rotating-image {js_curly_bracket_opened}
                width: 150px;
                height: 150px;
                transition: transform 0.1s linear;
                transform-origin: center;
            {js_curly_bracket_closed}

            /* Style for div-container */
            .div-container {js_curly_bracket_opened}
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            {js_curly_bracket_closed}

        </style>
    </head>
    <body>


        <!-- Div section -->
        <div class="div-container">

            <!-- Rotating image -->
            <img id="image" src="{assets_dir}/{logo_image}" alt="Rotating Image" class="rotating-image">

            {html_space}{html_space}{html_space}{html_space}{html_space}{html_space}{html_space}{html_space}
            
            <h1 class="text text-success">
                {html_template_heading}
            </h1>
        </div>
        <!-- End div section -->

        <!-- JavaScript section -->
        <script>
        
        	// Select image
            const image = document.getElementById("image");
            let angle = 0;

        	// Rotate image function
            function rotateImage() {js_curly_bracket_opened}
            angle {js_addition_assignment} 0.75; 									// Increase angle by step
            image.style.transform {js_assignment} `rotate(${js_curly_bracket_opened}angle{js_curly_bracket_closed}deg)`;  // Rotate image
            requestAnimationFrame(rotateImage);         	// Call rotateImage function

        	if (angle > 20) {js_curly_bracket_opened}
        		angle = -20
        	{js_curly_bracket_closed}
        {js_curly_bracket_closed}

        // Start rotation
        rotateImage();
        </script>
        <!-- End JavaScript section -->

    </body>
</html>"""


	# Program logic section.
	def create_directory():
		#os.system(f"mkdir {current_directory}{dir_name}")
		print(path)

	# {Comment}
	def create_virtualenv():
		pass

	def generate_html_css_bootstrap_javascript_template():
		#if not os.path.exists():
    		#os.makedirs("html")

		with open(f"{html_template_name}", "w") as file:
			file.write(html_template_body)

	# {Comment}
	def generate_django_template(project_name="Django_Project", env_path=os.getcwd()):

 		# Installing Python.
   		# winget install --id Docker.DockerDesktop

		# Upgrading pip.
		os.system("python.exe -m pip install --upgrade pip")

		# Checking if Django is installed.
		#version = os.system("python -m django --version")

		# Installing django.
		os.system("python -m pip install --user django")

		# Installing env.
		os.system("python -m pip install --user env")

		# 
		print(env_path)

		# Generating django project.
		#os.system(f"django-admin startproject {project_name}")

	# {Comment}
	def generate_tkinter_template(project_name="Tkinter_Main"):
		with open(f"{project_name}.pyw", "w") as file:
			file.write("""# Importing modules.
import tkinter

# Importing sub-modules.
from tkinter import *

root = Tk()
root.config(bg="#FFFFFF")
root.geometry("800x600")

root.mainloop()
""")

	# {Comment}
	def generate_pygame_template(project_name="Pygame_Main"):
		with open(f"{project_name}.pyw", "w") as file:
			file.write("""# Importing modules.
import pygame
import random
import sys
import os

# Importing sub-modules.
from random import randint

# Initializing modules.
pygame.init()

# Settings section.
# Variables section.
running = True
mouse_visibility = True
clock = pygame.time.Clock()

# Specials variables
__version__ = "v1.0.0"

# Constants section.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

SCREEN_TITLE = "Pygame_Main"
FPS = 60
PLAYER_SPEED = 10

# Colors tuple section.
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

ALPHA = GREEN

# Setting up screen.
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
TITLE = pygame.display.set_caption(f"{SCREEN_TITLE} | {__version__}")
MOUSE_VISIBILITY = pygame.mouse.set_visible(mouse_visibility)

# Functions section.
# Exit game function.
def exit():
    pygame.quit()
    sys.exit()
    running = False

# Class section.
# Hero class.
class Corenyatcha(pygame.sprite.Sprite):
    def __init__(self, pos_x=400, pos_y=300, scale_by=2):
        super().__init__()
        self.image = pygame.image.load("assets/corenyatcha-logo.png")
        self.image = pygame.transform.scale(self.image, (self.image.size[0] // scale_by, self.image.size[1] // scale_by))
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect(center = [pos_x, pos_y])

    # Update hero method.
    def update(self):
        pass    #self.rect.y -= (PLAYER_SPEED * 

# Creating Hero group.
corenyatcha_group = pygame.sprite.Group()
corenyatcha = Corenyatcha()
corenyatcha_group.add(corenyatcha)

# Main game loop.
while running:

    # Delta time.
    dt = (clock.tick(FPS) / 1000)

    # If key pressed statements.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Keyboard imput.
    keys = pygame.key.get_pressed()

    # Basic movement logic.
    # Move foreward.
    #if keys[pygame.K_w]:
        #corenyatcha.rect.y -= (PLAYER_SPEED * dt)

    # Filling screen with black.
    SCREEN.fill(BLACK)

    # Drawing sprites on the screen.
    corenyatcha_group.update()
    corenyatcha_group.draw(SCREEN)

    # FPS counter.
    pygame.display.flip()
    clock.tick(FPS)
""")

	# Creating Main (root) program window.
	root = Tk()
	root.geometry(ROOT_SIZE)
	root.title(f"{ROOT_TITLE} | {__version__} | by: {__tag__}")
	root.config(bg=DEFAULT_BACKGDOUND_COLOR)
	root.resizable(False, False)

	# Pre-processing images.
	background_logo = Image.open("assets/corenyatcha-logo.png")
	background = ImageTk.PhotoImage(background_logo)

	django_logo = Image.open("assets/django.png")
	django = ImageTk.PhotoImage(django_logo)

	django_rest_logo = Image.open("assets/django_rest_framework.png")
	django_rest = ImageTk.PhotoImage(django_rest_logo)

	html_logo = Image.open("assets/html.png")
	html = ImageTk.PhotoImage(html_logo)

	htmlcss_logo = Image.open("assets/htmlandcss.png")
	htmlcss = ImageTk.PhotoImage(htmlcss_logo)

	htmlcss_logo = Image.open("assets/htmlandcss.png")
	htmlcss = ImageTk.PhotoImage(htmlcss_logo)

	pygame_logo = Image.open("assets/pygame.png")
	pygame = ImageTk.PhotoImage(pygame_logo)

	tkinter_logo = Image.open("assets/tkinter.png")
	tkinter = ImageTk.PhotoImage(tkinter_logo)

	custom_logo = Image.open("assets/custom.png")
	custom = ImageTk.PhotoImage(custom_logo)

	technology_frame = Frame(root, bg=DEFAULT_BACKGDOUND_COLOR)
	technology_frame.pack(pady=60)

	# Buttons section.
	django_button = Button(technology_frame, image=django, relief="flat", bg=DEFAULT_BACKGDOUND_COLOR, command=lambda: generate_django_template())
	django_button.grid(row=0, column=1)

	django_rest_button = Button(technology_frame, image=django_rest, relief="flat", bg=DEFAULT_BACKGDOUND_COLOR)
	django_rest_button.grid(row=0, column=2)

	html_button = Button(technology_frame, image=html, relief="flat", bg=DEFAULT_BACKGDOUND_COLOR)
	html_button.grid(row=0, column=3)

	html_css_bootstrap_javascript_button = Button(technology_frame, image=htmlcss, relief="flat", bg=DEFAULT_BACKGDOUND_COLOR, command=lambda: generate_html_css_bootstrap_javascript_template())
	html_css_bootstrap_javascript_button.grid(row=0, column=4)

	pygame_button = Button(technology_frame, image=pygame, relief="flat", bg=DEFAULT_BACKGDOUND_COLOR, command=lambda: generate_pygame_template())
	pygame_button.grid(row=1, column=1)

	tkinter_button = Button(technology_frame, image=tkinter, relief="flat", bg=DEFAULT_BACKGDOUND_COLOR, command=lambda: generate_tkinter_template())
	tkinter_button.grid(row=1, column=2)

	# Custom template buttons.
	custom_button1 = Button(technology_frame, image=custom, relief="flat", bg=DEFAULT_BACKGDOUND_COLOR, command=None)
	custom_button1.grid(row=2, column=1)

	custom_button2 = Button(technology_frame, image=custom, relief="flat", bg=DEFAULT_BACKGDOUND_COLOR, command=None)
	custom_button2.grid(row=2, column=2)

	custom_button3 = Button(technology_frame, image=custom, relief="flat", bg=DEFAULT_BACKGDOUND_COLOR, command=None)
	custom_button3.grid(row=2, column=3)

	custom_button4 = Button(technology_frame, image=custom, relief="flat", bg=DEFAULT_BACKGDOUND_COLOR, command=None)
	custom_button4.grid(row=2, column=4)

	# Main program loop.
	root.mainloop()

# Running the program main function.
if __name__ == "__main__":
	main()
