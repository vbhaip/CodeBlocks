from conditionstruc import ConditionStructure, ConditionStructureLoop
from conditionblock import ConditionBlock
from color_num_to_block import dic as color_num_to_block
import conditions

SEARCH_CONE_SLOPE = .3
INDENT_DIST = 30

#inp = [(50, 50, 'PINK', 4), (100, 50, 'YELLOW', 4), (80, 100, 'PINK', 4), (130, 100, 'YELLOW', 4), (110, 150, 'GREEN', 4), (110, 200, 'GREEN', 5), (80, 250, 'GREEN', 6), (50, 300, 'GREEN', 4)]
#inp = [(50, 20, 'GREEN', 5), (50, 50, 'PINK', 4), (100, 50, 'YELLOW', 4), (80, 100, 'GREEN', 4), (80, 150, 'GREEN', 5), (50, 200, 'PINK', 5), (80, 250, 'GREEN', 6), (50, 300, 'GREEN', 4)]
#inp = [(50, 50, 'PINK', 4), (100, 50, 'YELLOW', 4), (80, 100, 'PINK', 4), (130, 100, 'YELLOW', 4), (110, 150, 'GREEN', 4), (80, 200, 'GREEN', 4)]
inp = [(50, 50, 'PINK', 5), (80, 50, 'YELLOW', 4), (80, 100, 'GREEN', 4)]

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
		# print('next block', rem[next_block_ind], 'last elif', last_elif)
		if next_block_ind == -1 or rem[next_block_ind][0] - last_elif_xy[0] < INDENT_DIST:
			# print('ending indent')
			# if no next block or indent ends
			return cur_block

		next_block = rem.pop(next_block_ind)
		if next_block[2] == 'YELLOW':
			raise Exception('Error in code! Condition has no if statement?')


		# elif blocks
		if next_block[2] == 'PINK':
			# if its an if or a for, find the condition
			if next_block[3] == 4 or next_block[3] == 6:
				# print('if')
				n_last_elif, n_last_elif_xy = next_block, (next_block[0], next_block[1])
				closest_in_cone_ind, closest_in_cone_x = -1, 999999999
				for i, (x, y, c, np) in enumerate(rem):
					dx = x - n_last_elif_xy[0]
					# if its in the cone
					if -SEARCH_CONE_SLOPE * dx + n_last_elif_xy[1] < y < SEARCH_CONE_SLOPE * dx + n_last_elif_xy[1]:
						if x < closest_in_cone_x and c == 'YELLOW':
							closest_in_cone_ind, closest_in_cone_x = i, x
				if closest_in_cone_ind == -1:
					print('Could not find a condition for an if!')
				last_added = rem.pop(closest_in_cone_ind)
				block = [n_last_elif, last_added]
				block += [add_block_group(rem, last_added, n_last_elif, n_last_elif_xy)]
				cur_block.append(block)
			# if its an else
			elif next_block[3] == 5:
				n_last_elif, n_last_elif_xy, last_added = next_block, (next_block[0], next_block[1]), next_block
				block = [n_last_elif]
				block += [add_block_group(rem, last_added, n_last_elif, n_last_elif_xy)]
				cur_block.append(block)



		elif next_block[2] == 'GREEN':
			last_added = next_block
			cur_block.append(next_block)
	return cur_block


def blocks_to_struct(blocks):
	ind = 0
	all_if_blocks = []
	# print('inp', blocks)
	while ind < len(blocks):
		print('processing', blocks[ind])
		# GREEN
		if type(blocks[ind]) == type((0,0)):
			block = blocks[ind]
			all_if_blocks.append(color_num_to_block[(block[2], block[3])])
			ind += 1
		# PINK
		else:
			block_group = blocks[ind]
			# if
			if block_group[0][2] == 'PINK' and block_group[0][3] == 4:
				cond = color_num_to_block[(block_group[1][2], block_group[1][3])]
				ind += 1
				rest = block_group[2]
				i_blocks = blocks_to_struct(rest)
				e_blocks = []
				# else
				if ind < len(blocks):
					if type(blocks[ind]) != type((0,0)):
						block_group = blocks[ind]
						if block_group[0][2] == 'PINK' and block_group[0][3] == 5:
							ind += 1
							rest = block_group[1]
							e_blocks = blocks_to_struct(rest)
				all_if_blocks.append(ConditionStructure(cond, i_blocks, e_blocks))
			# for
			if block_group[0][2] == 'PINK' and block_group[0][3] == 6:
				loops = block_group[1][3]
				ind += 1
				rest = block_group[2]
				l_blocks = blocks_to_struct(rest)
				all_if_blocks.append(ConditionStructureLoop(loops, l_blocks))

	return all_if_blocks


# try:
# 	blocks = add_block_group(inp, None, None, (-INDENT_DIST, 0))
# 	print('out', blocks)
# 	print('\n\n\n')
# 	i_blocks = blocks_to_struct(blocks)
# 	overall_struct = ConditionStructure(True, i_blocks, [])
# 	print()
# 	print(overall_struct)
# except:
# 	print('Error in parsing input! Please check your blocks')
# 	#return ConditionStructure(conditions.ret_true, [], [])

def format_objects(inp):
	try:
		blocks = add_block_group(inp, None, None, (-INDENT_DIST, 0))
		i_blocks = blocks_to_struct(blocks)
		overall_struct = ConditionStructure(conditions.ret_true, i_blocks, [])
		return overall_struct
	except:
		print('Error in parsing!')
		return ConditionStructure(conditions.ret_true, [], [])
