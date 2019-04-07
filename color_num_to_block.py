from conditionblock import ConditionBlock
import actions

dic = {}
dic[('ORANGE', 4)] = ConditionBlock('if', '')
dic[('ORANGE', 5)] = ConditionBlock('else', '')

dic[('YELLOW', 4)] = ConditionBlock('cond', '"my condition"')

dic[('GREEN', 4)] = ConditionBlock('action', 'print("i am 4")')
dic[('GREEN', 5)] = ConditionBlock('action', actions.open_spotify)
dic[('GREEN', 6)] = ConditionBlock('action', 'print("i am 6")')