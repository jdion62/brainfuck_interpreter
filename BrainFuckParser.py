from ply import yacc
from BrainFuckLex import tokens, lexer
from BrainFuckState import state

def p_prog(p):
    '''
    program : expList
    '''
    state.AST = p[1]

def p_empty(p):
    '''
    empty :
    '''
    p[0] = ('nil', )

def p_expList(p):
    '''
    expList : exp expList 
    | empty
    '''
    if (len(p) == 3):
        p[0] = ('seq', p[1], p[2])
    elif (len(p) == 2):
        p[0] = p[1]

def p_exp(p):
    '''
    exp : LSHIFT 
    | RSHIFT 
    | PLUS 
    | MINUS 
    | OUTPUT 
    | INPUT 
    | '[' expList ']'
    '''
    if(p[1] == '<'):
        p[0] = ('lshift', )
    elif(p[1] == '>'):
        p[0] = ('rshift', )
    elif(p[1] == '+'):
        p[0] = ('plus', )
    elif(p[1] == '-'):
        p[0] = ('minus', )
    elif(p[1] == '.'):
        p[0] = ('output', )
    elif(p[1] == ','):
        p[0] = ('input', )    
    elif(p[1] == '['):
        p[0] = ('block', p[2])
    else:
        raise ValueError("Invalid Token")
    
def p_error(p):
    print("Syntax error at '%s'" % p.value)


parser = yacc.yacc(debug=False)