from conditionblock import ConditionBlock

class ConditionStructure:
	def __init__(self, cond, if_block, else_block):
		self.cond = cond
		self.if_block = if_block
		self.else_block = else_block

	def isTrue(self):
		return self.cond()

	def evaluate(self):
		if (self.isTrue()):
			for block in self.if_block:
				block.evaluate()
		elif self.else_block:
			# else block if it exists
			for block in self.else_block:
				block.evaluate()

	def display(self, indents):
		print('%sif: %s' % ('  ' * indents, self.cond))
		for struct in self.if_block:
			if type(struct) == type(self):
				struct.display(indents + 1)
			else:
				print('%s%s' % ('  ' * (indents + 1), str(struct)))
		if self.else_block:
			print('%selse:' % '  ' * indents)
			for struct in self.else_block:
				if type(struct) == type(self):
					struct.display(indents + 1)
				else:
					print('%s%s' % ('  ' * (indents + 1), str(struct)))

	def __str__(self):
		self.display(0)
		return ''

class ConditionStructureLoop:
	def __init__(self, loops, loop_block):
		self.loops = loops
		self.loop_block = loop_block

	def evaluate(self):
		for i in range(self.loops):
			for block in self.loop_block:
				block.evaluate()

	def display(self, indents):
		print('%sfor: %i' % ('  ' * indents, self.loops))
		for struct in self.loop_block:
			if type(struct) == type(self):
				struct.display(indents + 1)
			else:
				print('%s%s' % ('  ' * (indents + 1), str(struct)))

	def __str__(self):
		self.display(0)
		return ''


# block1 = ConditionBlock("IF", "something", "action")
# block2 = ConditionBlock("ELSE", None, "action2")

# structure = ConditionStructure(block1, block2)

# structure.if_block.runAction()