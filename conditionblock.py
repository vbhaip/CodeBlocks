class ConditionBlock:

	def __init__(self, cond_type, cond, action):
		self.cond_type = cond_type
		self.cond = cond
		self.action = action

	def runAction(self):
		print("action")