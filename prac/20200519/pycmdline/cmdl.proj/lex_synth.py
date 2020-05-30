# lex
literals = ['+', '-']

tokens = ['NUMBER']

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

t_ignore = " \t"

def t_error(t):
    print("invalid character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

# synthax
def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]

def p_error(p):
    if p:
        print("error at '%s'" % p.value)
    else:
        print("EOF error")

import ply.yacc as yacc
parser = yacc.yacc()

import readline

while s := input(">> "):
    yacc.parse(s)
