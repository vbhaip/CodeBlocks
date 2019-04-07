from conditionblock import ConditionBlock


class WhileStructure:
    def __init__(self, while_block, cond, arg):
        self.while_block = while_block
        self.cond = cond
        self.arg = arg

    def isCondTrue(self):
        print("do if true")
