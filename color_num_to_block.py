from conditionblock import ConditionBlock

dic = {}
dic[('pink', 4)] = ConditionBlock('if', '')
dic[('pink', 5)] = ConditionBlock('else', '')

dic[('yellow', 4)] = ConditionBlock('cond', '"my condition"')

dic[('green', 4)] = ConditionBlock('action', 'print("i am 4")')
dic[('green', 5)] = ConditionBlock('action', 'print("i am 5")')
dic[('green', 6)] = ConditionBlock('action', 'print("i am 6")')