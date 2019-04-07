import conditionstruc, conditionblock

SEARCH_CONE_SLOPE = .15
INDENT_DIST = 10

inp = [(50, 50, 'pink', 4), (100, 50, 'yellow', 4), (80, 100, 'pink', 4), (130, 100, 'yellow', 4), (110, 150, 'green', 4), (110, 200, 'green', 4), (80, 250, 'green', 4), (50, 300, 'green', 4)]

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

print('ret', add_block_group(inp, None, None, (-INDENT_DIST, 0)))

