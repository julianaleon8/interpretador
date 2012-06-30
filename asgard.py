#!/usr/bin/python
# interpretador lexico 
# Gustavo Ortega 09-10590
# Juliana Leon 08-10608

from ply.lex import TOKEN

import ply.lex as lex
import ply.yacc as yacc
import sys

# lista de tokens reservados
reserved = {
		'using' : 'TkUsing', 'of type' : 'TkOfType', 'integer' : 'TkInteger', 'boolean' : 'TkBoolean', 'canvas' : 'TkCanvas',
		'begin' : 'TkBegin', 'from' : 'TkFrom', 'while' : 'TkWhile', 'to' : 'TkTo', 'repeat' : 'TkRepeat', 'with' : 'TkWith',
		'if' : 'TkIf', 'else' : 'TkElse', 'done' : 'TkDone', 'end' : 'TkEnd', 'then' : 'TkThen', 'read' : 'TkRead',
		'print' : 'TkPrint', 'true' : 'TkTrue', 'false' : 'TkFalse'
		}

# lista de tokens 

tokens = [
		'TkComa','TkPuntoYComa','TkParAbre','TkParCierra','TkLienzo','TkIdent','TkNum','TkSuma','TkResta','TkMult',
		'TkDiv','TkMod','TkConjuncion','TkDisyuncion','TkNegacion','TkMenor','TkMenorIgual','TkMayor','TkMayorIgual',
		'TkIgual','TkDesIgual','TkHorConcat','TkVerConcat','TkRot','TkTras','TkAsignacion',
		] + list(reserved.values())



# defincion para reconocer el token TkOfType
ab1	= r'of([\s\n\t]+ |{-[^\\]*-} )+type'

@TOKEN(ab1)
def t_ID(t):
	t_ID.__doc__ = ab1
	t.type = reserved.get(t.value,'TkOfType')
	for i in range(0,len(t.value)):
		if (t.value[i] == '\n'):
			t.lexer.lineno += 1
	return t

# definicion obtener el numero de lineas leidas
def t_newline(t):
	r'\n'
	t.lexer.lineno += 1


# definicion para ignorar comentarios
def t_COMMENT(t):
	#r'{-[ 0-9a-zA-Z<>/:=\\?\+\*#%()\[\]\t\n,;\.}{!"]*|[ 0-9a-zA-Z<>/:=\\?\+\*#%()\[\]\t\n,;\.}{!"]*-}'
	r'{-[^\\]*-}'	
	for i in range(0,len(t.value)):
		if (t.value[i] == '\n'):
			t.lexer.lineno += 1
	pass	
# definicion de expresiones

def t_TkNum(t):
	r'[0-9]+'
	try:
		t.value = int(t.value)
	except ValueError:
		print 'Error de decimal'
	return t

def t_TkIdent(t):
	r'[a-zA-Z0-9]+'
        t.type = reserved.get(t.value,'TkIdent')
        if (t.type == reserved.get(t.value,'reserved')):
	  return t
	else:
	  return t

def t_TkLienzo(t):
	r'<([/]|[\\]|[\-]|[_]|[ ]|empty)>' 
	return t

# definicion para saber en que columna se encuentra un caracter
# referencia a  http://mmandrille.googlecode.com/svn-history/r4/compiladores/Version_Final/Pascal_Lex.py, 
# se realizaron los ajustes necesarios a nuestra implementacion
def column(input,token):
    i = token.lexpos
    j = 0
    k = 0  
    while i > 0:
        if input[i] == '\n':
		break
        if input[i] == '\t': 
            	k +=1        #si el caracter es un tab tengo un contador para la cantidad de tabs
        i -=1                #resta la cantidad de caracteres (no se considera tab como 8 caracteres, sino como uno solo) desde la columna 					relativa (la que maneja python) del token hasta el principio de la linea del token
    if (token.lineno == 1):
        k +=0
        j = 0
    else:
        j = 1
    column = ((((token.lexpos - i) + (k*8)) - k) - j) +1     #formula que calcula las columnas
    return column



t_ignore = ' \t'


def t_error(t):
	print ("Error: Caracter inesperado %s en la fila %d columna %s " % (t.value[0],t.lineno,column(archi,t)))
	lexer.skip(1)
	count[0] = 1

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
archi = sys.stdin.read()

#----------------#
# Precedencia	 #
#----------------#


precedence = (
	 ('left','TkConjuncion','TkDisyuncion'),
	 ('left','TkHorConcat','TkVerConcat'),
	 ('left','TkRot'),
	 ('right','TkTras'),
    ('left', 'TkSuma', 'TkResta'),
  	 ('left','TkMult','TkDiv','TkMod'),
  	 ('right','TkNegacion'),
  	 ('left','TkIgual','TkDesIgual')
)


#----------------#
#    impresion   #
#----------------#

class Impre:
	def __init__(self,expr1,expr2):
		self.expr1 = expr1
		self.expr2 = expr2
	def __str__(self):
		return str(self.expr1) + ';' + str(self.expr2)

class Impre_uni:
	def __init__(self,expr):
		self.expr = expr
	def __str__(self):
		return str(self.expr)

class Impre_err:
	def __init__(self,expr):
		self.expr = expr
	def __str__(self):
		temp = 'SECUENCIACION'
		for expr in self.expr:
			temp = temp + str(expr) + ';'
		temp = temp[:-1]
		return "Error: " + aux

class Impre2:
	def __init__(self,expr1,expr2):
		self.expr1 = expr1
		self.expr2 = expr2
	def __str__(self):
		return str(self.expr1) + " ; " + str(self.expr2)


class expresion : pass



class OpBin(expresion):
	def __init__(self,op1,op2):
		self.op1 = op1
		self.op2 = op2

class Suma(OpBin):
	def __str__(self):
		return "Suma(" + "operador izquierdo= " + str(self.op1) + " ,operador derecho= " + str(self.op2) + ")" 

class Resta(OpBin):
	def __str__(self):
		return "Resta(" + "operador izquierdo= " + str(self.op1) + " ,operador derecho= " + str(self.op2) + ")"

class Mult(OpBin):
	def __str__(self):
		return "Multiplicacion(" + "operador izquierdo= " + str(self.op1) + " ,operador derecho= " + str(self.op2) + ")"

class Div(OpBin):
	def __str__(self):
		return "Division(" + "operador izquierdo= " + str(self.op1) + " ,operador derecho= " + str(self.op2) + ")"

class Modulo(OpBin):
	def __str__(self):
		return "Modulo(" + "operador izquierdo= " + str(self.op1) + " ,operador derecho= " + str(self.op2) + ")"

class And(OpBin):
	def __str__(self):
		return "And(" + "operador izquierdo= " + str(self.op1) + " ,operador derecho= " + str(self.op2) + ")"

class Or(OpBin):
	def __str__(self):
		return "Or(" + "operador izquierdo= " + str(self.op1) + " ,operador derecho= " + str(self.op2) + ")"

class Menor(OpBin):
	def __str__(self):
		return "Menor que(" + "operador izquierdo= " + str(self.op1) + " ,operador derecho= " + str(self.op2) + ")"

class MenorIg(OpBin):
	def __str__(self):
		return "Menor igual(" + "operador izquierdo= " + str(self.op1) + " ,operador derecho= " + str(self.op2) + ")"

class Mayor(OpBin):
	def __str__(self):
		return "Mayor que(" + "operador izquierdo= " + str(self.op1) + " ,operador derecho= " + str(self.op2) + ")"

class MayorIg(OpBin):
	def __str__(self):
		return "Mayor igual(" + "operador izquierdo= " + str(self.op1) + " ,operador derecho= " + str(self.op2) + ")"

class Igual(OpBin):
	def __str__(self):
		return "Igual(" + "operador izquierdo= " + str(self.op1) + " ,operador derecho= " + str(self.op2) + ")"

class Desigual(OpBin):
	def __str__(self):
		return "Desigual(" + "operador izquierdo= " + str(self.op1) + " ,operador derecho= " + str(self.op2) + ")"

class ConcatVer(OpBin):
	def __str__(self):
		return "Concadenacion Vertical(" + "operador izquierdo= " + str(self.op1) + " ,operador derecho= " + str(self.op2) + ")"

class ConcatHor(OpBin):
	def __str__(self):
		return "Concadenacion Horizontal(" + "operador izquierdo= " + str(self.op1) + " ,operador derecho= " + str(self.op2) + ")"

class OpUn(expresion):
	def __init__(self,op1):
		self.op1 = op1

class Menos(OpUn):
	def __str__(self):
		return "Negativo(" + str(self.op1) + ")"

class Nega(OpUn):
	def __str__(self):
		return "Negacion(" + str(self.op1) + ")"

class Rota(OpUn):
	def __str__(self):
		return "Rotacion(" + str(self.op1) + ")"

class Trans(OpUn):
	def __str__(self):
		return "Traspocision(" + str(self.op1) + ")"

class IfElse(expresion):
	def __init__(self,boolean,ex1,ex2):
		self.boolean = boolean
		self.ex1 = ex1
		self.ex2 = ex2

	def __str__(self):
		return "If-Else(" + "Condicion= "+ str(self.boolean) + " ,Instruccion= " + str(self.ex1) + " ,Instruccion= " + str(self.ex2) + ")"

class IfS(expresion):
	def __init__(self,boolean,ex1):
		self.boolean = boolean
		self.ex1 = ex1
	def __str__(self):
		return "If(" + "Condicion= "+ str(self.boolean) + " ,Instruccion= " + str(self.ex1) + ")"

class While(expresion):
	def __init__(self,boolean,ex1):
		self.boolean = boolean
		self.ex1 = ex1
	def __str__(self):
		return "While(" + "Condicion= "+ str(self.boolean) + " ,Instruccion= " + str(self.ex1) + ")"

class Fro(expresion):
	def __init__(self,num1,num2,ex1):
		self.num1 = num1
		self.num2 = num2
		self.ex1 = ex1
	def __str__(self):
		return "From(" + "Limite Inferior= " + str(self.num1) + " ,Limite Superior = " + str(self.num2) + " ,Instruccion" + str(self.ex1) + ")"

class With(expresion):
	def __init__(self,iden,num1,num2,ex1):
		self.iden = iden
		self.num1 = num1
		self.num2 = num2
		self.ex1= ex1
	def __str__(self):
		return "From-With(" + "Contador= " + str(self.iden) + " ,Limite Inferior = " + str(self.num1) + " ,Limite Superior= " + str(self.num2) + " ,Instruccion= " + str(self.ex1) + ")"

class Asig(expresion):
	def __init__(self,iden,ex1):
		self.iden = iden
		self.ex1 = ex1
	def __str__(self):
		return "Asignacion(" + "Variable= " + str(self.iden) + ", Expresion= " + str(self.ex1) + ")"

class Read(expresion):
	def __init__(self,iden):
		self.iden = iden
	def __str__(self):
		return "Read(" + "Variable= " + str(self.iden) + ")"

class Print(expresion):
	def __init__(self,iden):
		self.iden = iden
	def __str__(self):
		return "Print(" + "Lienzo= " + str(self.iden) + ")"


#####################
# FUNCIONES DE TIPO #
#####################

def evaluar(arbol):
	if (isinstance(arbol, Impre)):
		aux1 = arbol.expr1
		aux2 = arbol.expr2
		if(isinstance(aux1, Impre_uni)):
			evaluar(aux1)
		elif(isinstance(aux1, Impre)):
			evaluar(aux1)
		if(isinstance(aux2,Impre)):
			evaluar(aux2)
		elif(isinstance(aux2,Impre_uni)):
			evaluar(aux2)
		else:
			print 'jojo'
			
	elif(isinstance(arbol,Impre_uni)):
		aux = arbol.expr
		if(isinstance(aux,Asig)):
			aux2 = aux.ex1
			aux = aux.iden
			temp2 = Tipo(aux)
			temp3 = calcularExprBin(aux2)
			if(temp2 == temp3):
				pass
			else:
				print 'error de tipo1 {0}'.format(temp2)
		elif(isinstance(aux,IfElse)):
			aux = aux.boolean
			if(isinstance(aux,OpBin)):
				temp = calcularExprBin(aux)
			else:
				temp = Tipo(aux)
			if(temp == 'boolean'):
				pass
			else:
				print 'error de tipo {0}'.format(temp)
		elif(isinstance(aux,IfS)):
			aux = aux.boolean
			if(isinstance(aux,OpBin)):
				temp = calcularExprBin(aux)
			else:
				temp = Tipo(aux)
			if(temp == 'boolean'):
				pass
			else:
				print 'error de tipo {0}'.format(temp)
		elif(isinstance(aux,While)):
			aux = aux.boolean
			if(isinstance(aux,OpBin)):
				temp = calcularExprBin(aux)
			else:
				temp = Tipo(aux)
			if(temp == 'boolean'):
				pass
			else:
				print 'error de tipo {0}'.format(temp)
		
	



def Tipo(aux):
	if(tabla.has_key(aux)):
			temp = tabla[aux]
			temp = temp[0]
			return temp
	elif(type(aux) == int):
			temp = 'integer'
			return temp
	elif(aux == 'true' or aux == 'false'):
			return 'boolean'
	elif(aux[0] == '<'):
			return 'canvas'


def calcularExprBin(exp):
	if(isinstance(exp,OpBin)):
		aux = exp.op1
		aux2 = exp.op2
		if(isinstance(exp,Menor)):
			if(isinstance(aux,OpBin)):
				temp = calcularExprBin(aux)
			else:
				temp = Tipo(aux)

			if(isinstance(aux2,OpBin)):
				temp2 = calcularExprBin(aux2)
			else:
				temp2 = Tipo(aux2)
			
			if(temp == 'integer' and temp2 == 'integer'):
				return 'boolean'
			else:
				return '1'
		elif(isinstance(exp,MenorIg)):
			if(isinstance(aux,OpBin)):
				temp = calcularExprBin(aux)
			else:
				temp = Tipo(aux)

			if(isinstance(aux2,OpBin)):
				temp2 = calcularExprBin(aux2)
			else:
				temp2 = Tipo(aux2)
		
			if(temp == 'integer' and temp2 == 'integer'):
				return 'boolean'
			else:
				return '1'
		elif(isinstance(exp,Mayor)):
			if(isinstance(aux,OpBin)):
				temp = calcularExprBin(aux)
			else:
				temp = Tipo(aux)

			if(isinstance(aux2,OpBin)):
				temp2 = calcularExprBin(aux2)
			else:
				temp2 = Tipo(aux2)
		
			if(temp == 'integer' and temp2 == 'integer'):
				return 'boolean'
			else:
				return '1'
		elif(isinstance(exp,MayorIg)):
			if(isinstance(aux,OpBin)):
				temp = calcularExprBin(aux)
			else:
				temp = Tipo(aux)

			if(isinstance(aux2,OpBin)):
				temp2 = calcularExprBin(aux2)
			else:
				temp2 = Tipo(aux2)
		
			if(temp == 'integer' and temp2 == 'integer'):
				return 'boolean'
			else:
				return '1'
		elif(isinstance(exp,Igual)):
			if(isinstance(aux,OpBin)):
				temp = calcularExprBin(aux)
			else:
				temp = Tipo(aux)

			if(isinstance(aux2,OpBin)):
				temp2 = calcularExprBin(aux2)
			else:
				temp2 = Tipo(aux2)
		
			if(temp == 'boolean' or temp2 == 'boolean'):
				return '1'
			elif(temp2 == temp):
				return 'boolean'
			else:
				return '1'
		elif(isinstance(exp,Desigual)):
			if(isinstance(aux,OpBin)):
				temp = calcularExprBin(aux)
			else:
				temp = Tipo(aux)

			if(isinstance(aux2,OpBin)):
				temp2 = calcularExprBin(aux2)
			else:
				temp2 = Tipo(aux2)
		
			if(temp == 'boolean' or temp2 == 'boolean'):
				return '1'
			elif(temp2 == temp):
				return 'boolean'
			else:
				return '1'
		elif(isinstance(aux,OpBin)):
			temp = calcularExprBin(aux)
		else:
			temp = Tipo(aux)

		if(isinstance(aux2,OpBin)):
			temp2 = calcularExprBin(aux2)
		else:
			temp2 = Tipo(aux2)
		
		if(temp2 == temp):
			return temp
		else:
			return '1'
	
	elif(isinstance(exp,OpUn)):
		aux = exp
		if(isinstance(aux,Nega)):
				aux = aux.op1
				if(isinstance(aux,OpBin)):
					temp = calcularExprBin(aux)
				else:
					temp = Tipo(aux)
				if(temp == 'boolean'):
					return temp
				else:
					return '1'
		elif(isinstance(aux,Rota)):
				aux = aux.op1
				if(isinstance(aux,OpBin)):
					temp = calcularExprBin(aux)
				else:
					temp = Tipo(aux)
				if(temp == 'canvas'):
					return temp
				else:
					return '1'
		elif(isinstance(aux,Trans)):
				aux = aux.op1
				if(isinstance(aux,OpBin)):
					temp = calcularExprBin(aux)
				else:
					temp = Tipo(aux)
				if(temp == 'canvas'):
					return temp
				else:
					return '1'
		elif(isinstance(aux,Menos)):
				aux = aux.op1
				if(isinstance(aux,OpBin)):
					temp = calcularExprBin(aux)
				else:
					temp = Tipo(aux)
				if(temp == 'integer'):
					return temp
				else:
					return '1'
	elif(type(exp) == int):
		return 'integer'
	elif(exp == 'true' or exp == 'false'):
		return 'boolean'
	elif(exp[0] == '<'):
		return 'canvas'
	else:
		return Tipo(exp)





####################	
# ARBOL SINTACTICO #
####################


tabla = {}
contador = 0
temp = []

def p_expr(p):
	''' expr : TkUsing Declar TkBegin expr TkEnd
				| expr TkPuntoYComa expr 
				| instr  '''
	global contador
	global temp
	if len(p) == 4:
		p[0] = Impre(p[1],p[3])
	elif(len(p) == 6):
		temp = []
		contador += 1
		p[0] = p[4]
		for i in tabla:
			count = contador
			aux = tabla[i]
			aux2 = aux[-1]
			while(type(aux2) == list):
				if(type(aux[1]) == int):
					aux = aux2
					aux2 = aux[-1]
				else:
					aux[1] = count					
					aux = aux2
					aux2 = aux[-1]
	else:
		p[0] = Impre_uni(p[1])

def p_empty(p):
	'empty :'
	p[0] = ''
	pass


def p_Declar(p):
	''' Declar : Declar TkComa TkIdent TkOfType Tipo
				  | Declar TkComa TkIdent
				  | TkIdent TkOfType Tipo
				  | Declar TkPuntoYComa Declar 
				  | TkIdent '''
	global temp
	global contador
	cont = 0
	if(len(p) == 4):

		if(p[2] == ','):
			temp.append(p[3])
			p[0] = p[1]
		elif(p[2] == ';'):
			temp.append(p[1])
			temp.append(p[3])
		else:
			if(tabla.has_key(p[1])):
					aux = tabla[p[1]]
					aux2 = aux[-1]
					while(type(aux2) == list):
						aux = aux2
						aux2 = aux[-1]
					if(aux[1] == contador):
						print 'variable repetida {0}'.format(p[1])
						exit(-1)
					else:
						aux3 = [p[3],contador,'']
						aux.append(aux3)
			else:
				lista = [p[3],contador,'']
				tabla[p[1]] = lista
			p[0] = tabla
	elif(len(p) == 6):
		temp.append(p[3])
		temp.append(p[1])
		for i in temp:
			if(tabla.has_key(i)):
				aux = tabla[i]
				aux2 = aux[-1]
				while(type(aux2) == list):
					aux = aux2
					aux2 = aux[-1]
				if(aux[1] == contador):
					print 'variable repetida {0}'.format(i)
					exit(1)
				else:
					aux3 = [p[5],contador,'']
					aux.append(aux3)
			else:
				lista = [p[5],contador,'']
				tabla[i] = lista
			temp = []

	else:
		if(tabla.has_key(p[1])):
				aux = tabla[p[1]]
				aux2 = aux[-1]
				while(type(aux2) == list):
					aux = aux2
					aux2 = aux[-1]
				if(aux[1] == contador):
					print 'variable2 repetida {0}'.format(p[1])
					exit(1)
				else:
					aux3 = [p[5],contador,'']
					aux.append(aux3)
		else:
					p[0]=p[1]
def p_Tipo(p):
	''' Tipo : TkInteger
				| TkBoolean
				| TkCanvas '''
	p[0] = p[1]

def p_InNum(p):
	''' InNum : TkNum
				 | TkIdent '''
	if(type(p[1]) != int):
		if(tabla.has_key(p[1])):
			aux = tabla[p[1]]
			if(aux[0] == 'integer'):
				p[0] = p[1]
			else:
				print 'La variable [{0}] debe ser de tipo entera'.format(p[1])
				exit(1)
		else:
			print 'errorde sintaxis {0} no fue declarada'.format(p[1])
			exit(1)	
	p[0] = p[1]

def p_instr(p):
	'''instr : TkIdent TkAsignacion expbin
		 	   | TkIf booleana TkThen expr TkElse expr TkDone
		 	   | TkIf booleana TkThen expr TkDone
		 	   | TkWhile booleana TkRepeat expr TkDone
		 	   | TkWith TkIdent TkFrom InNum TkTo InNum TkRepeat expr TkDone
		 	   | TkFrom InNum TkTo InNum TkRepeat expr TkDone 
		 	   | TkPrint TkIdent
		 	   | TkPrint TkLienzo
		 	   | TkRead TkIdent '''

	if (len(p)== 4):
	    if (p[2] == ':='):
	    	if(tabla.has_key(p[1])):
	    		p[0] = Asig(p[1] , p[3])
	    	else:
	    		print 'errorde sintaxis {0} no fue declarada'.format(p[1])
	    		exit(1)	
	elif(len(p) == 8):
	    if(p[1] == 'if'):
	    	p[0] = IfElse(p[2],p[4],p[6])
	    if(p[1] =='from'):
	    	p[0] = Fro(p[2],p[4],p[6])	
	elif(len(p) == 6):
	    if(p[1] == 'while'):
	    	p[0] = While( p[2] , p[4])
	    elif(p[1] == 'if'):
	    	p[0] = IfS(p[2],p[4])
	elif(len(p) == 10 ):
		if(tabla.has_key(p[2])):
			aux = tabla[p[2]]
			if(aux[0] == 'integer'):
				p[0] = With(p[2],p[4],p[6],p[8])
			else:
				print 'La variable [{0}] debe ser de tipo entera'.format(p[2])
				exit(1)
		else:
			print 'errorde sintaxis {0} no fue declarada'.format(p[2])
			exit(1)
	elif(len(p) == 3):
		if(p[1] == 'read'):
			if(tabla.has_key(p[2])):
				aux = Tipo(p[2])
				if(aux == 'integer'):
					p[0] = Read(p[2])
				else:
					print 'La variable1 [{0}] debe ser de tipo entera'.format(p[2])
					exit(1)
			else:
				print 'errorde sintaxis {0} no fue declarada'.format(p[2])
				exit(1)	
		else:	
			if(p[2][0] != '<'):
				if(tabla.has_key(p[2])):
					temp = Tipo(p[2])
					if(temp == 'canvas'):
						p[0] = Print(p[2])
					else:
						print 'La variable [{0}] debe ser de tipo canvas'.format(p[2])
						exit(1)
				else:
					print 'errorde sintaxis {0} no fue declarada'.format(p[2])
					exit(1)	
			p[0] = Print(p[2])


def p_arit(p):
	''' arit : arit operatorA arit
		 		| TkResta arit
		 		| TkParAbre arit TkParCierra
		 		| TkNum
		 		| TkIdent '''

	if(len(p) == 4):
		if(p[2] == '+'):
			p[0] = Suma(p[1],p[3])
		if(p[2] == '-'):
			p[0] = Resta(p[1],p[3])
		if(p[2] == '*'):
			p[0] = Mult(p[1],p[3])
		if(p[2] == '/'):
			p[0] = Div(p[1],p[3])
		if(p[2] == '%'): 
			p[0] = Modulo(p[1],p[3])
		if p[1] == '(':
			if p[3] == ')':
				p[0] = p[2] 
	elif(len(p) == 3):
		p[0] = Menos(p[2])
	else:
		if(type(p[1]) != int):
			if(tabla.has_key(p[1])):
				p[0] = p[1]
			else:
				print 'error de sintaxis {0} no fue declarada'.format(p[1])
				exit(1)
		p[0] = p[1]

def p_expbin(p):
	''' expbin : arit
	  		  	  | booleana
			  	  | lienzo '''
	p[0] = p[1]


def p_booleana(p):
	''' booleana : booleana operatorB booleana
		    		 | TkParAbre booleana TkParCierra
		    		 | TkTrue
		    		 | TkFalse
		    		 | TkIdent
				 	 | booleana TkNegacion
				 	 | arit
				 	 | lienzo '''
#| TkNegacion booleana

	if(len(p) == 4):
		if(p[2] == '/\\'):
			p[0] = And(p[1],p[3])
		if(p[2] == '\\/'):
			p[0] = Or(p[1],p[3])
		if(p[2] == '<'):
			p[0] = Menor(p[1], p[3])
		if(p[2] =='<='):
			p[0] = MenorIg(p[1],p[3])
		if(p[2] == '>'):
			p[0] = Mayor(p[1],p[3])
		if(p[2] == '>='):
			p[0] = MayorIg(p[1],p[3])
		if(p[2] == '='):
			p[0] = Igual(p[1],p[3])
		if(p[2] == '/='):
			p[0] = Desigual(p[1],p[3])
		if p[1] == '(':
			if p[3] == ')':
				p[0] = p[2]
	elif(len(p) == 3):
		p[0] = Nega(p[1])
	else:
		if(isinstance(p[1],OpBin)):
			p[0] = p[1]
		elif(type(p[1]) == int):
			p[0] = p[1]
		elif(p[1] != 'true'):
			if(p[1] != 'false'):
				if(tabla.has_key(p[1])):
						p[0] = p[1]
				else:
					print 'errorde sintaxis {0} no1 fue declarada'.format(p[1])
					exit(1)
		else:
			p[0] = p[1]

def p_lienzo(p):
	''' lienzo : lienzo operatorL lienzo 
		   	  | TkParAbre lienzo TkParCierra
		   	  | TkRot lienzo 
		   	  | lienzo TkTras 
		   	  | TkLienzo
		   	  | TkIdent '''

	if len(p) == 4:
		if p[2] == ':':
			p[0] = ConcatHor(p[1],p[3])
		if p[2] == '|':
			p[0] = ConcatVer(p[1],p[3])
		if p[1] == '(':
			if p[3] == ')':
				p[0] =  p[2]
	elif (len(p)==3):
		if(p[2]=='\''):
			p[0]=Trans(p[1])
		else:		
			p[0]=Rota(p[2])

	else:
		if(p[1][0] != '<'):
				if(tabla.has_key(p[1])):
					p[0] = p[1]
				else:
					print 'errorde sintaxis {0} no fue declarada'.format(p[1])
					exit(1)
		p[0] = p[1]

def p_operatorA(p):
	''' operatorA : TkSuma
					  | TkResta
					  | TkMult
					  | TkDiv
					  | TkMod '''
	p[0] = p[1]

def p_operatorB(p):
	''' operatorB : TkMenor
					  | TkMenorIgual
					  | TkMayor
					  | TkMayorIgual
					  | TkIgual
					  | TkDesIgual 
					  | TkConjuncion
					  | TkDisyuncion '''
	p[0] = p[1]

def p_operatorL(p):
	''' operatorL : TkHorConcat
					  | TkVerConcat '''
	p[0] = p[1] 			

def p_error(p):
	print "Error de sintaxis " + p.type +" " +  p.value
	exit(1)

parser = yacc.yacc()
arbol = parser.parse(archi)
evaluar(arbol)
#print tabla
#print arbol



