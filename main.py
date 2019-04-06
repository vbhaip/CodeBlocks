import conditionstruc as cs
import conditionblock as cb
action1 = 'print(\'action1\')'
action2 = 'print(\'action2\')'
block1 = cb.ConditionBlock("IF", action1)
block2 = cb.ConditionBlock("ELSE", action2)
cond = '5+5==11'
structure = cs.ConditionStructure(block1, block2, cond)

if eval(structure.cond) == True:
    structure.if_block.runAction()
elif eval(structure.cond) == False:
    structure.else_block.runAction()

