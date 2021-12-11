#!/usr/bin/python3

class Display:
	def __init__(self):
		self.puzzle = {}

	def _parse_input(self):
		with open('data/day8.txt', 'r') as infile:
			content = infile.readlines()

		self.puzzle['first'] = []
		self.puzzle['second'] = []
		for line in content:
			parts = line.split(' | ')
			self.puzzle['first'].append(parts[0].rstrip())
			self.puzzle['second'].append(parts[1].rstrip())
			
	def unique(self):
		self._parse_input()
		items = []
		for i in self.puzzle['second']:
			for j in i.split():
				items.append(j)

		count = 0
		for i in items:
			if (len(i) == 2) or (len(i) == 4) or (len(i) == 3) or (len(i) == 7):
				count += 1

		print(count)
		

if __name__ == '__main__':
	Sub = Display()
	Sub.unique()