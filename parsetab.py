
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "INPUT LSHIFT MINUS OUTPUT PLUS RSHIFT\n    program : expList\n    \n    empty :\n    \n    expList : exp expList \n    | empty\n    \n    exp : LSHIFT \n    | RSHIFT \n    | PLUS \n    | MINUS \n    | OUTPUT \n    | INPUT \n    | '[' expList ']'\n    "
    
_lr_action_items = {'LSHIFT':([0,3,5,6,7,8,9,10,11,14,],[5,5,-5,-6,-7,-8,-9,-10,5,-11,]),'RSHIFT':([0,3,5,6,7,8,9,10,11,14,],[6,6,-5,-6,-7,-8,-9,-10,6,-11,]),'PLUS':([0,3,5,6,7,8,9,10,11,14,],[7,7,-5,-6,-7,-8,-9,-10,7,-11,]),'MINUS':([0,3,5,6,7,8,9,10,11,14,],[8,8,-5,-6,-7,-8,-9,-10,8,-11,]),'OUTPUT':([0,3,5,6,7,8,9,10,11,14,],[9,9,-5,-6,-7,-8,-9,-10,9,-11,]),'INPUT':([0,3,5,6,7,8,9,10,11,14,],[10,10,-5,-6,-7,-8,-9,-10,10,-11,]),'[':([0,3,5,6,7,8,9,10,11,14,],[11,11,-5,-6,-7,-8,-9,-10,11,-11,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,12,14,],[-2,0,-1,-2,-4,-5,-6,-7,-8,-9,-10,-3,-11,]),']':([3,4,5,6,7,8,9,10,11,12,13,14,],[-2,-4,-5,-6,-7,-8,-9,-10,-2,-3,14,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'expList':([0,3,11,],[2,12,13,]),'exp':([0,3,11,],[3,3,3,]),'empty':([0,3,11,],[4,4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> expList','program',1,'p_prog','BrainFuckParser.py',7),
  ('empty -> <empty>','empty',0,'p_empty','BrainFuckParser.py',13),
  ('expList -> exp expList','expList',2,'p_expList','BrainFuckParser.py',19),
  ('expList -> empty','expList',1,'p_expList','BrainFuckParser.py',20),
  ('exp -> LSHIFT','exp',1,'p_exp','BrainFuckParser.py',29),
  ('exp -> RSHIFT','exp',1,'p_exp','BrainFuckParser.py',30),
  ('exp -> PLUS','exp',1,'p_exp','BrainFuckParser.py',31),
  ('exp -> MINUS','exp',1,'p_exp','BrainFuckParser.py',32),
  ('exp -> OUTPUT','exp',1,'p_exp','BrainFuckParser.py',33),
  ('exp -> INPUT','exp',1,'p_exp','BrainFuckParser.py',34),
  ('exp -> [ expList ]','exp',3,'p_exp','BrainFuckParser.py',35),
]
