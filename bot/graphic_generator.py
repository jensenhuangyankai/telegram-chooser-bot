import tkinter as tk
import random
import math
from PIL import Image
import os
import glob
import subprocess
import requests
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('WEBHOOK_HOST')

from pyvirtualdisplay import Display
os.environ['PYVIRTUALDISPLAY_DISPLAYFD'] = '0'


def save_as_png(canvas, fileName):
    canvas.postscript(file='./eps/' + fileName + '.eps', colormode='color', pagewidth=400)
    img = Image.open('./eps/' + fileName + '.eps')
    img.convert()
    img.save('./png/' + fileName + '.png', 'png')


class WheelSpinGame:
    """
    Class to create a Wheel Spin game using tkinter.

    Attributes:
    - root: tk.Tk
        The root window of the game.
    - canvas: tk.Canvas
        The canvas widget to display the wheel.
    - wheel_values: list
        List of values to display on the wheel.
    - wheel_size: int
        The size of the wheel.
    - wheel_radius: int
        The radius of the wheel.
    - wheel_center: tuple
        The center coordinates of the wheel.
    #- spin_button: tk.Button
    #    The button to spin the wheel.
    """

    def __init__(self, wheel_values: list, tele_chat_id: str):
        """
        Constructor to instantiate the WheelSpinGame class.

        Parameters:
        - wheel_values: list
            List of values to display on the wheel.
        """

        # Creating the root window
        self.root = tk.Tk()
        self.root.title("Indecisive")

        # Setting up the canvas
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        

        # Setting up the wheel attributes
        self.wheel_values = wheel_values
        self.wheel_size = len(wheel_values)
        self.wheel_radius = 150
        self.wheel_center = (200, 200)

        self.colors = []
        self.imageCounter = 0
        self.width = 400
        self.height = 400

        self.tele_chat_id = tele_chat_id
        self.result = ""
        

    def draw_wheel(self):
        """
        Draws the wheel on the canvas with the given values.
        """

        # Clearing the canvas
        self.canvas.delete("all")

        self.canvas.create_polygon([355, 200, 380, 190, 380, 210], fill='yellow')

        # Drawing the wheel
        extent = 360 / self.wheel_size
        start_angle = 0


        for value in self.wheel_values:
            colors = ['#fc0c8e', '#fd8a1a', '#fde334', '#acfb13', '#21d1fd', '#ee0f58', 
                      '#fb7a08', '#fdf12f', '#36e8f3', '#8b1df2',
                      '#e71919', '#fb8637', '#fdef0a', '#57e9f6', '#1683e8']
            #color = "#" + "%06x" % random.randint(0, 0xFFFFFF)
            color = random.choice(colors)
            self.colors.append(color)
            end_angle = start_angle + extent
            self.canvas.create_arc(
                self.wheel_center[0] - self.wheel_radius,
                self.wheel_center[1] - self.wheel_radius,
                self.wheel_center[0] + self.wheel_radius,
                self.wheel_center[1] + self.wheel_radius,
                start=start_angle,
                extent=extent,
                fill=color,
                outline="black"
            )


            self.canvas.create_text(
                self.wheel_center[0] + self.wheel_radius * 0.8 * math.sin(math.radians(start_angle + 108)),
                self.wheel_center[1] + self.wheel_radius * 0.8 * math.cos(math.radians(start_angle + 108)),
                text=str(value),
                font=("Arial", 12, "bold")
            )
            start_angle = end_angle
        save_as_png(self.canvas, str(f'{self.imageCounter:04}') + '_' + self.tele_chat_id)
        self.imageCounter += 1

    def spin_wheel(self):
        """
        Spins the wheel and displays the result.
        """ 

        # Randomly selecting a value from the wheel
        result = random.choice(self.wheel_values)
        self.result = str(result)
        print("RESULT:" + str(result))
        
        # Rotating the wheel to the selected value
        angle = 360 / self.wheel_size
        rotation_angle = angle * self.wheel_values.index(result) + 360 * random.randint(3,5) 

        self.canvas.after(10, self.rotate_wheel, 360 - (random.randint(-int(angle/4), int(angle//4))), rotation_angle, 1)


    def rotate_wheel(self,angle=360, rotation_angle=0,time=0):
        self.canvas.delete('all')

        extent = 360 / self.wheel_size
        start_angle = angle
        self.canvas.create_polygon([355, 200, 380, 190, 380, 210], fill='yellow')
        for value in self.wheel_values:
            end_angle = start_angle + extent
            self.canvas.create_arc(
                self.wheel_center[0] - self.wheel_radius,
                self.wheel_center[1] - self.wheel_radius,
                self.wheel_center[0] + self.wheel_radius,
                self.wheel_center[1] + self.wheel_radius,
                start=start_angle,
                extent=extent,
                fill=self.colors[self.wheel_values.index(value)],
                outline="black"
            )

            self.canvas.create_text(
                self.wheel_center[0] + self.wheel_radius * 0.8 * math.sin(math.radians(start_angle + 108)),
                self.wheel_center[1] + self.wheel_radius * 0.8 * math.cos(math.radians(start_angle + 108)),
                text=str(value),
                font=("Arial", 12, "bold")
            )
            start_angle = end_angle

        
        save_as_png(self.canvas, str(f'{self.imageCounter:04}') + '_' + self.tele_chat_id)
        self.imageCounter += 1
        
        print(rotation_angle)
        if rotation_angle > 500:
            self.canvas.after(time, self.rotate_wheel, (angle - 80), rotation_angle - 80, time + 5)
        elif 0 <= rotation_angle <= 500:
            max_rot_angle = int(extent / (random.randint(4,8)))
            self.canvas.after(time, self.rotate_wheel, (angle - max_rot_angle), rotation_angle - max_rot_angle, time + 100)

        #elif -extent < rotation_angle < 0:
        #    max_rot_angle = int(extent / (random.randint(4,8)))
        #
        #    self.canvas.after(time, self.rotate_wheel, angle - max_rot_angle, -max_rot_angle, time + 180)
        else:
            for _ in range(20):
                save_as_png(self.canvas, str(f'{self.imageCounter:04}') + '_' + self.tele_chat_id)
                self.imageCounter += 1
            process = subprocess.call('convert -delay 0 -loop 0 ./png/*{tele_chat_id}.png -size 400x400 output_{tele_chat_id}.gif'.format(tele_chat_id = self.tele_chat_id), shell=True)
            self.root.destroy()
            if process == 0:
                packet = {
                    'chat_id' : self.tele_chat_id,
                    'winner' : self.result
                }
                x= requests.get(f"https://{HOST}/winner_helper", json = packet)
                
                files = glob.glob("./png/*{tele_chat_id}.png".format(tele_chat_id = self.tele_chat_id))
                files2 = glob.glob("./eps/*{tele_chat_id}.eps".format(tele_chat_id = self.tele_chat_id))
                for f in files:
                    os.remove(f)
                for f in files2:
                    os.remove(f)


    def start(self):
        """
        Starts the game by running the tkinter main loop.
        """
        
        self.draw_wheel()
        self.spin_wheel()
        self.root.mainloop()



def generate_wheel(wheel_values, tele_chat_id):
    with Display(backend="xvfb", visible=0, size=(500,500)) as disp:
        print("display status:" + str(disp.is_alive()))
        game = WheelSpinGame(wheel_values, str(tele_chat_id))
        game.start()
        print(game.result)
        disp.stop()
    return game.result
