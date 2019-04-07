#example of how one conditional structure would work
import conditionstruc as cs
import whilestruc as ws
import conditionblock as cb
arg = 0
action1 = 'print(\'action1\')'
action2 = 'print(\'action2\')'
action3 = 'print(\'action3\')\narg+=1'
block1 = cb.ConditionBlock("IF", action1)
block2 = cb.ConditionBlock("ELSE", action2)
block3 = cb.ConditionBlock("WHILE", action3)
cond1 = '5+5==11'
cond2 = 'arg<10'
structure1 = cs.ConditionStructure(block1, block2, cond1)
structure2 = ws.WhileStructure(block3, cond2, arg)
if eval(structure1.cond) == True:
    structure1.if_block.runAction()
elif eval(structure1.cond) == False:
    structure1.else_block.runAction()
while eval(structure2.cond) == True:
    structure2.while_block.runAction()
