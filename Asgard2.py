#!/usr/bin/python
# interpretador lexico 
# Gustavo Ortega 09-10590
# Juliana Leon 08-10608
from ply.lex import TOKEN

import ply.lex as lex
import ply.yacc as yacc
import sys
def calcularExprBin(expr,expr1):
    global error
  if isinstance(expr,Interp.Suma):
	if (expr1.tipo=="int") & (expr.tipo=="int"):
		print "todo cool"
	else:
		if (expr.tipo!="tipo_error") & (expr1!="tipo_error"):
			print "error de tipo en la variable"
			error=True
		expr.tipo="tipo_error"
  elif isinstance(expr,Interp.Resta):
	if (expr1.tipo=="int") & (expr.tipo=="int"):
		expr.tipo="int"
	else:
		if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
			print "Error de tipo en la variable esperaba tipos int"
			error=True
		expr.tipo="tipo_error"
  elif isinstance(expr,Interp.Mult):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
		if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
			print "Error de tipo en la variable esperaba tipos int"
			error=True
		expr.tipo="tipo_error"

  elif isinstance(expr,Interp.Div):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
		if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
			print "Error de tipo en la variable esperaba tipos int"
			error=True
            expr.tipo="tipo_error"
   elif isinstance(expr,Interp.Modulo):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
	if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
	expr.tipo="tipo_error"
  elif isinstance(expr,Interp.And):
	if (expr.tipo=="bool") & (expr1.tipo=="bool"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  elif isinstance(expr,Interp.Or):
	if (expr.tipo=="bool") & (expr1.tipo=="bool"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  elif isinstance(expr,Interp.Menor):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  
  elif isinstance(expr,Interp.Mayor):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  elif isinstance(expr,Interp.MenorIg):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  elif isinstance(expr,Interp.MayorIg):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  elif isinstance(expr,Interp.Igual):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  elif isinstance(expr,Interp.Desigual):
	if (expr.tipo=="int") & (expr1.tipo=="int"):
		expr.tipo
	else:
	    if (expr1.tipo!="tipo_error") & (expr.tipo!="tipo_error"):
                print "Error de tipo en la variable esperaba tipos int"
                error=True
            expr.tipo="tipo_error"
  
