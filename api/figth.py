import random
import io,base64
import matplotlib.pyplot  as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from hero import Hero
import numpy as np

class Figth():
    "fight fight fight"

    def __init__(self, figther_one, figther_two):
        self.__fighter_one = figther_one
        self.__fighter_two = figther_two

    def get_fighter_one(self):
        return self.__fighter_one

    def get_fighter_two(self):
        return self.__fighter_two

    def who_hit(self):
        f_1_characters = self.get_fighter_one().get_characteristics()
        f_2_characters = self.get_fighter_two().get_characteristics()

        if ((f_1_characters['speed']+random.randrange(0,100)) >= f_2_characters['speed']+random.randrange(0,100)):
            return self.get_fighter_one(), self.get_fighter_two()
        else:
            return self.get_fighter_two(), self.get_fighter_one()

    def figth(self): #las peleas son a muerte o por rounds (?)
        hit_list=[]
        hero_hit, hero_defender = self.who_hit()
        hit_list.append(f'Golpeó {hero_hit.get_name()}')
        while hero_defender.is_alive():
            if hero_hit.get_characteristics()['total']*random.randrange(1,9) > hero_defender.get_characteristics()['total']*random.randrange(1,9):
                damage = hero_hit.give_hit()
                hero_defender.take_hit(damage)   
            hero_hit, hero_defender = self.who_hit()    
            hit_list.append(f'Golpeó {hero_hit.get_name()}')
        return hit_list
       
    def show(self):
        hero_one=self.get_fighter_one().get_characteristics()
        hero_two=self.get_fighter_two().get_characteristics()
        
        
        fighter_one = [hero_one['strength'],hero_one['speed'],hero_one['intelligence'],hero_one['hardness'],hero_one['power'],hero_one['combat']]
        fighter_two = [hero_two['strength'],hero_two['speed'],hero_two['intelligence'],hero_two['hardness'],hero_two['power'],hero_two['combat']]

        labels = ['Strength', 'Speed', 'Intelligence', 'Hardness', 'Power', 'Combat']
        
        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, fighter_one, width, label=self.get_fighter_one().get_name())
        rects2 = ax.bar(x + width/2, fighter_two, width, label=self.get_fighter_two().get_name())

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Values')
        ax.set_title('Comparison of Qualities')
        ax.set_xticks(x, labels)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        fig.tight_layout()
        image_html = io.BytesIO()
        FigureCanvas(fig).print_png(image_html)
        return base64.b64encode(image_html.getvalue()).decode('utf8')

        
