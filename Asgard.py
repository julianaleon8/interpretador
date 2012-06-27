#!/usr/bin/python
# interpretador lexico 
# Gustavo Ortega 09-10590
# Juliana Leon 08-10608
from ply.lex import TOKEN

import ply.lex as lex
import ply.yacc as yacc
import sys
from Interp import *
def calcularExprBin(expr,expr1):
    global error
    if isinstance(expr,Suma):
	if (expr1.tipo=="int") & (expr.tipo=="int"):
		print "todo cool"
	else:
		if (expr.tipo!="tipo_error") & (expr1!="tipo_error"):
			print "error de tipo en la variable"
			error=True
		expr.tipo="tipo_error"
 
  
