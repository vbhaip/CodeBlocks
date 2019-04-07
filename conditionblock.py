class ConditionBlock:

	def __init__(self, cond_type, action):
		self.cond_type = cond_type
		self.action = action

	def evaluate(self):
		exec(self.action)



