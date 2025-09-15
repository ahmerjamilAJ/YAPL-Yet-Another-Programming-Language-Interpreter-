import ply.yacc as yacc
from yapl_lexer import *

#sys.tracebacklimit = 0 # to prevent traceback debug output since it is not needed
# to resolve ambiguity, individual tokens assigned a precedence level and associativity. 
# tokens ordered from lowest to highest precedence, rightmost terminal judged

precedence = (
    ('left', 'PLUS', 'MINUS'), # +, - same precedence, left associative
    ('left','MULTIPLY','DIVIDE', 'MOD'),
    ('left', 'POW'),
    
)



start = 'S'

# multiple variables, assigning data from one variable to another
# after the lexing, start parsinh

def p_start(p): # non-terminal, starting
    """
    S : stmt S 
    """
    p[0] = [p[1]] + p[2] # list comprehension used to solve recursive grammar, added/appending as well  

def p_start_empty(p):
    """
    S : 
    """
    p[0] = []

def p_print_stmt(p): # printing 
    """
    stmt : PRINT LPAREN coom RPAREN SEMICOL
         | PRINT LPAREN condition RPAREN SEMICOL
    """  
    p[0] = ('PRINT', p[3])   
    
def p_condition_handle(p):
    """
    condition : condition LESS condition
              | condition GREATER condition
              | condition LEQ condition
              | condition GEQ condition
              | condition EQUALTO condition
              | condition NEQUALTO condition
              | condition AND condition
              | condition OR condition              
    """
    p[0] = ( p[2], p[1], p[3])
    
def p_condition_des(p):
    """
    condition : exp    
    """
    p[0] = p[1]

def p_condition_not(p):
    """
    condition : NOT condition    
    """
    p[0] = ( p[1], p[2])

def p_condition_parantheses(p): # for printing
    """ 
    condition : LPAREN condition RPAREN
    """ 
    p[0] = p[2]
   
def p_print_coom(p): # printing 
    """
    coom : coom COMMA coom       
    """  
    p[0] = ( p[2] ,p[1], p[3])
    
def p_comma(p): # printing 
    """
    coom : condition        
    """  
    p[0] = (p[1])    
    
def p_exp_var(p): # for printing
    """
    exp : NAME 
         
    """
    p[0] = ( 'NAME' , p[1])
    
def p_exp_defintion(p): #
    """
    exp : INT
        | FLOAT
        | STRING   
        | CHAR
        | BOOL
             
    """  
    p[0] = ( type(p[1]).__name__ , p[1]) 
    
def p_exp_parantheses(p): # 
    """ 
    exp : LPAREN exp RPAREN
    """ 
    p[0] = p[2]

def p_exp_bin(p): # 
    """ 
    exp : exp PLUS exp
        | exp MINUS exp
        | exp MULTIPLY exp
        | exp DIVIDE exp 
        | exp MOD exp
        | exp POW exp
        
    """
    p[0] = (p[2], p[1], p[3]) # '1+2' -> ('+', '1', '2')

def p_statement_assignn(p): # assign int and double
    """
    stmt : TYPE_INT NAME SEMICOL
         | TYPE_STRING NAME SEMICOL
         | TYPE_CHAR NAME SEMICOL
         | TYPE_FLOAT NAME SEMICOL
         | TYPE_BOOL NAME SEMICOL
    """
    p[0] = ('assign', p[1] ,p[2] )
    
def p_statement_assign_val(p): # assign new string varuaible
    """
    stmt : TYPE_STRING NAME EQUALS exp SEMICOL
         | TYPE_CHAR NAME EQUALS exp SEMICOL
         | TYPE_BOOL NAME EQUALS condition SEMICOL
         | TYPE_INT NAME EQUALS exp SEMICOL
         | TYPE_FLOAT NAME EQUALS exp SEMICOL
         
    """
    p[0] = ('assign_val', p[2], p[4], p[1])

def p_bool(p):
    """
    BOOL : TRUE
         | FALSE
         
    """
    p[0] = p[1]

def p_exp_Uminus(p):
    """
    exp : MINUS exp
    """
    p[0] = ('*',( 'int' ,-1 ), p[2] )

def p_list_noVal(p):
    """
    stmt : TYPE_LIST NAME EQUALS listLparan listRparan SEMICOL
    """
    p[0] = ('assign_list_noVAl', p[2])

def p_list(p):
    """
    stmt : TYPE_LIST NAME EQUALS listLparan mult listRparan SEMICOL
    """
    p[0] = ('assign_list', p[2], p[5])
        
def p_multcond(p):
    """
    multcond : condition 
    
    """
    p[0] = [ p[1] ]

def p_mult_recur(p):
    """
    mult : multcond multrecurs
    
    """
    p[0] =  [ p[1] ] + p[2]

def p_mult_onnly(p):
    """
    multrecurs : COMMA mult
    
    """
    p[0] =  p[2]
        
def p_mult_empty(p):
    """
    multrecurs : 
    
    """
    p[0] =  []

def p_list_split(p):
    """
    exp : NAME SLICE LPAREN INT COMMA INT RPAREN
    
    """
    p[0] =  ( 'slice' , p[4] , p[6] , p[1]      )

def p_list_index(p):
    """
    exp : NAME INDEX INT RPAREN
        | NAME listLparan INT listRparan
    
    """
    p[0] =  ( 'INDEX', p[1] , p[3] )

def p_list_pop(p):
    """
    exp : NAME POP LPAREN INT RPAREN
    
    """
    p[0] =  ( 'POP', p[1] , p[4] )

def p_list_push(p):
    """
    stmt : NAME PUSH LPAREN condition RPAREN SEMICOL
    """
    p[0] =  ( 'PUSH', p[1] , p[4] )

def p_statement_update(p):
    """
    stmt : NAME EQUALS exp SEMICOL          
         
    """
    p[0] = ('update', p[1], p[3])

def p_expression_increment(p):
    """
    stmt : NAME INCREMENT SEMICOL
    """
    p[0] = ('increment', p[1])

def p_expression_decrement(p):
    """
    stmt : NAME DECREMENT SEMICOL
    """
    p[0] = ('decrement', p[1])
 
def p_If_stmt(p):
    """
    stmt : TYPE_IF LPAREN condition RPAREN COLON Bstmt tempElseIF hanElse   
    """
    if p[8] == -1:
        p[0] = ( 'IF', ('IF', p[3], p[6]) ,  p[7] )
    else:	
        p[0] = ( 'IF', ('IF', p[3], p[6]) ,  p[7]   ,  p[8] )

def p_else_if(p):
    """
    hanElseIf : TYPE_ELSEIF LPAREN condition RPAREN COLON Bstmt 
    
    """
    p[0] = ('ELSEIF', p[3] , p[6] )

def p_elseif_recur(p):
    """
    tempElseIF : hanElseIf tempElseIF
    
    """
    p[0] =  [ p[1] ] + p[2]

def p_elseif_empty(p):
    """
    tempElseIF : 
    
    """
    p[0] =  []

def p_else(p):
    """
    hanElse : TYPE_ELSE COLON Bstmt
    """
    p[0] = ('ELSE' , p[3])

def p_else_empty(p):
    """
    hanElse : 
    """
    p[0] = -1

def p_do_while(p):
    """
    stmt : TYPE_DO Bstmt TYPE_While LPAREN condition RPAREN SEMICOL 
    """
    p[0] = ( 'DO', p[2], p[5]  )

def p_Bstmt(p): 
    """
    Bstmt : LFUNCPARAN newS RFUNCPARAN  
    """
    p[0] = p[2]

def p_newS(p): 
    """
    newS : stmt newS
    """
    p[0] = [p[1]] + p[2]
    
def p_newS_empty(p):
    """
    newS : 
    """
    p[0] = []

def p_statement_FUCNTION_define(p): # 
    """
    stmt : TYPE_FUNCTION NAME LPAREN args RPAREN Bstmt
    """
    p[0] = ('FUNCTION_DEFINE', p[2] ,p[4], p[6] )

def p_args_def(p):
    """
    ArgDef : TYPE_STRING NAME 
         | TYPE_CHAR NAME 
         | TYPE_BOOL NAME 
         | TYPE_INT NAME 
         | TYPE_FLOAT NAME 
    """
    p[0] = [ (p[1],p[2]) ]

def p_args_recur(p):
    """
    args : ArgDef ArgsRecurs
    
    """
    p[0] =  [ p[1] ] + p[2]

def p_args_onnly(p):
    """
    ArgsRecurs : COMMA args
    
    """
    p[0] =  p[2]
        
def p_args_empty(p):
    """
    ArgsRecurs : 
    
    """
    p[0] =  []

def p_return(p):
    """
    stmt : TYPE_RETURN exp SEMICOL 
    
    """
    p[0] = ('RETURN', p[2])
	
	
	
	
	
	
	
def p_exp_funccall(p):
    """
    exp : NAME LPAREN many RPAREN
    
    """
    p[0] = ('CALL_FUNC', p[1], p[3])


def p_funcall_def(p):
    """
    manyDef : exp
    """
    p[0] = [ p[1] ]

def p_funcal_recur(p):
    """
    many : manyDef manyRecurs
    
    """
    p[0] =  [ p[1] ] + p[2]

def p_funcal_onnly(p):
    """
    manyRecurs : COMMA many
    
    """
    p[0] =  p[2]
        
def p_funcal_empty(p):
    """
    manyRecurs : 
    
    """
    p[0] =  []
   
def p_error(p):
    print("Syntax error at token", p.value, p.type, p.lexpos)
    exit(1)

parser = yacc.yacc() # start parsing, yacc object created
