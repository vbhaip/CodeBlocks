from conditionblock import ConditionBlock
import actions

dic = {}
dic[('PINK', 4)] = ConditionBlock('if', '')
dic[('PINK', 5)] = ConditionBlock('else', '')

dic[('YELLOW', 4)] = True
dic[('YELLOW', 5)] = False

dic[('GREEN', 4)] = ConditionBlock('action', actions.print_time)
dic[('GREEN', 5)] = ConditionBlock('action', actions.open_spotify)
dic[('GREEN', 6)] = ConditionBlock('action', 'print("i am 6")')