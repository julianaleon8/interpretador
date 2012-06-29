from asgard import *
import ply.lex as lex
import ply.yacc as yacc

def calcularExprBin(exp):
	if(isinstance(exp,OpBin)):
		aux = exp.op1
		aux2 = exp.op2
		if(isinstance(aux,OpBin)):
			temp = esSuma(aux)
		else:
			if(type(aux) == int):
				temp = 'integer'
			elif(tabla.has_key(aux)):
				temp = tabla[aux]
				temp = temp[0]

		if(isinstance(aux2,OpBin)):
			temp2 = esSuma(aux2)
		else:
			if(type(aux2) == int):
				temp2 = 'integer'
			elif(tabla.has_key(aux2)):
				temp2 = tabla[aux2]
				temp2 = temp2[0]

		if(temp2 == temp):
			return 'integer'
		else:
			return '1'



#if (isinstance(arbol, Impre)):
#	print 'chap'
#	if (isinstance(arbol, Asig)):
#		print 'hola'
#		calcularExprBin()	
#elif(isinstance(arbol,Impre_uni)):
#	aux = arbol.expr
#	if(isinstance(aux,Asig)):
#		aux2 = aux.ex1
#		aux = aux.iden
#		print 'jajaja'
#		if(tabla.has_key(aux)):
#			temp = tabla[aux]
#			temp2 = temp[0]
#			temp3 = esSuma(aux2)
#			if(temp2 == temp3):
#				print 'yey'
#			else:
#				print 'error de tipo'
		#if(type(aux) == TkIdent):
		#	if(isinstance(aux2,Suma)):
		#		aux = aux2.op1
		#		aux2 = aux2.op2
		#		if(type(aux) == TkNum):
		#			if(type(aux2) == TkNum):
		#				print 'yey'



#!/usr/bin/python
# asgardretador lexico 
# Gustavo Ortega 09-10590
# Juliana Leon 08-10608
'''from ply.lex import TOKEN

import ply.lex as lex
import ply.yacc as yacc
import sys
def calcular(expr,expr1,expr2):
    global error
  if isinstance(expr,asgard.Suma):
	if (expr1.tipo == expr2.tipo):
		expr.tipo = expr1.tipo
		print "todo cool"
	else:
		if (expr2.tipo!="tipo_error") & (expr1!="tipo_error"):
			print "error de tipo en la variable"
			error=True
		expr.tipo="tipo_error"
  elif isinstance(expr,asgard.Resta):
	if (expr1.tipo=="int") & (expr2.tipo=="int"):
		expr.tipo="int"
	else:
		if (expr1.tipo!="tipo_error") & (expr2.tipo!="tipo_error"):
			print "Error de tipo en la variable esperaba tipos int"
			error=True
		expr.tipo="tipo_error"
  elif isinstance(expr,asgard.Mult):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
		if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
			print "Error de tipo en la variable esperaba tipos int"
			error=True
		expr.tipo="tipo_error"

  elif isinstance(expr,asgard.Div):
	if (expr2.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
		if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
			print "Error de tipo en la variable esperaba tipos int"
			error=True
            expr.tipo="tipo_error"
   elif isinstance(expr,asgard.Modulo):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
	if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
	expr.tipo="tipo_error"
  elif isinstance(expr,asgard.And):
	if (expr.tipo=="bool") & (expr1.tipo=="bool"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  elif isinstance(expr,asgard.Or):
	if (expr.tipo=="bool") & (expr1.tipo=="bool"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  elif isinstance(expr,asgard.Menor):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  
  elif isinstance(expr,asgard.Mayor):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  elif isinstance(expr,asgard.MenorIg):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  elif isinstance(expr,asgard.MayorIg):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  elif isinstance(expr,asgard.Igual):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  elif isinstance(expr,asgard.Desigual):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  else:
	print 'jojo'
  '''
