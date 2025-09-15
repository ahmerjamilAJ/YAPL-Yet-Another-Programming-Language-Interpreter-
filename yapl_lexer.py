# Build the lexer
import ply.lex as lex
import re



reserved = {
    'STRING' : 'TYPE_STRING',
    'CHAR' : 'TYPE_CHAR',
    'INT' : 'TYPE_INT',
    'FLOAT' : 'TYPE_FLOAT',
    'PRINT' : 'PRINT',
    'NOT' : 'NOT',
    'AND' : 'AND',
    'OR' : 'OR',
    'TRUE' : 'TRUE',
    'FALSE' : 'FALSE',
    'BOOL' : 'TYPE_BOOL',
    'DO': 'TYPE_DO',
    'WHILE': 'TYPE_While',
    'IF' : 'TYPE_IF',
    'ELSEIF' :  'TYPE_ELSEIF',
    'ELSE' :  'TYPE_ELSE',
    'FUNCTION' : 'TYPE_FUNCTION',
    'RETURN' : 'TYPE_RETURN',
    'LIST' : 'TYPE_LIST'
    
 }

tokens = [
    'INT', 'FLOAT', 'STRING', 'CHAR', 
    'PLUS','MINUS','MULTIPLY','DIVIDE','EQUALS', 'POW', 'MOD', 'INCREMENT', 'DECREMENT',
    'LPAREN','RPAREN',
    'LESS', 'GREATER', 'LEQ', 'GEQ', 'EQUALTO', 'NEQUALTO',
    'NAME',
    'COMMA',
    'SEMICOL', 'COLON',
    'LFUNCPARAN',
    'RFUNCPARAN',
    'listLparan',
    'listRparan',
    'SLICE',
    'INDEX',
    'PUSH',
    'POP',
 ] + list(reserved.values())

# Tokens
t_INCREMENT = r'\+\+'
t_DECREMENT = r'\-\-'
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_MULTIPLY  = r'\*'
t_DIVIDE    = r'/'
t_EQUALS    = r'='
t_POW       = r'\^'
t_MOD       = r'%'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LESS      = r'<'
t_GREATER   = r'>'
t_LEQ       = r'<='
t_GEQ       = r'>='
t_EQUALTO   = r'=='
t_NEQUALTO  = r'!='
t_COMMA     = r'\,'
t_LFUNCPARAN = r'\{'
t_RFUNCPARAN = r'\}'
t_listLparan = r'\['
t_listRparan = r'\]'
t_SLICE = r'\.slice'
t_INDEX = r'\.index\('
t_SEMICOL = r'\;'
t_COLON = r'\:'
t_ignore = ' \t\r\n\f\v'
t_PUSH = r'\.push'
t_POP =  r'\.pop'


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME') 
    return t

def t_CHAR(t):
    r'\'.\''
    
    t.value = t.value[1:-1]
    
    return t
    
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


# Ignored characters
#t_ignore = " \t"

def t_lineno(t):
    r'\n'
    t.lexer.lineno += len(t.value) 
    
def t_error(t): # error while lexing
    print("[Lexer Error] Line",t.lineno)
    print(f"Illegal character: {t.value}")
    t.lexer.skip(1) # skips illegal character

lexer = lex.lex()

# ENABLE THIS TO TEST YOUR LEXER DIRECTLY
#while True:
#    print("YAPL_LEXER>>",end='')
#    lexer.input(input()) # reset lexer, store new input
#       
#    while True: # necessary to lex all tokens
#        tokenEntered = lexer.token() # return next token from lexer
#        if not tokenEntered: # lexer error also given
#            break
#        print(tokenEntered)
