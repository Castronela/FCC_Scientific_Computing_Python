#!/bin/python3.11

import copy
import random

class Hat:
		
	def __init__(self, **kwargs):
		contents_2d = [[color] * amount for color, amount in kwargs.items()]
		self.contents = sum(contents_2d, [])
		
	def draw(self, amount_draw):
		if amount_draw > len(self.contents):
			amount_draw = len(self.contents)
		balls_drawn = []
		for _ in range(amount_draw):
			index_drawn = random.randint(0, len(self.contents) - 1)
			color_drawn = self.contents.pop(index_drawn)
			balls_drawn.append(color_drawn)
		return balls_drawn

hat = Hat(black=6, red=4, green=3)
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	successful_draws = 0
	for _ in range(num_experiments):
		hat_copy = copy.deepcopy(hat)
		drawn = hat_copy.draw(num_balls_drawn)
		if all(amount <= len(list(filter(lambda col: col == color, drawn))) for color, amount in expected_balls.items()):
			successful_draws += 1
	return successful_draws / num_experiments

if __name__ == '__main__':
	probability = experiment(hat, {'red':2,'green':1}, 5, 2000)
	print(probability)