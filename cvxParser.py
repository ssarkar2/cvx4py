from cvxLexer import cvxLexer
from ply import yacc

class cvxParser(object):
    def __init__(self):
        self.lexerObj = cvxLexer()
        self.lexerObj.buildLex()
        #self.parserObj = yacc.yacc(module = self)  #define rules and uncomment this line to build parser.


    def parse(self, cvxProgramString):
        pass
        #return self.parserObj.parse(cvxProgramString)  #uncomment once parser is implemented


    #implement a bunch of functions required for parser here
    #def p_program(self, p)  #https://github.com/cvxgrp/qcml/blob/master/src/qc_parser.py
        #pass
