from cvxLexer import cvxLexer
from ply import yacc

class cvxParser(object):
    def __init__(self):
        self.lexerObj = cvxLexer()
        self.lexerObj.buildLex()
        self.tokens = self.lexerObj.tokens
        #self.parserObj = yacc.yacc(module = self)  #define rules and uncomment this line to build parser.


    def parse(self, cvxProgramString):
        
        pass
        #return self.parserObj.parse(cvxProgramString)  #uncomment once parser is implemented


    #implement a bunch of functions required for parser here
    #def p_program(self, p)  #https://github.com/cvxgrp/qcml/blob/master/src/qc_parser.py
        #pass
    def p_expression_add(self,p):
        'expression : expression PLUS expression'
        p[0] = p[1] + p[3] # expression + epxression
        
    def p_expression_minus(self,p):
        'expression : expression MINUS expression'
        p[0] = p[1] - p[3]

    def p_expression_divide(self,p):
        '''expression : expression DIVIDE CONSTANT
                      | expression DIVIDE INTEGER'''
        p[0] = Number(1.0/p[3]) * p[1]    
    def p_expression_multiply(self,p):
        'expression : expression TIMES expression'
        p[0] = p[1] * p[3]

    def p_expression_group(self,p):
        'expression : LPAREN expression RPAREN'
        p[0] = p[2]

    def p_expression_negate(self,p):
        'expression : MINUS expression %prec UMINUS'
        p[0] = -p[2]

    def p_expression_transpose(self,p):
        'expression : expression TRANSPOSE'
        if isscalar(p[1]): p[0] = p[1]
        else: p[0] = Transpose(p[1])
        
