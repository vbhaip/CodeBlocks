from conditionstruc import ConditionStructure
from conditionblock import ConditionBlock
from color_num_to_block import dic as color_num_to_block

SEARCH_CONE_SLOPE = .15
INDENT_DIST = 10

#inp = [(50, 50, 'pink', 4), (100, 50, 'yellow', 4), (80, 100, 'pink', 4), (130, 100, 'yellow', 4), (110, 150, 'green', 4), (110, 200, 'green', 5), (80, 250, 'green', 6), (50, 300, 'green', 4)]
#inp = [(50, 50, 'pink', 4), (100, 50, 'yellow', 4), (80, 100, 'green', 4)]
inp = [(50, 50, 'green', 4)]

def add_block_group(rem, last_added, last_elif, last_elif_xy):
	cur_block = []

	while len(rem):
		# getting next block
		print(cur_block, rem)
		next_block_ind, highest_y = -1, 999999999
		for i, (x, y, c, np) in enumerate(rem):
			dx = x - last_elif_xy[0]
			y_score = SEARCH_CONE_SLOPE * dx + y
			if y_score < highest_y:
				next_block_ind, highest_y = i, y_score
		print('next block', rem[next_block_ind], 'last elif', last_elif)
		if next_block_ind == -1 or rem[next_block_ind][0] - last_elif_xy[0] < INDENT_DIST:
			print('ending indent')
			# if no next block or indent ends
			return cur_block

		next_block = rem.pop(next_block_ind)
		if next_block[2] == 'yellow':
			print('Condition is by itself')

		# elif blocks
		if next_block[2] == 'pink':
			# if its an if, find the condition
			if next_block[3] == 4:
				print('if')
				n_last_elif, n_last_elif_xy = next_block, (next_block[0], next_block[1])
				closest_in_cone_ind, closest_in_cone_x = -1, 999999999
				for i, (x, y, c, np) in enumerate(inp):
					dx = x - n_last_elif_xy[0]
					# if its in the cone
					if -SEARCH_CONE_SLOPE * dx + n_last_elif_xy[1] < y < SEARCH_CONE_SLOPE * dx + n_last_elif_xy[1]:
						if x < closest_in_cone_x and c == 'yellow':
							closest_in_cone_ind, closest_in_cone_x = i, x
				if closest_in_cone_ind == -1:
					print('Could not find a condition for an if!')
				last_added = rem.pop(closest_in_cone_ind)
				block = [n_last_elif, last_added]
				block += add_block_group(rem, last_added, n_last_elif, n_last_elif_xy)
				cur_block.append(block)
			# if its an else
			else:
				n_last_elif, n_last_elif_xy, last_added = next_block, (next_block[0], next_block[1]), next_block
				block = [n_last_elif]
				block += add_block_group(rem, last_added, n_last_elif, n_last_elif_xy)
				cur_block.append(block)


		elif next_block[2] == 'green':
			last_added = next_block
			cur_block.append(next_block)
	return cur_block

blocks = add_block_group(inp, None, None, (-INDENT_DIST, 0))
print('out', blocks)
print('\n\n\n')

def block_to_struct(blocks):
	ind = 0
	all_if_blocks, all_else_blocks = [], []
	while ind < len(blocks):
		b_group = blocks[ind]
		if type(b_group) == type((0,0)):
			print('x')
			all_if_blocks.append(color_num_to_block[(b_group[2], b_group[3])])
			ind += 1
		else:
			block = b_group[0]
			# if
			if block[2] == 'pink' and block[3] == 4:
				print('if')
				cond = b_group[1]
				if_block = [block_to_struct(b_group[ind+2:])]
				else_block = None
				ind += 1
				if ind < len(blocks):
					print('else')
					b_group = blocks[ind]
					if type(b_group) == type((0,0)):
						print('nvm, y')
						print('c',cond)
						all_if_blocks.append(ConditionStructure(color_num_to_block[(cond[2], cond[3])], [color_num_to_block[(b_group[2], b_group[3])]], None))
						ind += 1
					else:
						block = b_group[0]
						# else
						if block[2] == 'pink' and block[3] == 5:
							else_block = [block_to_struct(blocks[ind+1:])]
							ind += 1
				print(type(if_block))
				print('c',cond)
				all_if_blocks.append(ConditionStructure(color_num_to_block[(cond[2], cond[3])], if_block, else_block))
			elif block[2] == 'green':
				print('z')
				all_if_blocks.append(color_num_to_block[(block[2], block[3])])
				ind += 1
	all_if_blocks.reverse()
	all_else_blocks.reverse()
	print(all_if_blocks, all_else_blocks)
	return ConditionStructure(True, all_if_blocks, all_else_blocks)

def blocks_to_struct(blocks):
	ind = 0
	all_if_blocks, all_else_blocks = [], []
	print('inp', blocks)
	while ind < len(blocks):
		print(blocks[ind])
		# green
		if type(blocks[ind]) == type((0,0)):
			print('green')
			block = blocks[ind]
			all_if_blocks.append(color_num_to_block[(block[2], block[3])])
			ind += 1
		# pink
		else:
			block_group = blocks[ind]
			# if
			print('pink',block_group)
			if block_group[0][2] == 'pink' and block_group[0][3] == 4:
				cond = block_group[1]
				print('2:',block_group[2:])
				if_block = blocks_to_struct(block_group[2:])
				else_block = None
				ind += 1
				if ind < len(blocks):
					# else
					# green
					if type(blocks[ind]) == type((0,0)):
						print('green')
						block = blocks[ind]
						all_if_blocks.append(color_num_to_block[(block[2], block[3])])
						ind += 1
					else:
						block_group = blocks[ind]
						print('bg', block_group)
						if block_group[0][2] == 'pink' and block_group[0][3] == 5:
							else_block = blocks_to_struct(block_group[1:])
				all_if_blocks.append(if_block)
				all_else_blocks.append(else_block)
	print(all_if_blocks, all_else_blocks)
	return ConditionStructure(True, all_if_blocks, all_else_blocks)

overall_struct = block_to_struct(blocks)
print()
print(overall_struct)