from ply import lex

literals = ['[', ']']

tokens = ['PLUS', 'MINUS', 'LSHIFT', 'RSHIFT', 'OUTPUT', 'INPUT']

t_PLUS = '\+'
t_MINUS = '-'
t_LSHIFT = '<'
t_RSHIFT = '>'
t_OUTPUT = '\.'
t_INPUT = ','

t_ignore = ' \t'

def t_NEWLINE(t):
    r'\n'
    pass

def t_error(t):
    print("Illegal Character %s", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex(debug=0)