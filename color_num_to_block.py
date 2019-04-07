from conditionblock import ConditionBlock
import actions
import datetime
import conditions

dic = {}
dic[('PINK', 4)] = ConditionBlock('if', '')
dic[('PINK', 5)] = ConditionBlock('else', '')
dic[('PINK', 6)] = ConditionBlock('for', '')

dic[('YELLOW', 4)] = conditions.check_time
dic[('YELLOW', 5)] = conditions.ret_true
dic[('YELLOW', 6)] = conditions.ret_false

dic[('GREEN', 4)]  = ConditionBlock('action', actions.open_google)
dic[('GREEN', 5)]  = ConditionBlock('action', actions.open_spotify)
dic[('GREEN', 6)]  = ConditionBlock('action', actions.print_time)
dic[('GREEN', 10)] = ConditionBlock('action', actions.get_tweets_global)
dic[('GREEN', 11)] = ConditionBlock('action', actions.get_tweets_refugees)
dic[('GREEN', 13)] = ConditionBlock('action', actions.get_tweets_yext)