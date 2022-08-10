nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]


class FlatIterator:

	def __init__(self, all_list: list):
		self.all_list = all_list
		self.len_new_list = len(all_list)
		self.len_in_list = len(nested_list[0])

	def __iter__(self):
		self.cursor = 0
		self.cursor_in_list = 0
		return self


	def __next__(self):
		while self.cursor < self.len_new_list:
			if self.cursor_in_list < len(self.all_list[self.cursor]):
				f = self.all_list[self.cursor][self.cursor_in_list]
				self.cursor_in_list += 1
				return f
			self.cursor_in_list = 0
			self.cursor += 1
		else:
			raise StopIteration

def flat_generation(list):
	cursor = 0
	cursor_in_list = 0
	while cursor < len(list):
		while cursor_in_list < len(list[cursor]):
			f = list[cursor][cursor_in_list]
			cursor_in_list += 1
			yield f
		cursor_in_list = 0
		cursor += 1

for item in flat_generation(nested_list):
	print(item)
for item in FlatIterator(nested_list):
	print(item)
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

