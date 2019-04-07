class ConditionBlock:
	def __init__(self, cond_type, action):
		self.cond_type = cond_type
		self.action = action

	def evaluate(self):
		self.action()

	def __str__(self):
		return str(self.action)