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

precedence= (
	('left','TkLienzo','TkDiv'),
	('left','TkLienzo','TkMenor'))

# valores a ignorar
# los valores de ^ y $ fuera de los corchetes significa que es el inicio de linea y el final de linea respectivamente

def t_comment(t):
	r'^[{][}]$'
	return None

# para saber el numeros de lineas
def t_newline(t):
	r'\n'
	t.lexer.lineno += 1
	lista.append('\n')

# definicion de expresiones
def t_TkNum(t):
	r'([0-9]+)'
	try:
		t.value = int(t.value)
	except ValueError:
		print 'Error de decimal'
	lista.append('{0}({1}) '.format(t.type,t.value))

def t_TkIdent(t):
	r'(([a-zA-Z]([a-zA-Z0-9]*))|(of type))'
        t.type = reserved.get(t.value,'TkIdent')
        if (t.type == reserved.get(t.value,'reserved')):
	  lista.append(t.type+" ")
	else:
	  lista.append('{0}("{1}") '.format(t.type,t.value))

def t_TkLienzo(t):
	r'<([/]|[\\]|[\-]|[_]|[ ]|empty)>' # fuck, arreglar esto

#	t.type = tokens.get(t.value,'TkLienzo')
	lista.append('{0}("{1}") '.format(t.type,t.value[1: len(t.value) - 1]) )

def find_column(input,token):
    i = token.lexpos
    t = 0
    k = 0   ##inicializo k en 0
    while i > 0:
        if input[i] == '\n': break
        if input[i] == '\t': ##controlar si el caracter es un tab (expresion regular '\t')
            k +=1            ##si es asi tengo un contador para la cantidad de tabs
        i -=1                ##resta la cantidad de caracteres (no se considera tab como 8 caracteres, sino como uno solo) desde la columna relativa (la que maneja python) del token hasta el principio de la linea del token
    if (token.lineno == 1):
        k +=1
        t = 0
    else:
        t = 1
    column = ((((token.lexpos - i) + (k*8)) - k) - t) +1      ##formula que calcula las columnas ok
    return column

t_ignore = ' \t'

def t_error(t):
	print ("Error: Caracter inesperado %s en la fila %d columna %s " % (t.value[0],t.lineno,find_column(archi,t)))
	lexer.skip(1)
	#count = count + 1

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
lexer=lex.lex(debug=0)

# abrir archivo
f = open(sys.argv[1],"r")
# leer archivo
archi = f.read()
lexer.input(archi)
f.close()
count = 0
lista = ['']
while True:
    tok = lexer.token()
    if not tok: 
	break      # No more input
    else: 
	lista.append(tok.type+" ")
if (count == 0):
	for i in range (0,len(lista)):
		sys.stdout.write(lista[i])
