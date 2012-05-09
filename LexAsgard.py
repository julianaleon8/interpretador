#!/usr/bin/python
# interpretador lexico 

import lex
import sys

# lista de tokens 
tokens = (
		'TkComa','TkPuntoYComa','TkParAbre','TkParCierra','TkLienzo','TkIdent','TkNum','TkSuma','TkResta','TkMult',
		'TkDiv','TkMod','TkConjuncion','TkDisyuncion','TkNegacion','TkMenor','TkMenorIgual','TkMayor','TkMayorIgual',
		'TkIgual','TkDesIgual','TkHorConcat','TkVerConcat','TkRot','TkTras','TkAsignacion',
		)
	  
# lista de tokens reservados
reserved = {
		'using' : 'TkUsing', 'of type' : 'TkOfType', 'integer' : 'TkInteger', 'boolean' : 'TkBoolean', 'canvas' : 'TkCanvas',
		'begin' : 'TkBegin', 'from' : 'TkFrom', 'while' : 'TkWhile', 'to' : 'TkTo', 'repeat' : 'TkRepeat', 'with' : 'TkWith',
		'if' : 'TkIf', 'else' : 'TkElse', 'done' : 'TkDone', 'end' : 'TkEnd', 'then' : 'TkThen', 'read' : 'TkRead',
		'print' : 'TkPrint', 'true' : 'TkTrue', 'false' : 'TkFalse'
		}
	      
#precedence= (
#	('left','TkLienzo','TkDiv'),
#	('left','TkLienzo','TkMenor'))

# valores a ignorar
# los valores de ^ y $ fuera de los corchetes significa que es el inicio de linea y el final de linea respectivamente
t_ignore = ' \t^{[-a-zA-Z0-9]*}$ '

# para saber el numeros de lineas
def t_newline(t):
	r'\n'
	t.lexer.lineno += 1

# definicion de expresiones
def t_TkNum(t):
	r'([0-9]+)'
	try:
		t.value = int(t.value)
	except ValueError:
		print 'Error de decimal'
	print t

def t_TkIdent(t):
	r'(([a-zA-Z]([a-zA-Z0-9]*))|(of type))'
        t.type = reserved.get(t.value,'TkIdent')
	print t


def t_TkLienzo(t):
	r'<([/]|[\\]|[\-]|[_]|empty)>'
	t.type = reserved.get(t.value,'TkLienzo')
	print t

def t_error(t):
	print ("Error: Caracter inesperado %s en la fila %d columna " % (t.value[0],t.lineno))
	lexer.skip(1)

# valores de los tokens simples

t_TkComa = r','
t_TkPuntoYComa = r';'
t_TkParAbre = r'\('
t_TkParCierra = r'\)'
t_TkSuma = r'\+'
t_TkResta = r'-'
t_TkMult = r'\*'
t_TkDiv = r'/'
t_TkMod = r'%'
t_TkConjuncion = r'/\\'
t_TkDisyuncion = r'\\/'
t_TkNegacion = r'\^'
t_TkMenor = r'<'
t_TkMenorIgual = r'<='
t_TkMayor = r'>'
t_TkMayorIgual = r'>='
t_TkIgual = r'='
t_TkDesIgual = r'/='
t_TkHorConcat = r':'
t_TkVerConcat = r'\|'
t_TkRot = r'\$'
t_TkTras = r'\''
t_TkAsignacion = r':='

# contruir el analizador lexico
<<<<<<< HEAD
=======
lexer=lex.lex(debug=0)
>>>>>>> 70eda21f30709571decd13b80754fde074727bb7

lexer=lex.lex(debug=1)
# abrir archivo
f = open(sys.argv[1],"r")
# leer archivo
lexer.input(f.read())
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    
   # if tok ==  
    print tok
