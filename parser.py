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
	lista.append(t.type+" ")

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
	r'([0-9]+)'
	try:
		t.value = int(t.value)
	except ValueError:
		print 'Error de decimal'
	#lista.append('{0} '.format(t.type))
	return t

def t_TkIdent(t):

	r'[a-zA-Z0-9]+'
        t.type = reserved.get(t.value,'TkIdent')
        if (t.type == reserved.get(t.value,'reserved')):
	  lista.append(t.type+" ")
	else:
	  #lista.append('{0} '.format(t.type))
	  return t

def t_TkLienzo(t):
	r'<([/]|[\\]|[\-]|[_]|[ ]|empty)>' 
	lista.append('{0} '.format(t.value[1: len(t.value) - 1]) )

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
t_TkTras = r'\\'
t_TkAsignacion = r':='

#contruir el analizador lexico
lexer=lex.lex(debug=0)

#abrir archivo
#f = open(sys.argv[1],"r")

# leer archivogi
archi = sys.stdin.read()
lexer.input(archi)

#f.close()
#lista que contiene un solo valor, el cual es el identificador 
#para saber si se encontro un caracter invalido o no
count = [0]
#lista que contiene todos los tokens validos 
lista = ['']
while True:
    tok = lexer.token()
    if not tok: 
	break      
    else: 
	lista.append(tok.type+" ")
if (count[0] == 0): 
#ciclo para imprimir los tokens
	for i in range (0,len(lista)):
		sys.stdout.write(lista[i])
parser = yacc.yacc
#----------------#
# Precedencia	 #
#----------------#


precedence = (
	 ('left','TkIf','TkThen','TkElse'),
  	 ('right','TkNegacion'),    	
	 ('left','TkConjuncion','TkDisyuncion'),
	 ('left','TkHorConcat','TkVerConcat'),
	 ('left','TkRot'),
	 ('right','TkTras'),
    	 ('left', 'TkSuma', 'TkResta'),
  	 ('left','TkMult','TkDiv','TkMod'),
	 #('right','menos'),
)


#----------------#
#    impresion   #
#----------------#

class Impre:
	def __init__(self,expr):
		self.expr = expr
	def __str__(self):
		temp = 'SECUENCIACION'
		for expr in self.expr:
			temp = temp + str(expr) + ';'
		temp = temp[:-1]
		return temp

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
		return "Error: " + temp
		


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
	
class form(expresion):
	def __init__(sefl,num1,num2,ex1):
		self.num1 = num1
		self.num2 = num2
		self.ex1= ex1
		def __str__(self):
			return "From(" + "Limite Inferior= " + str(self.num1) + " ,Limite Superior =" + str(self.num2) + " ,Intruccion" + str(self.ex1) + ')'
			
class FromWith(expresion):
	def __init__(self,iden,num1,num2,ex1):
		self.iden = iden
		self.num1 = num1
		self.num2 = num2
		self.ex1= ex1
	def __str__(self):
		return "From-With(" + "Contador= " + str(self.iden) + " ,Limite Inferior =" + str(self.num1) + " ,Limite Superior= " + str(self.num2) + " ,Intruccion= " + str(self.ex1) + ")"
		
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
		

####################	
# ARBOL SINTACTICO #
####################

#start='expr'
def p_expr(p):
	''' expr : expr TkPuntoYComa instr 
				| instr '''
	if len(p) == 4:
		p[0] = p[1] + p[3]
		#p[0]=Impre(p[1])
		#print(p[0]);
	elif (len(p)==2 ):
		p[0] = p[1]

def p_empty(p):
	'empty :'
	p[0] = ''
	pass
#def p_aux(p):
 #   '''aux : TkIdent
#	   | TkNum'''
 #   p[0]= Var(p[1])

def p_instr(p):
	'''instr : TkIdent TkAsignacion expbin
		 	   | TkIf booleana TkThen instr TkElse instr TkDone
		 	   | TkIf booleana TkThen instr TkDone
		 	   | TkWhile booleana TkRepeat instr TkDone
		 	   | TkWith TkIdent TkFrom TkNum TkTo TkNum TkRepeat instr TkDone
		 	   | TkFrom TkNum TkTo TkNum TkRepeat instr TkDone 
		 	   | TkPrint TkLienzo
		 	   | TkRead TkIdent 
			   | expbin'''
	
	if (len(p)== 4):

	    if (p[2] == ':='):
		p[0] = Asig (p[1] , p[3])
	elif(len(p) == 8):
	    if(p[1] == 'if'):	
    	    	p[0] = IfElse(p[2],p[4],p[6])
	    if(p[1] =='from'):
	    	p[0] = FromWith(p[2],p[4],p[6])	
	elif(len(p) == 6):
	    if(p[1] == 'while'):
	    	p[0] = While( p[2] , p[4])
	    if(p[1] == 'if'):
	    	p[0] = IfS( p[2],p[4])
	elif(len(p) == 10 ):
		p[0] = With(p[2],p[4],p[6],p[8])
	elif(len(p) == 3):
		if(p[1] == 'read'):
			p[0] = Read(p[2])
		else:
			p[0] = Print(p[2])
	elif(len(p)==2):
	     p[0]=p[1]
	    
def p_arit(p):
	''' arit : arit operatorA arit
		 		| TkResta arit
		 		| TkParAbre arit TkParCierra
		 		| TkNum
		 		| TkIdent'''

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
		if (p[1]=='-'):		
			p[0] = Menos(p[2])
	else:
		p[0] = p[1]



def p_booleana(p):
	''' booleana : booleana operatorB booleana
				 | booleana operatorB arit
				 | booleana operatorB lienzo
		    		 | TkParAbre booleana TkParCierra
		    		 | booleana TkNegacion
				 | TkTrue
		    		 | TkFalse '''
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
			p[0] = MayorIg(p[1],p[1])
		if p[1] == '(':
			if p[3] == ')':
				p[0] = p[2]
	elif(len(p) == 3):
		if (p[1]=='\^'):
			p[0] = Nega(p[1])
	elif(len(p) == 2):
		p[0] = p[1]
		print true

def p_lienzo(p):
	''' lienzo : lienzo operatorL lienzo 
		   	  | TkParAbre lienzo TkParCierra
		   	  | TkRot lienzo 
		   	  | lienzo TkTras 
		   	  | TkLienzo '''

	if (len(p) == 4):
		if (p[2] == ':'):
			p[0] = ConcatHor(p[1],p[3])
		if (p[2] == '|'):
			p[0] = ConcatVer(p[1],p[3])
		if (p[1] == '('):
			if p[3] == ')':
				p[0] =  p[2]
	else:
		p[0] = p[1]


def p_expbin(p):
	''' expbin : arit
	  	   | booleana
		   | lienzo '''
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
	print "Error de sintaxis " #+ p.type +" " + "%d" % p.value




print parser.parse(archi)


#s = ''
#i = 0
#while len(lista) != i:
#	if lista[i] == r'TkNum([0-9]+)':
#		s = s + lista[i][6]
#		print s 
#	s = s + lista[i]
#	i = i + 1
#print s 

#while True:
 #  try:
  #     s = sys.stdin.read()
   #except EOFError:
    #   break
   #if not s: continue
#result = parser.parse(s)
#print result	

#while 1:
#    try:
#        s = raw_input('calc > ')   # Use raw_input on Python 2
#    except EOFError:
#        break
#    result = parser.parse(s)
#    print result	
