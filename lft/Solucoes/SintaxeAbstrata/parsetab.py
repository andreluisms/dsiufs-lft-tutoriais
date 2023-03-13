
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ATRIBUICAO DIVIDE DO ELSE ENDIF ENDWHILE ID IF MAIS MENOS NUMERO PONTOEVIRGULA THEN VAR VEZES WHILEprograma : listadecomandoslistadecomandos : comando\n                      |  comando listadecomandoscomando : VAR ID ATRIBUICAO expressao PONTOEVIRGULAcomando : ID ATRIBUICAO expressao PONTOEVIRGULAcomando : IF expressao THEN listadecomandos ELSE listadecomandos ENDIFcomando : WHILE expressao DO listadecomandos ENDWHILEexpressao : expressao MAIS expressaoexpressao : expressao MENOS expressaoexpressao : expressao VEZES expressaoexpressao : expressao DIVIDE expressaoexpressao : IDexpressao : NUMERO'
    
_lr_action_items = {'VAR':([0,3,17,22,24,31,32,33,35,],[4,4,4,4,-5,-4,4,-7,-6,]),'ID':([0,3,4,6,7,10,15,17,18,19,20,21,22,24,31,32,33,35,],[5,5,9,12,12,12,12,5,12,12,12,12,5,-5,-4,5,-7,-6,]),'IF':([0,3,17,22,24,31,32,33,35,],[6,6,6,6,-5,-4,6,-7,-6,]),'WHILE':([0,3,17,22,24,31,32,33,35,],[7,7,7,7,-5,-4,7,-7,-6,]),'$end':([1,2,3,8,24,31,33,35,],[0,-1,-2,-3,-5,-4,-7,-6,]),'ELSE':([3,8,24,25,31,33,35,],[-2,-3,-5,32,-4,-7,-6,]),'ENDWHILE':([3,8,24,30,31,33,35,],[-2,-3,-5,33,-4,-7,-6,]),'ENDIF':([3,8,24,31,33,34,35,],[-2,-3,-5,-4,-7,35,-6,]),'ATRIBUICAO':([5,9,],[10,15,]),'NUMERO':([6,7,10,15,18,19,20,21,],[13,13,13,13,13,13,13,13,]),'THEN':([11,12,13,26,27,28,29,],[17,-12,-13,-8,-9,-10,-11,]),'MAIS':([11,12,13,14,16,23,26,27,28,29,],[18,-12,-13,18,18,18,18,18,18,18,]),'MENOS':([11,12,13,14,16,23,26,27,28,29,],[19,-12,-13,19,19,19,19,19,19,19,]),'VEZES':([11,12,13,14,16,23,26,27,28,29,],[20,-12,-13,20,20,20,20,20,20,20,]),'DIVIDE':([11,12,13,14,16,23,26,27,28,29,],[21,-12,-13,21,21,21,21,21,21,21,]),'DO':([12,13,14,26,27,28,29,],[-12,-13,22,-8,-9,-10,-11,]),'PONTOEVIRGULA':([12,13,16,23,26,27,28,29,],[-12,-13,24,31,-8,-9,-10,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'listadecomandos':([0,3,17,22,32,],[2,8,25,30,34,]),'comando':([0,3,17,22,32,],[3,3,3,3,3,]),'expressao':([6,7,10,15,18,19,20,21,],[11,14,16,23,26,27,28,29,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> listadecomandos','programa',1,'p_programa','sintatico.py',24),
  ('listadecomandos -> comando','listadecomandos',1,'p_listadecomandos','sintatico.py',28),
  ('listadecomandos -> comando listadecomandos','listadecomandos',2,'p_listadecomandos','sintatico.py',29),
  ('comando -> VAR ID ATRIBUICAO expressao PONTOEVIRGULA','comando',5,'p_comando_declaracaovariavel','sintatico.py',36),
  ('comando -> ID ATRIBUICAO expressao PONTOEVIRGULA','comando',4,'p_comando_atribuicao','sintatico.py',40),
  ('comando -> IF expressao THEN listadecomandos ELSE listadecomandos ENDIF','comando',7,'p_comando_if','sintatico.py',44),
  ('comando -> WHILE expressao DO listadecomandos ENDWHILE','comando',5,'p_comando_while','sintatico.py',48),
  ('expressao -> expressao MAIS expressao','expressao',3,'p_expressao_soma','sintatico.py',52),
  ('expressao -> expressao MENOS expressao','expressao',3,'p_expressao_sub','sintatico.py',57),
  ('expressao -> expressao VEZES expressao','expressao',3,'p_expressao_mul','sintatico.py',61),
  ('expressao -> expressao DIVIDE expressao','expressao',3,'p_expressao_div','sintatico.py',65),
  ('expressao -> ID','expressao',1,'p_expressao_id','sintatico.py',69),
  ('expressao -> NUMERO','expressao',1,'p_expressao_num','sintatico.py',73),
]